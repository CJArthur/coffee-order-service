#--- Импорты aiogram ---#
from aiogram import Router, F
from aiogram.types import Message

# Роутер
settings_router = Router()

# заглушка настроек, где позже будут подгружаться данные из бд
@settings_router.message(F.text == "⚙️ Настройки")
async def check_settings(message: Message):
    await message.answer("*ℹ️ Ваши данные \n*" \
                         "Имя: \n" \
                         "Номер телефона: \n" \
                         "Почта: \n" \
                         "Платежная информация: ",
                         parse_mode = "Markdown")


