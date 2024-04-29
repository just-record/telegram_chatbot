from dotenv import load_dotenv
load_dotenv()
import os

from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, ContextTypes, CommandHandler

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="I'm a bot, please talk to me!"
    )


# 사용자가 Message를 입력 했을 때 답변해주는 함수입니다.
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text=update.message.text
    )

if __name__ == '__main__':
    telegram_token = os.getenv('TELEGRAM_TOKEN')
    application = ApplicationBuilder().token(telegram_token).build()

    start_handler = CommandHandler('start', start)
    # MessageHandler를 생성합니다.
    # filters.TEXT: 사용자가 입력한 메시지가 텍스트인지 확인합니다.
    # ~filters.COMMAND: 사용자가 입력한 메시지가 명령어(/start, /help)가 아닌지 확인합니다.
    # 2개의 조건이 참일 때 echo 함수가 실행됩니다.
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    
    application.add_handler(start_handler)
    # 생성한 MessageHandler를 application에 추가합니다.
    application.add_handler(echo_handler)

    application.run_polling()