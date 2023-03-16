from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from validation import *

from keyboards import get_kb

import os

bot = Bot(token='6173771315:AAGff0teIypm7U32SDXzHdjdzN23cxtCID4')
dp = Dispatcher(bot)

smth_went_wrong = 'Что-то пошло не так'
shit = 'I shat myself'
user_s = 'User'
agent_s = 'Agent'
lord_s = 'Lord'

# agent
@dp.message_handler(commands=['просмотреть_заявки'])
async def show(message: types.Message):
    ans, u_type = user_vald(message.from_user.id)
    if not ans or u_type != agent_s:
        print(1)
        await message.answer(smth_went_wrong)
        return
    suc, appl = get_appl_by_id(message.from_user.id)
    if not suc:
        print(2)
        await message.answer(smth_went_wrong)
        return
    suc = add_to_pend(message.from_user.id, appl)
    if not suc:
        print(3)
        await message.answer(smth_went_wrong)
        return
    text = appl['text']
    await message.answer(text, reply_markup=get_kb('Accept'))


@dp.message_handler(commands=['да'])
async def accept(message: types.Message):
    ans, u_type = user_vald(message.from_user.id)
    if not ans or u_type != agent_s:
        print(1)
        await message.answer(smth_went_wrong)
    suc, appl = get_pending_by_id(message.from_user.id)
    if not suc:
        print(2)
        await message.answer(smth_went_wrong)
        return
    suc = add_for_site(appl)
    if not suc:
        print(3)
        await message.answer(smth_went_wrong)
        return
    await message.answer('Заявка успешно принята')

@dp.message_handler(commands=['нет'])
async def decline(message: types.Message):
    ans, u_type = user_vald(message.from_user.id)
    if not ans or u_type != agent_s:
        await message.answer(smth_went_wrong)
    suc, appl = get_pending_by_id(message.from_user.id)
    if not suc:
        await message.answer(smth_went_wrong)
        return
    await message.answer('Заявка успешно отклонена')


# common
@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    ans, u_type = user_vald(message.from_user.id)
    kb = get_kb(u_type)
    if u_type == shit:
        await message.answer(smth_went_wrong)
        return
    if ans:
        await message.answer('Вы уже валидированы, добро пожаловать обратно', reply_markup=kb)
        return
    await message.answer('Введите, пожалуйста, свой ключ')


# user
@dp.message_handler(commands=['подтвердить_оплату'])
async def start(message: types.Message):
    if are_they(message.from_user.id, user_s):
        await message.answer('Оплата прошла успешно')
    else:
        await message.answer(smth_went_wrong)

# lord
@dp.message_handler(commands=['подать_заявку'])
async def start(message: types.Message):
    if are_they(message.from_user.id, lord_s):
        await message.answer('Пожалуйста, опишите жилье, которое вы сдаёте. Не забудьте указать ваш адрес,'
                             ' контактные данные и посуточную цену')
    else:
        await message.answer(smth_went_wrong)

@dp.message_handler(content_types=['text'])
async def key_validation(message: types.Message):
    # if user is already validated we dont need to do anything
    suc, u_type = user_vald(message.from_user.id)
    if suc:
        # lord application
        if are_they(message.from_user.id, lord_s):
            suc = add_appl(message.text, str(message.from_user.id))
            if not suc:
                await message.answer(smth_went_wrong)
        return

    val = key_vald(message.text)
    val_result = val[0]
    user_type = val[1]

    if val_result:
        await message.answer('Успешно')
    else:
        await message.answer('Неверный ключ, попробуйте снова или получите ключ у местного территориального агента')

    # telling user who they are in case of wrong description of key
    kb = get_kb(user_type)

    if user_type == 'User':
        await message.answer('Вы квартирант', reply_markup=kb)
    elif user_type == 'Agent':
        await message.answer('Вы территориальный агент', reply_markup=kb)
    elif user_type == 'Lord':
        await message.answer('Вы арендодатель', reply_markup=kb)

    else:
        await message.answer('Что-то пошло не так, попробуйте снова')

    add_user(message.from_user.id, user_type, message.text)






executor.start_polling(dp, skip_updates=True)