from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.menuKeyboard import menu
from keyboards.default.buyurtma import buyurtma
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove
from states.buyurtmaState import buyurtma
from keyboards.default.tasdiq import tasdiq
from loader import dp

@dp.message_handler(text='⚡️ Ha')
async def bot_start(message: types.Message):
    await message.answer("Buyurtma alamga oshirildi", reply_markup=menu)
    await buyurtma.manzil.set()

@dp.message_handler(text='⛔️ Yo`q')
async def bot_start(message: types.Message):
    await message.answer("Buyurtma alamga oshirilmadi", reply_markup=menu)
    await buyurtma.manzil.set()
