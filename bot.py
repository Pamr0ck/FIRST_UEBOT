pip3 install pytelegrambotapi
import telebot
from collections import deque
from telebot import types

queue = deque()  # массив с возможностью расширения и сжатия
# queue.append('name')-добавляет ячейку с информацией ('name') в массив queue
# q.popleft()-удаляет нулевой элемент из массива и сдвигает все элементы на 1 влево
bot = telebot.TeleBot("782381386AAFLzg8wce1km24O2sspt_ObKHUwMeA_5yc")


@bot.message_handler(commands=['start', 'go'])
def handle_start(message):
        user_markup = telebot.types.ReplyKeyboardMarkup(true, false)
        user_markup.row("Хочу кофе", "Длина очереди?")
        user_markup.row("какой я по счету?", "Пропустить одного человека вперед", "Выйти из очереди")
        bot.send_message(message.chat.id, "Добро пожаловать:", reply_markup=user_markup)
@bot.message_handler  (commands=['stop'] )
def handle_start (message):
        hide_markup = elebot.types.ReplyKeyboardMarkup ()
        bot.send_message(message.chat.id, "...:", reply_markup=hide_markup)
        
        
            bot.send_message(message.from_user.id, "Окей, я добавил тебя в очередь!:)")
            # добавить чувака в стэк

        elif message.text == "Пропустить одного человека вперед": # пропустить одного человека вперед
            bot.send_message(message.from_user.id, "Ok...")
'''
        elif message.text == "Сколько человек передо мной" : #показать номер человека в очереди

        elif message.text == "Длина очрееди" : #показать всю очередь
            
        elif message.text=='Выйти из очереди': #выйти из очереди
            bot.send_message(message.from_user.id, "Oh, I didn't expect you to be such a one-minute man!")
            bot.send_message(message.from_user.id, 'you next')

        else:
            bot.send_message(message.from_user.id, "Sorry, i dont understand you.")
'''
