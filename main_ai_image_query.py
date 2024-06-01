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
    model = "gpt-4o"
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


async def translation(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args #/translation 명령어 뒤에 입력한 텍스트를 args에 저장
    args_to_str = ' '.join(args) # args를 문자열로 변환

    query = f'{args_to_str}\n\n위의 문장을 영어로 번역해주세요.'

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

    await context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text=answer
    )     


async def generate_image(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args #/translation 명령어 뒤에 입력한 텍스트를 args에 저장
    args_to_str = ' '.join(args) # args를 문자열로 변환

    query = f'{args_to_str}'

    client = OpenAI()

    images = client.images.generate(
        model="dall-e-3",
        prompt=query,
        n=1,
        size="1024x1024"
    )    

    try:
        answer = images.data[0].url
    except Exception as e: # 예외 발생 시
        print(f'Error: {e}')
        answer = "죄송합니다. 인공지능이 답변을 생성하는 중에 오류가 발생했습니다."

    await context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text=answer
    )    


async def image_query(update: Update, context: ContextTypes.DEFAULT_TYPE):
    caption = update.message.caption
    query = caption if caption else '이미지를 설명해 주세요.'
    photo = update.message.photo[-1]
    photo_file = await photo.get_file()
    # await photo_file.download_to_drive('received_image.jpg')
    photo_file_dict = photo_file.to_dict()
    uploaded_file_url = photo_file_dict['file_path']

    client = OpenAI()

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": query},
                    {
                        "type": "image_url",
                        "image_url": {"url": f"{uploaded_file_url}"},
                    },
                ],
            }
        ],
        max_tokens=300,
    )

    answer = response.choices[0].message.content

    await context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text=answer
    )         


if __name__ == '__main__':
    telegram_token = os.getenv('TELEGRAM_TOKEN')
    application = ApplicationBuilder().token(telegram_token).build()

    start_handler = CommandHandler('start', start)
    answer_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), answer)
    translation_handler = CommandHandler('translation', translation)
    generate_image = CommandHandler('generation_image', generate_image)
    image_query_handler = MessageHandler(filters.PHOTO, image_query)
    
    application.add_handler(start_handler)
    application.add_handler(answer_handler)
    application.add_handler(translation_handler)
    application.add_handler(generate_image)
    application.add_handler(image_query_handler)

    application.run_polling()