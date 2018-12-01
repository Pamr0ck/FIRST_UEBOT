import telebot
from collections import deque
import sys
queue = deque()  # массив с возможностью расширения и сжатия
queue_name = deque()
# queue.append('name')-добавляет ячейку с информацией (name) в массив queue
# q.popleft()-удаляет нулевой элемент из массива и сдвигает все элементы на 1 влево
bot = telebot.TeleBot("752631468:AAF94NeDyreo67Sg2sT7y_t9lBOxCmCwGTA")

sys.setrecursionlimit(100000000)

@bot.message_handler(commands=['start', 'go'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    user_markup.row("Coffee", "Show queue")
    user_markup.row("My number", "Step ahead", "Finish")
    bot.send_message(message.chat.id, "Write smth)):", reply_markup=user_markup)


@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text == "Hi":
        bot.send_message(message.from_user.id, "Hello! Want some..?")

    elif message.text == "How are you?" or message.text == "How are u?":
        bot.send_message(message.from_user.id, "Better than you while you haven't any coffee")

    elif message.text == "Coffee":
        if message.from_user.id not in queue:
            bot.send_message(message.from_user.id, "You are added to the stack, well done! :)")
            queue.append(message.from_user.id)
            queue_name.append(message.from_user.username)
        else:
            bot.send_message(message.from_user.id, "You're already in queue")

    elif message.text == "Step ahead":
        try:
            N = queue.index(message.from_user.id)
        except ValueError:
            N = None
        if len(queue) > 1 and N != (len(queue) - 1) and N != None:
            queue[N + 1], queue[N] = queue[N], queue[N + 1]
            queue_name[N + 1], queue_name[N] = queue_name[N], queue_name[N + 1]
            bot.send_message(message.from_user.id, "Ok.....")
            if N==0:
                bot.send_message(queue[0],"You are turn!!!!!!!!!")
        elif N != None and len(queue) == 1:
            bot.send_message(message.from_user.id, "You one")
        elif N != None and len(queue) - 1 == N:
            bot.send_message(message.from_user.id, "You are last")
        else:
            bot.send_message(message.from_user.id, "You not in stack")
    elif message.text == "My number":
        try:
            N = queue.index(message.from_user.id)
        except ValueError:
            N = None
        if N != None:
            bot.send_message(message.from_user.id, "Ok.....Your number is ")
            bot.send_message(message.from_user.id, (N + 1))
        else:
            bot.send_message(message.from_user.id, "You not in stack")

    elif message.text == "Show queue":
        for i in queue_name:
            bot.send_message(message.from_user.id, str(i))
        if len(queue) == 0:
            bot.send_message(message.from_user.id, "Nobody wants to have a cup of coffee, be first!=)")
    elif message.text == "Finish":
        try:
            N = queue.index(message.from_user.id)
        except ValueError:
            N = -1
        if len(queue) == 1 and N != -1:
            bot.send_message(message.from_user.id, "Oh, I didn't expect you would be such a one-minute man!")
            queue.popleft()
            queue_name.popleft()
        elif len(queue) > 1 and N == 0 and N != -1:
            bot.send_message(message.from_user.id, "Oh, I didn't expect you would be such a one-minute man!")
            bot.send_message(queue[1], "You are turn!!!!!!!!!")
            queue.popleft()
            queue_name.popleft()
        elif N != -1:
            bot.send_message(message.from_user.id, "Ok.....")
            queue.remove(message.from_user.id)
            queue_name.remove(message.from_user.username)
        else:
            bot.send_message(message.from_user.id, "You not in stack")


    else:
        bot.send_message(message.from_user.id, "I can't understand you :c")


def start():
    try:
        bot.polling(none_stop=True, interval=0)
    except:
        start()

def robuststart():
    try:
        start()
    except:
        robuststart()
start()

bot.polling(none_stop=True, interval=0)
