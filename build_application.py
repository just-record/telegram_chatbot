from dotenv import load_dotenv
load_dotenv()
import os

from telegram.ext import ApplicationBuilder

if __name__ == '__main__':
    # Telegram token from .env file
    telegram_token = os.getenv('TELEGRAM_TOKEN')
    # Create an instance of ApplicationBuilder
    application = ApplicationBuilder().token(telegram_token).build()

    print(application)