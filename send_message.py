from dotenv import load_dotenv
load_dotenv()
import os

import asyncio
import telegram


async def get_me(bot):
    async with bot:
        return await bot.get_me()
    

async def get_updates(bot):
    async with bot:
        return await bot.get_updates()
    
async def send_message(bot, chat_id, text):
    async with bot:
        await bot.send_message(text=text, chat_id=chat_id)


if __name__ == '__main__':
    telegram_token = os.getenv("TELEGRAM_TOKEN")
    bot = telegram.Bot(telegram_token)
    
    me = asyncio.run(get_me(bot=bot))
    print(me.to_dict())

    chat_id = ''
    updates = asyncio.run(get_updates(bot=bot))
    for i, update in enumerate(updates):
        if i == 0:
            chat_id = update.message.chat.id
        print(f'message: {update.message.text}')        # 메시지 내용  
        print(f'chat_id: {update.message.chat.id}')  # 채팅 사용자 Id

    text = "Hello, Telegram!"
    asyncio.run(send_message(bot=bot, chat_id=chat_id, text=text))

