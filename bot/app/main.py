#--- Основная библиотека ---#
import asyncio
from aiogram import Bot, Dispatcher

#--- Токен бота ---#
from config import BOT_TOKEN

#--- Запуск бота ---#
async def main():
    bot = Bot(BOT_TOKEN)
    dp = Dispatcher()

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())