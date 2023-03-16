from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/Подтвердить_оплату')

user_kb = ReplyKeyboardMarkup()
user_kb.add(b1)
