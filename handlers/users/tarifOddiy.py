from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.menuKeyboard import menu
from keyboards.default.buyurtma import buyurtma
from aiogram.types import ReplyKeyboardRemove
from loader import dp

@dp.message_handler(text='🚖 Buyurtma')
async def bot_start(message: types.Message):
    await message.answer("Manzilni kiriting 👇", reply_markup=ReplyKeyboardRemove())