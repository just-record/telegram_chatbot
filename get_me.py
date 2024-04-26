from dotenv import load_dotenv
load_dotenv()
import os

import asyncio
import telegram


async def get_me(bot):
    async with bot:
        return await bot.get_me()


if __name__ == '__main__':
    telegram_token = os.getenv("TELEGRAM_TOKEN")
    bot = telegram.Bot(telegram_token)
    
    me = asyncio.run(get_me(bot=bot))
    print(me.to_dict())