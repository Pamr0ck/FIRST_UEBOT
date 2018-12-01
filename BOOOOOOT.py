import telebot
from collections import deque

queue = deque()  # массив с возможностью расширения и сжатия
# queue.append('name')-добавляет ячейку с информацией (name) в массив queue
# q.popleft()-удаляет нулевой элемент из массива и сдвигает все элементы на 1 влево
bot = telebot.TeleBot("782381386AAFLzg8wce1km24O2sspt_ObKHUwMeA_5yc")

@bot.message_handler(commands=['start', 'go'])
def handle_start(message):
        user_markup = telebot.types.ReplyKeyboardMarkup(true, false)
        user_markup.row("Хочу кофе", "Длина очереди?")
        user_markup.row("какой я по счету?", "Пропустить одного человека вперед", "Выйти из очереди")
        bot.send_message(message.chat.id, "Добро пожаловать:", reply_markup=user_markup)
        
@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text == "Hi":
        bot.send_message(message.from_user.id, "Hello! Want some..?")

    elif message.text == "How are you?" or message.text == "How are u?":
        bot.send_message(message.from_user.id, "Better than you while you haven't any coffee")

    else:  bot.send_message(message.from_user.id, "I can't understand you :c")

@bot.message_handler(command=["How_are_you"])
def handle_text(message):
    bot.send_message(message.chat.id, "I'm fine, thanks. And you?")

@bot.message_handler(command=["Coffee"])
def handle_text(message):
    bot.send_message(message.chat.id, "You are added to the stack, well done! :)")
    queue.append(chat.id)

@bot.message_handler(command=["Step_ahead"])
def handle_text(message):
    bot.send_message(message.chat.id, "Ok.....")
    N=queue.index(chat.id)
    queue[N+1],queue[N]=queue[N],queue[N+1]

@bot.message_handler(command=["My_number"])
def handle_text(message):
    bot.send_message(message.chat.id, "Ok.....Your number is ", queue.index(chat.id))


@bot.message_handler(command=["Show_queue"])
def handle_text(message):
    for i in queue:
        bot.send_message(message.chat.id, i)

@bot.message_handler(command=["Finish"])
def handle_text(message):
    bot.send_message(message.chat.id, "Oh, I didn't expect you to be such a one-minute man!")
    bot.send.message(message.queue[1],"You are next!!!!!!!!!")
    queue.popleft()

