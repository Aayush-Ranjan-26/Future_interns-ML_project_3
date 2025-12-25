# 🤖 Customer Support Chatbot

A comprehensive customer support chatbot built with Python, featuring a Streamlit web interface and optional Telegram bot integration.

## ✨ Features

- **Smart Intent Recognition**: Matches user questions to appropriate responses
- **FAQ System**: Pre-loaded with common customer support questions and answers
- **Conversation Flow**: Handles greetings, goodbyes, and fallback responses
- **Web Interface**: Beautiful Streamlit-based chat interface
- **Telegram Integration**: Optional Telegram bot for messaging platforms
- **Conversation History**: Tracks user interactions
- **Sample Questions**: Quick access to common queries

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the Streamlit Web App

```bash
streamlit run streamlit_app.py
```

The app will open in your browser at `http://localhost:8501`


## 📁 Project Structure

```
.
├── chatbot_engine.py      # Main chatbot logic and intent matching
├── streamlit_app.py        # Web interface using Streamlit
├── telegram_bot.py         # Telegram bot integration
├── faq_data.json          # FAQ questions and answers database
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## 🎯 How It Works

### Chatbot Engine (`chatbot_engine.py`)

The core chatbot engine uses:
- **Text Normalization**: Converts text to lowercase and removes special characters
- **Similarity Matching**: Uses word-based similarity to match user queries to intents/FAQs
- **Intent Recognition**: Matches patterns to identify user intent (order status, refund, shipping, etc.)
- **Context Management**: Tracks conversation history and user context


### Web Interface (`streamlit_app.py`)

Features:
- Real-time chat interface
- Sample questions sidebar
- Conversation history
- Intent and confidence display
- Clear chat functionality


## 📚 Sample Questions

The chatbot can handle questions like:
- "Where is my order?"
- "What is your return policy?"
- "How can I track my order?"
- "Do you offer international shipping?"
- "What payment methods do you accept?"
- "How do I cancel my order?"
- "How do I contact customer service?"
- "Can I modify my order after placing it?"

## 🛠️ Technologies Used

- **Python**: Core programming language
- **Streamlit**: Web interface framework
- **python-telegram-bot**: Telegram Bot API integration
- **JSON**: Data storage for FAQs and intents
