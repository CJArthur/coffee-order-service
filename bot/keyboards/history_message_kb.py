#--- Импорты aiogram для кнопок ---#
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

make_order_review_ikb = InlineKeyboardMarkup(inline_keyboard = [
    [InlineKeyboardButton(text = "💬 Оставить отзыв", callback_data = "make_order_review")]
])