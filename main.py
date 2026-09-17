import os
os.system("cls" if os.name == "nt" else "clear")

import asyncio
import logging

from aiogram import Bot, Dispatcher

from config import BOT_TOKEN
from handlers.routers import router


dp = Dispatcher()

dp.include_router(router)


async def main():
    bot = Bot(token=BOT_TOKEN)

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
