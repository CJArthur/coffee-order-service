#--- ---#
import asyncio
from aiogram import Bot, Dispatcher

#--- ---#
from config import BOT_TOKEN

#--- ---#
import handlers.start_handler as start_handler


async def main():
    bot = Bot(BOT_TOKEN)
    dp = Dispatcher()

    #
    dp.include_router(start_handler.start_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())