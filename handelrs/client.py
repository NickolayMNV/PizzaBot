# import aiogram
from aiogram import types, Dispatcher
from keyboards import kb_client
from create_bot import dp, bot
from aiogram.types import ReplyKeyboardRemove
from data_base import sqlite_db as sql

# @dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Приятного аппетита', reply_markup=kb_client)
    except:
        await message.reply("Бот не может начать общение первым, напишите ему:\nhttps://web.telegram.org/a/#6375956995")


# @dp.message_handler(commands=['Режим_работы'])
async def pizza_work(message: types.Message):
    await bot.send_message(message.from_user.id, "Вс-Чт с 9:00 до 00:00, Пт-Сб с 8:00 до 01:00")

# @dp.message_handler(commands=['Расположение'])
async def pizza_location(message: types.Message):
    await bot.send_message(message.from_user.id, "Ул. Колбасная 15")

@dp.message_handler(commands=['Меню'])
async def pizza_menu_command(message: types.Message):
    await sql.sql_read(message)




def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(pizza_work, commands=['Режим_работы'])
    dp.register_message_handler(pizza_location, commands=['Расположение'])
    dp.register_message_handler(pizza_menu_command, commands=['Меню'])

