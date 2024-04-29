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


def get_openai_generate_image(client, model: str, prompt: str, n: int = 1, size: str = "1024x1024"):
    return client.images.generate(
        model=model,
        prompt=prompt,
        n=n,
        size=size
    )


def add_system_content(messages: List, system_message: str):
    messages.insert(0, {"role": "system", "content": system_message})


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="I'm a bot, please talk to me!"
    )


async def answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.message.text
    client = get_openai_client()
    model = "gpt-3.5-turbo-0613"
    messages = [{"role": "user", "content": query}]
    add_system_content(messages, "You are a helpful assistant.")
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

    await context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text=answer
    )    


async def generate_image(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.message.text
    client = get_openai_client()
    model = "dall-e-3"
    n = 1
    size = "1024x1024"
    images = get_openai_generate_image(
        client=client,
        model=model,
        prompt=query,
        n=n,
        size=size
    )

    try:
        # image_url = images.data[0].url
        answer = images.data[0].url
    except Exception as e: # 예외 발생 시
        print(f'Error: {e}')
        answer = "죄송합니다. 인공지능이 답변을 생성하는 중에 오류가 발생했습니다."

    await context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text=answer
    )        


if __name__ == '__main__':
    telegram_token = os.getenv('TELEGRAM_TOKEN')
    application = ApplicationBuilder().token(telegram_token).build()

    start_handler = CommandHandler('start', start)
    # answer_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), answer)
    answer_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), generate_image)
    
    application.add_handler(start_handler)
    application.add_handler(answer_handler)

    application.run_polling()