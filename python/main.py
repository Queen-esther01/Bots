import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
from telegram.constants import ChatAction

load_dotenv()

# Function that handles /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    await update.message.reply_text('Hello! I am your bot. How can I help you today?')

async def handle_message(update, context):
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action=ChatAction.TYPING)
    await update.message.reply_text('This is a test bot')

def main():
    # Use your bot token here
    application = ApplicationBuilder().token(os.getenv("BOT_TOKEN")).build()

    # Register the /start command
    application.add_handler(CommandHandler("start", start))

    # Register the message handler
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Run the bot until you send a signal to stop
    application.run_polling()

if __name__ == '__main__':
    main()