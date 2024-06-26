from typing import List
from dotenv import load_dotenv
load_dotenv()
import os

from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, ContextTypes, CommandHandler

from openai import OpenAI


def get_openai_client():
    return OpenAI()


def get_openai_chat_completion(client, model: str, messages: List ):
    return client.chat.completions.create(
        model=model,
        messages=messages
    )


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="I'm a bot, please talk to me!"
    )


# 채팅 메시지에 답변을 보내는 함수
async def answer(update: Update, context: ContextTypes.DEFAULT_TYPE):

    # 사용자가 보낸 메시지를 query 변수에 저장
    query = update.message.text
    
    client = get_openai_client()  # OpenAI API 클라이언트 생성
    model = "gpt-4o"  # 사용할 모델 이름
    # 사용자가 보낸 메시지를 OpenAI API에 user 역할로 전달
    messages = [{"role": "user", "content": query}]
    # OpenAI API로 답변 생성
    completion = get_openai_chat_completion(
        client=client, 
        model=model, 
        messages=messages
    )

    try:
        answer = completion.choices[0].message.content
    except Exception as e: # 예외 발생 시
        print(f'Error: {e}')
        answer = "죄송합니다. 인공지능이 답변을 생성하는 중에 오류가 발생했습니다."

    # OpenAI API의 답변을 사용자에게 전송
    await context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text=answer
    )


if __name__ == '__main__':
    telegram_token = os.getenv('TELEGRAM_TOKEN')
    application = ApplicationBuilder().token(telegram_token).build()

    start_handler = CommandHandler('start', start)
    # answer_handler를 생성
    answer_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), answer)
    
    application.add_handler(start_handler)
    application.add_handler(answer_handler)



    application.run_polling()