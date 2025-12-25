# 🚀 Quick Start Guide

Get your Customer Support Chatbot up and running in minutes!

## Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

## Step 2: Run the Web Interface

```bash
streamlit run streamlit_app.py
```

The chatbot will open in your browser automatically at `http://localhost:8501`

## Step 3: Test the Chatbot

Try asking questions like:
- "Where is my order?"
- "What is your return policy?"
- "How can I track my order?"
- "Do you offer international shipping?"

## Step 4: (Optional) Set Up Telegram Bot

1. **Create a Telegram Bot:**
   - Open Telegram and search for [@BotFather](https://t.me/botfather)
   - Send `/newbot` command
   - Follow the instructions to create your bot
   - Copy the bot token you receive

2. **Set the Token:**
   
   **Windows PowerShell:**
   ```powershell
   $env:TELEGRAM_BOT_TOKEN="your_bot_token_here"
   ```
   
   **Windows CMD:**
   ```cmd
   set TELEGRAM_BOT_TOKEN=your_bot_token_here
   ```
   
   **Linux/Mac:**
   ```bash
   export TELEGRAM_BOT_TOKEN="your_bot_token_here"
   ```

3. **Run the Telegram Bot:**
   ```bash
   python telegram_bot.py
   ```

4. **Test on Telegram:**
   - Search for your bot on Telegram
   - Send `/start` to begin
   - Try asking questions!

## 🎯 What's Included

✅ **Smart Intent Recognition** - Understands user questions  
✅ **FAQ System** - Pre-loaded with common support questions  
✅ **Web Interface** - Beautiful Streamlit chat interface  
✅ **Telegram Integration** - Optional messaging bot  
✅ **Conversation History** - Tracks all interactions  
✅ **Fallback Responses** - Handles unknown questions gracefully  

## 📝 Customization

### Add Your Own FAQs

Edit `faq_data.json` to add more questions and answers:

```json
{
  "faqs": [
    {
      "question": "Your question?",
      "answer": "Your answer."
    }
  ]
}
```

### Add New Intents

Add patterns and responses in `faq_data.json`:

```json
{
  "intents": [
    {
      "name": "your_intent",
      "patterns": ["pattern1", "pattern2"],
      "response": "Your response"
    }
  ]
}
```

## 🐛 Troubleshooting

**Issue:** Streamlit app won't start
- **Solution:** Make sure you've installed all dependencies: `pip install -r requirements.txt`

**Issue:** Telegram bot shows "Token not set" error
- **Solution:** Make sure you've set the `TELEGRAM_BOT_TOKEN` environment variable

**Issue:** Chatbot gives wrong answers
- **Solution:** Check `faq_data.json` and add more patterns to improve matching

## 📚 Next Steps

- Customize the FAQ data for your business
- Deploy to Streamlit Cloud (free)
- Connect to a database for conversation logging
- Add more advanced NLP features
- Integrate with Dialogflow for enhanced AI

---

**Happy Chatting! 🤖**

