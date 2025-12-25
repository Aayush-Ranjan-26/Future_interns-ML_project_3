"""
Telegram Bot Integration for Customer Support Chatbot
Run with: python telegram_bot.py

Before running, set your Telegram Bot Token in environment variable:
export TELEGRAM_BOT_TOKEN="your_bot_token_here"
Or create a .env file with TELEGRAM_BOT_TOKEN=your_token
"""

import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from chatbot_engine import get_chatbot

# Try to load from .env file
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # python-dotenv is optional

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Get bot token from environment variable
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

if not TELEGRAM_BOT_TOKEN:
    logger.error("TELEGRAM_BOT_TOKEN environment variable is not set!")
    logger.info("Please set it using: export TELEGRAM_BOT_TOKEN='your_token_here'")
    logger.info("Or create a .env file with TELEGRAM_BOT_TOKEN=your_token")
    exit(1)

# Initialize chatbot
chatbot = get_chatbot()


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /start command"""
    welcome_message = """
🤖 Welcome to Customer Support Chatbot!

I'm here to help you with:
• Order tracking
• Returns & refunds
• Shipping information
• Payment questions
• Account issues
• Product inquiries

Just send me a message and I'll help you!
    """
    await update.message.reply_text(welcome_message)


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /help command"""
    help_text = """
📚 Available Commands:
/start - Start the chatbot
/help - Show this help message
/clear - Clear conversation history

💡 Sample Questions:
• "Where is my order?"
• "What is your return policy?"
• "How can I track my order?"
• "Do you offer international shipping?"
• "What payment methods do you accept?"

Just ask me anything!
    """
    await update.message.reply_text(help_text)


async def clear_history(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /clear command"""
    user_id = str(update.effective_user.id)
    chatbot.clear_history(user_id)
    await update.message.reply_text("✅ Conversation history cleared!")


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle regular text messages"""
    user_message = update.message.text
    user_id = str(update.effective_user.id)
    
    # Show typing indicator
    await context.bot.send_chat_action(
        chat_id=update.effective_chat.id,
        action='typing'
    )
    
    # Process message with chatbot
    response = chatbot.process_message(user_message, user_id)
    
    # Send response
    await update.message.reply_text(response["response"])
    
    # Log the interaction
    logger.info(f"User {user_id}: {user_message}")
    logger.info(f"Bot response (intent: {response['intent']}, confidence: {response['confidence']:.2f})")


def main():
    """Start the Telegram bot"""
    logger.info("Starting Telegram bot...")
    
    # Create application
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    
    # Register handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("clear", clear_history))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # Start the bot
    logger.info("Bot is running...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == '__main__':
    main()

