
import logging
logging.basicConfig(level=logging.INFO)

from telegram.ext import Updater, CommandHandler, MessageHandler

TOKEN = "YOUR_BOT_TOKEN"

def start(update, context):
    update.message.reply_text("Welcome to my bot! I can help you with your questions.")

def ask(update, context):
    query = update.message.text
    client = Client("https://ysharma-explore-llamav2-with-tgi.hf.space/")
    result = client.predict(query, api_name="/chat")
    update.message.reply_text(result)

def main():
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("ask", ask))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
