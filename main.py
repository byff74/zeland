from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import sqlite3

bot = Bot(token='5316076461:AAEGsJkrkfIxXr8EeXuNbPf7pHKDAhD4-Ss')
dp = Dispatcher(bot)

button_card = KeyboardButton("Вытащить карту 💫")
button = ReplyKeyboardMarkup(resize_keyboard=True).add(button_card)   

conn = sqlite3.connect('zeland.db')    
cur = conn.cursor()

def db_table_val(id_user):
    cur.execute('INSERT INTO taro (id_user) VALUES (?)', (id_user,))
    conn.commit()

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):   
    await message.answer("Привет 👋\nНажми на кнопку и вытащи свою карту на день", reply_markup=button) 
    us_id = message.chat.id
    db_table_val(id_user = us_id)  

@dp.message_handler(text="Вытащить карту 💫")
async def send_welcome(message: types.Message):
    cur.execute("SELECT * FROM taro ORDER BY RANDOM() LIMIT 1")
    while True:
        cards = cur.fetchone()
        if cards == None:
            break
        cards_full = "КАРТА: " + cards[1].upper() + "\n\n✨ДЕКЛАРАЦИЯ✨\n\n " + cards[2] + "\n\n✨НАМЕРЕНИЕ✨\n\n " + cards[3] + "\n" + cards[4]
        await bot.send_message(message.chat.id, cards_full, reply_markup=button)          
    cur.close()
    conn.close()

if __name__ == '__main__':
    executor.start_polling(dp)