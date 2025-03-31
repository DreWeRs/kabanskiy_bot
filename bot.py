import asyncio
import logging

from aiogram import Bot, Dispatcher

from config.config import load_config
from handlers import main_menu


async def main():
    config = load_config()
    token = config.api_token
    bot = Bot(token=token)

    dp = Dispatcher()
    dp.include_routers(main_menu.router)

    try:
        await dp.start_polling(bot)
    finally:
        print('Bot has shut down')


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
