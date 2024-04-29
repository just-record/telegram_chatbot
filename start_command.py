from dotenv import load_dotenv
load_dotenv()
import os

from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

# '/start' 라는 명령어가 입력되면 실행되는 함수입니다.
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="I'm a bot, please talk to me!"
    )

if __name__ == '__main__':
    telegram_token = os.getenv('TELEGRAM_TOKEN')
    application = ApplicationBuilder().token(telegram_token).build()

    # CommandHandler를 생성합니다.
    # '/start' 라는 명령어가 입력되면 start 함수가 실행됩니다.
    start_handler = CommandHandler('start', start)
    # 생성한 CommandHandler를 application에 추가합니다.
    application.add_handler(start_handler)

    # 프로그램이 종료 되지 않고 계속 실행되면서 Polling 방식으로 메시지를 받아옵니다.
    # Ctrl + C 를 눌러서 프로그램을 종료할 수 있습니다.
    application.run_polling()