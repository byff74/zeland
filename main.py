from cgitb import text
from email import message
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import sqlite3

bot = Bot(token='5316076461:AAEGsJkrkfIxXr8EeXuNbPf7pHKDAhD4-Ss')
dp = Dispatcher(bot)

button_card = KeyboardButton("Вытащить карту 💫")
button = ReplyKeyboardMarkup(resize_keyboard=True).add(button_card)   

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("Привет\n Нажми на кнопку и вытащи свою карту на день", reply_markup=button)

@dp.message_handler(text="Вытащить карту 💫")
async def send_welcome(message: types.Message):        
    conn = sqlite3.connect('zeland.db')    
    cur = conn.cursor()
    cur.execute("SELECT * FROM taro ORDER BY RANDOM() LIMIT 1")
    while True:
        cards = cur.fetchone()
        if cards == None:
            break
        cards_full = "КАРТА: " + cards[1].upper() + "\n\n✨ДЕКЛАРАЦИЯ✨\n\n " + cards[2] + "\n\n✨НАМЕРЕНИЕ✨\n\n " + cards[3] + "\n" + cards[4]
        await bot.send_message(message.chat.id, cards_full, reply_markup=button)  
        # await bot.send_message(message.chat.id, "✨КАРТА✨\n " + cards[1])  
        # await bot.send_message(message.chat.id, "✨ДЕКЛАРАЦИЯ✨\n " + cards[2])  
        # await bot.send_message(message.chat.id, "✨НАМЕРЕНИЕ✨\n " + cards[3])
        # await bot.send_message(message.chat.id, cards[4])
    cur.close()
    conn.close()

if __name__ == '__main__':
    executor.start_polling(dp)