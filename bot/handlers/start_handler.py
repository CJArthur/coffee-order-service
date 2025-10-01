#--- Основные библиотеки ---#
from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Router

#--- Кнопки ---#
from keyboards.start_message_kb import start_msg_kb

# создаем Router
start_router = Router()

# команда /start
@start_router.message(Command("start"))
async def start_command_message(message: Message):
    await message.answer("Привет, я бот для онлайн оформления заказа в кофейне", reply_markup = start_msg_kb)