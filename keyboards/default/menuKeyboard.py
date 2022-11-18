from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🚖 Buyurtma'),
            KeyboardButton(text='📊 Hisobot')
        ],
        [
            KeyboardButton(text='📌 Kompaniya haqida'),
            KeyboardButton(text='🗒 Taklif')
        ]
        
    ],
    resize_keyboard=True

)