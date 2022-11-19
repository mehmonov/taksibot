from aiogram.dispatcher.filters.state import StatesGroup, State


# Shaxsiy ma'lumotlarni yig'sih uchun PersonalData holatdan yaratamiz
class buyurtma(StatesGroup):
    # Foydalanuvchi buyerda 3 ta holatdan o'tishi kerak
    manzil = State() # ism
    hudud = State() # email
    