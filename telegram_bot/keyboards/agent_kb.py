from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/Просмотреть_заявки')
b_yes = KeyboardButton('/Да')
b_no = KeyboardButton('/Нет')

agent_kb = ReplyKeyboardMarkup()
agent_kb.add(b1)

agent_accept_kb = ReplyKeyboardMarkup()
agent_accept_kb.add(b_yes).add(b_no)
