"""
Streamlit Web Interface for Customer Support Chatbot
Run with: streamlit run streamlit_app.py
"""

import streamlit as st
import json
from chatbot_engine import get_chatbot, CustomerSupportChatbot
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Customer Support Chatbot",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better UI
st.markdown("""
    <style>
    .chat-message {
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
        display: flex;
        align-items: flex-start;
    }
    .user-message {
        background-color: #e3f2fd;
        margin-left: 20%;
    }
    .bot-message {
        background-color: #f5f5f5;
        margin-right: 20%;
    }
    .stButton>button {
        width: 100%;
        border-radius: 0.5rem;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'chatbot' not in st.session_state:
    st.session_state.chatbot = get_chatbot()
    st.session_state.messages = []
    st.session_state.user_id = f"user_{datetime.now().timestamp()}"

# Sidebar
with st.sidebar:
    st.title("🤖 Chatbot Settings")
    
    st.markdown("### Quick Actions")
    if st.button("🔄 Clear Chat History"):
        st.session_state.messages = []
        st.session_state.chatbot.clear_history(st.session_state.user_id)
        st.rerun()
    
    st.markdown("---")
    st.markdown("### 📚 Sample Questions")
    sample_questions = [
        "Where is my order?",
        "What is your return policy?",
        "How can I track my order?",
        "Do you offer international shipping?",
        "What payment methods do you accept?",
        "How do I cancel my order?",
        "How do I contact customer service?",
        "Can I modify my order after placing it?"
    ]
    
    for question in sample_questions:
        if st.button(f"💬 {question}", key=f"sample_{question}"):
            # Process the sample question
            response = st.session_state.chatbot.process_message(
                question, 
                st.session_state.user_id
            )
            st.session_state.messages.append({
                "role": "user",
                "content": question,
                "timestamp": datetime.now().isoformat()
            })
            st.session_state.messages.append({
                "role": "assistant",
                "content": response["response"],
                "intent": response["intent"],
                "confidence": response["confidence"],
                "timestamp": response["timestamp"]
            })
            st.rerun()
    
    st.markdown("---")
    st.markdown("### ℹ️ About")
    st.info("""
    **Customer Support Chatbot**
    
    This chatbot can help you with:
    - Order tracking
    - Returns & refunds
    - Shipping information
    - Payment questions
    - Account issues
    - Product inquiries
    
    Ask me anything!
    """)

# Main chat interface
st.title("🤖 Customer Support Chatbot")
st.markdown("Welcome! I'm here to help you with your questions. Type your message below or click a sample question from the sidebar.")

# Display chat history
chat_container = st.container()
with chat_container:
    for message in st.session_state.messages:
        if message["role"] == "user":
            with st.chat_message("user"):
                st.write(message["content"])
        else:
            with st.chat_message("assistant"):
                st.write(message["content"])
                # Show intent and confidence in a small text
                if message.get("intent") and message.get("intent") != "fallback":
                    st.caption(f"Intent: {message.get('intent')} | Confidence: {message.get('confidence', 0):.2f}")

# Chat input
user_input = st.chat_input("Type your message here...")

if user_input:
    # Add user message to chat
    st.session_state.messages.append({
        "role": "user",
        "content": user_input,
        "timestamp": datetime.now().isoformat()
    })
    
    # Get bot response
    with st.spinner("Thinking..."):
        response = st.session_state.chatbot.process_message(
            user_input,
            st.session_state.user_id
        )
    
    # Add bot response to chat
    st.session_state.messages.append({
        "role": "assistant",
        "content": response["response"],
        "intent": response["intent"],
        "confidence": response["confidence"],
        "timestamp": response["timestamp"]
    })
    
    st.rerun()

