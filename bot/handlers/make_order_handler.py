#--- Импорты aiogram---#
from aiogram import Router, F
from aiogram.types import Message

#--- Ипорты состояния ---#
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup


# Роутер
make_order_router = Router()

# Класс состояния
class OrderSteps(StatesGroup):
    select_main_product = State()


@make_order_router.message(F.text == "📋 Сделать заказ")
async def choose_product(message: Message, state = FSMContext):
    await message.answer("ща будем тебе ебашить заказ падажи")

    await state.set_state(OrderSteps.select_main_product)

#@make_order_router(OrderSteps.select_main_product)
