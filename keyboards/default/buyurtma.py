from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

buyurtma = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🚕 Oddiy"),
            KeyboardButton(text="⚡️ Tezkor"),
            
        ],
        [
            KeyboardButton(text="🛵 Yetkazma"),
            KeyboardButton(text="🚖 Komfort"),
            
        ],
        [
            KeyboardButton(text='⬅️ Orqaga')
        ]
    ],
    resize_keyboard=True
)