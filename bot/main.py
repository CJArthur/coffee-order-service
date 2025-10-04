#--- Библиотеки ---#
import asyncio
from aiogram import Bot, Dispatcher

#--- Токен бота ---#
from config import BOT_TOKEN

#--- Ипортируем handlers ---#
import handlers.start_handler as start_handler
import handlers.make_order_handler as make_order_handler
import handlers.settings_handler as settings_handler
import handlers.history_handler as history_handler


async def main():
    bot = Bot(BOT_TOKEN)
    dp = Dispatcher()

    # Объявляем роутеры
    dp.include_router(start_handler.start_router)
    dp.include_router(make_order_handler.make_order_router)
    dp.include_router(settings_handler.settings_router)
    dp.include_router(history_handler.history_router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())