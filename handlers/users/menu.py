from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.menuKeyboard import menu
from keyboards.default.buyurtma import buyurtma
from loader import dp


@dp.message_handler(text='🚖 Buyurtma')
async def bot_start(message: types.Message):
    await message.answer(f"Bu yurtma turini tanlang: 👇 \n \n 🚕 Oddiy  -  Minimal summa - 5000 so'm. 1km - 500 so'm.  Nexia, matiz. \n \n  ⚡️ Tezkor - 5 daqiqada kelishi ta'minlanadi. Minimal summa - 500 so'm. \n \n 🛵 Yetkazib berish - Minimal summa - 5000 so'm.  1km - 500 so'm \n \n 🚖 Komfort - Komfort mashina. Konditsioner. Minimal summa - 5000  so'm.  1km - 500 so'm \n \n Barcha tarifda minimal yo'nalish 3 km.",reply_markup=buyurtma)
