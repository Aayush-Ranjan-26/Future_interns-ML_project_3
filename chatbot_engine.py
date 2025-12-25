"""
Customer Support Chatbot Engine
Handles intent recognition, FAQ matching, and conversation flow
"""

import re
import json
from typing import Dict, List, Optional
from datetime import datetime
import random


class CustomerSupportChatbot:
    """Main chatbot engine for customer support"""
    
    def __init__(self, faq_file: str = "faq_data.json"):
        """Initialize the chatbot with FAQ data"""
        self.faq_data = self._load_faq_data(faq_file)
        self.conversation_history = []
        self.user_context = {}
        self.greetings = [
            "Hi! How can I help you today?",
            "Hello! What can I assist you with?",
            "Hey there! How may I help you?",
            "Welcome! How can I support you today?"
        ]
        self.fallback_responses = [
            "I'm sorry, I didn't quite understand that. Could you please rephrase your question?",
            "I'm not sure I understand. Can you provide more details?",
            "Let me help you better. Could you ask your question in a different way?",
            "I'm here to help! Could you clarify what you need assistance with?"
        ]
        
    def _load_faq_data(self, faq_file: str) -> Dict:
        """Load FAQ data from JSON file"""
        try:
            with open(faq_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            # Return default FAQ structure if file doesn't exist
            return {
                "intents": [],
                "faqs": []
            }
    
    def _normalize_text(self, text: str) -> str:
        """Normalize text for better matching"""
        text = text.lower().strip()
        # Remove special characters but keep spaces
        text = re.sub(r'[^\w\s]', '', text)
        return text
    
    def _calculate_similarity(self, text1: str, text2: str) -> float:
        """Calculate simple word-based similarity"""
        words1 = set(self._normalize_text(text1).split())
        words2 = set(self._normalize_text(text2).split())
        
        if not words1 or not words2:
            return 0.0
        
        intersection = words1.intersection(words2)
        union = words1.union(words2)
        
        return len(intersection) / len(union) if union else 0.0
    
    def _check_greeting(self, user_input: str) -> bool:
        """Check if user input is a greeting"""
        greeting_keywords = [
            'hi', 'hello', 'hey', 'greetings', 'good morning', 
            'good afternoon', 'good evening', 'sup', 'what\'s up'
        ]
        normalized = self._normalize_text(user_input)
        # Check if input starts with greeting or is very short (likely a greeting)
        words = normalized.split()
        if len(words) <= 3:  # Short messages are likely greetings
            return any(keyword in normalized for keyword in greeting_keywords)
        # For longer messages, check if it starts with a greeting
        return words[0] in greeting_keywords or any(f"{keyword} " in normalized for keyword in greeting_keywords)
    
    def _check_goodbye(self, user_input: str) -> bool:
        """Check if user input is a goodbye"""
        goodbye_keywords = [
            'bye', 'goodbye', 'see you', 'farewell', 'exit', 
            'quit', 'thanks', 'thank you', 'done'
        ]
        normalized = self._normalize_text(user_input)
        return any(keyword in normalized for keyword in goodbye_keywords)
    
    def _match_intent(self, user_input: str) -> Optional[Dict]:
        """Match user input to an intent"""
        best_match = None
        best_score = 0.0
        threshold = 0.4  # Minimum similarity threshold (increased for better accuracy)
        
        normalized_input = self._normalize_text(user_input)
        
        # Check intents - try exact keyword matching first
        for intent in self.faq_data.get("intents", []):
            for pattern in intent.get("patterns", []):
                # Check if pattern keywords are in the input
                pattern_words = set(pattern.split())
                input_words = set(normalized_input.split())
                
                # If all pattern words are in input, it's a strong match
                if pattern_words.issubset(input_words) and len(pattern_words) > 0:
                    similarity = 0.9  # High confidence for keyword match
                else:
                    similarity = self._calculate_similarity(normalized_input, pattern)
                
                if similarity > best_score and similarity >= threshold:
                    best_score = similarity
                    best_match = intent
        
        return best_match if best_match else None
    
    def _match_faq(self, user_input: str) -> Optional[Dict]:
        """Match user input to FAQ questions"""
        best_match = None
        best_score = 0.0
        threshold = 0.35  # Minimum similarity threshold
        
        normalized_input = self._normalize_text(user_input)
        
        # Check FAQs - prioritize exact question matches
        for faq in self.faq_data.get("faqs", []):
            question = faq.get("question", "")
            normalized_question = self._normalize_text(question)
            
            # Check for exact or near-exact match
            if normalized_input == normalized_question:
                similarity = 1.0
            # Check if question keywords are in input
            elif normalized_input in normalized_question or normalized_question in normalized_input:
                similarity = 0.85
            else:
                similarity = self._calculate_similarity(normalized_input, normalized_question)
            
            if similarity > best_score and similarity >= threshold:
                best_score = similarity
                best_match = faq
        
        return best_match if best_match else None
    
    def process_message(self, user_input: str, user_id: str = "default") -> Dict:
        """
        Process user message and return response
        
        Returns:
            Dict with 'response', 'intent', 'confidence', and 'timestamp'
        """
        if not user_input or not user_input.strip():
            return {
                "response": "Please enter a message.",
                "intent": None,
                "confidence": 0.0,
                "timestamp": datetime.now().isoformat()
            }
        
        # Store in conversation history
        self.conversation_history.append({
            "user_id": user_id,
            "user_message": user_input,
            "timestamp": datetime.now().isoformat()
        })
        
        # Check for goodbye first (very specific)
        if self._check_goodbye(user_input):
            return {
                "response": "Thank you for contacting us! Have a great day! 😊",
                "intent": "goodbye",
                "confidence": 1.0,
                "timestamp": datetime.now().isoformat()
            }
        
        # Try to match FAQ first (more specific)
        faq_match = self._match_faq(user_input)
        faq_score = 0.0
        if faq_match:
            # Calculate FAQ match score
            normalized_input = self._normalize_text(user_input)
            normalized_question = self._normalize_text(faq_match.get("question", ""))
            faq_score = self._calculate_similarity(normalized_input, normalized_question)
        
        # Try to match intent
        intent_match = self._match_intent(user_input)
        intent_score = 0.0
        if intent_match:
            # Calculate intent match score
            normalized_input = self._normalize_text(user_input)
            best_pattern_score = 0.0
            for pattern in intent_match.get("patterns", []):
                score = self._calculate_similarity(normalized_input, pattern)
                if score > best_pattern_score:
                    best_pattern_score = score
            intent_score = best_pattern_score
        
        # Prioritize FAQ if it has higher confidence
        if faq_match and faq_score >= 0.4:
            return {
                "response": faq_match.get("answer", ""),
                "intent": "faq",
                "confidence": faq_score,
                "timestamp": datetime.now().isoformat()
            }
        
        # Use intent if it has good confidence
        if intent_match and intent_score >= 0.4:
            response = intent_match.get("response", "")
            # Handle dynamic responses
            if "{order_id}" in response and "order_id" in self.user_context.get(user_id, {}):
                response = response.replace("{order_id}", self.user_context[user_id]["order_id"])
            
            return {
                "response": response,
                "intent": intent_match.get("name", "unknown"),
                "confidence": intent_score,
                "timestamp": datetime.now().isoformat()
            }
        
        # Fallback to FAQ if available (lower threshold)
        if faq_match:
            return {
                "response": faq_match.get("answer", ""),
                "intent": "faq",
                "confidence": faq_score,
                "timestamp": datetime.now().isoformat()
            }
        
        # Check for greetings (after other checks to avoid false positives)
        if self._check_greeting(user_input):
            response = random.choice(self.greetings)
            return {
                "response": response,
                "intent": "greeting",
                "confidence": 1.0,
                "timestamp": datetime.now().isoformat()
            }
        
        # Fallback response
        return {
            "response": random.choice(self.fallback_responses),
            "intent": "fallback",
            "confidence": 0.0,
            "timestamp": datetime.now().isoformat()
        }
    
    def get_conversation_history(self, user_id: str = "default") -> List[Dict]:
        """Get conversation history for a user"""
        return [msg for msg in self.conversation_history if msg.get("user_id") == user_id]
    
    def clear_history(self, user_id: str = "default"):
        """Clear conversation history for a user"""
        self.conversation_history = [
            msg for msg in self.conversation_history if msg.get("user_id") != user_id
        ]


# Initialize global chatbot instance
_chatbot_instance = None

def get_chatbot() -> CustomerSupportChatbot:
    """Get or create chatbot instance (singleton pattern)"""
    global _chatbot_instance
    if _chatbot_instance is None:
        _chatbot_instance = CustomerSupportChatbot()
    return _chatbot_instance

