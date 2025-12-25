"""
Simple test script to verify the chatbot is working correctly
Run with: python test_chatbot.py
"""

import sys
from chatbot_engine import CustomerSupportChatbot

# Fix encoding for Windows console
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def test_chatbot():
    """Test the chatbot with sample questions"""
    print("Testing Customer Support Chatbot\n")
    print("=" * 50)
    
    chatbot = CustomerSupportChatbot()
    
    # Test cases
    test_cases = [
        "Hello",
        "Where is my order?",
        "What is your return policy?",
        "How can I track my order?",
        "Do you offer international shipping?",
        "What payment methods do you accept?",
        "How do I cancel my order?",
        "This is a random question that doesn't match anything",
        "Thank you, goodbye!"
    ]
    
    for i, question in enumerate(test_cases, 1):
        print(f"\n[{i}] User: {question}")
        response = chatbot.process_message(question)
        print(f"Bot: {response['response']}")
        print(f"Intent: {response['intent']} | Confidence: {response['confidence']:.2f}")
        print("-" * 50)
    
    print("\nChatbot test completed!")

if __name__ == "__main__":
    test_chatbot()

