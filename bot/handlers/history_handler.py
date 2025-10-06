#--- Импорты aiogram ---#
from aiogram import Router, F
from aiogram.types import Message

#--- Кнопки ---#
from keyboards.history_message_kb import make_order_review_ikb

# Роутер
history_router = Router()

# заглушка кнопки история заказов
@history_router.message(F.text == "🔄 История заказов")
async def order_history(message: Message):
    await message.answer("*История заказов \n*" \
                         "Дата: \n" \
                         "Место: \n" \
                         "Содержимое: ",
                         reply_markup = make_order_review_ikb,
                         parse_mode = "Markdown")