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

### 3. (Optional) Run Telegram Bot

1. Create a Telegram bot by messaging [@BotFather](https://t.me/botfather) on Telegram
2. Get your bot token
3. Set the token as an environment variable:

**Windows (PowerShell):**
```powershell
$env:TELEGRAM_BOT_TOKEN="your_bot_token_here"
python telegram_bot.py
```

**Windows (CMD):**
```cmd
set TELEGRAM_BOT_TOKEN=your_bot_token_here
python telegram_bot.py
```

**Linux/Mac:**
```bash
export TELEGRAM_BOT_TOKEN="your_bot_token_here"
python telegram_bot.py
```

Or create a `.env` file:
```
TELEGRAM_BOT_TOKEN=your_bot_token_here
```

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

### FAQ System (`faq_data.json`)

The FAQ system includes:
- **Intents**: Pattern-based matching for common queries
- **FAQs**: Direct question-answer pairs
- **Responses**: Contextual responses that can include dynamic content

### Web Interface (`streamlit_app.py`)

Features:
- Real-time chat interface
- Sample questions sidebar
- Conversation history
- Intent and confidence display
- Clear chat functionality

### Telegram Bot (`telegram_bot.py`)

Features:
- `/start` - Welcome message
- `/help` - Show help information
- `/clear` - Clear conversation history
- Natural language processing for all text messages

## 🔧 Customization

### Adding New FAQs

Edit `faq_data.json` to add new questions and answers:

```json
{
  "faqs": [
    {
      "question": "Your question here?",
      "answer": "Your answer here."
    }
  ]
}
```

### Adding New Intents

Add new intents to `faq_data.json`:

```json
{
  "intents": [
    {
      "name": "intent_name",
      "patterns": [
        "pattern 1",
        "pattern 2",
        "pattern 3"
      ],
      "response": "Response text here"
    }
  ]
}
```

### Adjusting Similarity Threshold

In `chatbot_engine.py`, modify the `threshold` value in `_match_intent()` and `_match_faq()` methods (default: 0.3)

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

## 🎓 Learning Outcomes

By building this chatbot, you'll learn:
- 🤖 How chatbots work in websites and apps
- 💬 Designing real conversations (greeting, help, fallback)
- 🧠 Understanding how AI matches user questions to answers
- 📲 Basic deployment on web or messaging platforms
- 🔧 Intent recognition and pattern matching
- 📊 Conversation flow management

## 🛠️ Technologies Used

- **Python**: Core programming language
- **Streamlit**: Web interface framework
- **python-telegram-bot**: Telegram Bot API integration
- **JSON**: Data storage for FAQs and intents

## 🔄 Next Steps

### Advanced Features (Optional)

1. **Connect to Dialogflow**: Integrate with Google Dialogflow for more advanced NLP
2. **Database Integration**: Store conversations in a database (SQLite, PostgreSQL)
3. **Email Integration**: Send support tickets to email
4. **Airtable/Notion Integration**: Create support tickets in external systems
5. **Multi-language Support**: Add support for multiple languages
6. **Sentiment Analysis**: Analyze user sentiment to improve responses
7. **Machine Learning**: Train a model on customer support datasets

### Deployment

- **Streamlit Cloud**: Deploy the Streamlit app for free
- **Heroku**: Deploy both web app and Telegram bot
- **AWS/GCP**: Deploy on cloud platforms
- **Docker**: Containerize the application

## 📝 License

This project is open source and available for educational purposes.

## 🤝 Contributing

Feel free to fork this project and add your own features!

## 📞 Support

For questions or issues, please open an issue on the repository.

---

**Happy Chatbot Building! 🚀**

