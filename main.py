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
    cur.execute('INSERT INTO users (id_users) VALUES (?)', (id_user,))
    conn.commit()

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):   
    await message.answer("Привет 👋\nНажми на кнопку и вытащи свою карту на день", reply_markup=button) 
    us_id = message.from_user.id
    db_table_val(id_user = us_id)    

@dp.message_handler(text="Вытащить карту 💫")
async def send_welcome(message: types.Message):
    cards = cur.execute("SELECT * FROM taro ORDER BY RANDOM() LIMIT 1").fetchone()
    id = cur.execute("SELECT id_users FROM users").fetchall()
    us_id = message.from_user.id,
    while True:        
        if cards == None:
            break
        cards_full = "КАРТА: " + cards[1].upper() + "\n\n✨ДЕКЛАРАЦИЯ✨\n\n " + cards[2] + "\n\n✨НАМЕРЕНИЕ✨\n\n " + cards[3] + "\n" + cards[4]
        await bot.send_message(message.chat.id, cards_full, reply_markup=button) 
        break  
    if us_id in id:
        print("true")  
    else:
        print("false")    

if __name__ == '__main__':
    executor.start_polling(dp)