from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


start_msg_kb = ReplyKeyboardMarkup(keyboard = [
               [KeyboardButton(text = "📋 Сделать заказ")],
               [KeyboardButton(text = "⚙️ Настройки"),
                KeyboardButton(text = "🔄 История заказов")] ], resize_keyboard = True)