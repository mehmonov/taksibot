from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.menuKeyboard import menu
from keyboards.default.buyurtma import buyurtma
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove
from states.buyurtmaState import buyurtma
from loader import dp

@dp.message_handler(text='🚖 Buyurtma')
async def bot_start(message: types.Message):
    await message.answer("Manzilni kiriting 👇", reply_markup=ReplyKeyboardRemove())
    await buyurtma.fullName.set()

@dp.message_handler(state=buyurtma.manzil)
async def answer_manzil(message: types.Message, state: FSMContext):
    manzil = message.text

    await state.update_data(
        {"manzil": manzil}
    )

    await message.answer("Hududni tanlang")

    # await PersonalData.email.set()
    await buyurtma.next()
    
@dp.message_handler(state=buyurtma.hudud)
async def answer_hudud(message: types.Message, state: FSMContext):
    hudud = message.text

    await state.update_data(
        {"hudud": hudud}
    )
    data = await state.get_data()
    manzil = data.get("manzil")
    hudud = data.get("hudud")
   
    msg = "Quyidagi ma`lumotlar qabul qilindi:\n"
    msg += f"Manzil -<b> {manzil}</b>\n"
    msg += f"Manzil -<b> {hudud}</b>\n"
    
    await message.answer(msg)


    # await PersonalData.email.set()
    await  state.finish()
