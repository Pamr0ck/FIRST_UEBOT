import telebot
from collections import deque

queue = deque()  # массив с возможностью расширения и сжатия
# queue.append('name')-добавляет ячейку с информацией (name) в массив queue
# q.popleft()-удаляет нулевой элемент из массива и сдвигает все элементы на 1 влево
bot = telebot.TeleBot("782381386:AAFLzg8wce1km24O2sspt_ObKHUwMeA_5yc")


@bot.message_handler(commands=['start', 'go'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup()
    user_markup.row("Coffee", "Show_queue")
    user_markup.row("My_number", "Step_ahead", "Finish")
    bot.send_message(message.chat.id, "Write smth)):", reply_markup=user_markup)


@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text == "Hi":
        bot.send_message(message.from_user.id, "Hello! Want some..?")

    elif message.text == "How are you?" or message.text == "How are u?":
        bot.send_message(message.from_user.id, "Better than you while you haven't any coffee")

    elif message.text == "Coffee":
        bot.send_message(message.from_user.id, "You are added to the stack, well done! :)")
        queue.append(message.from_user.id)
    
    elif message.text =="Step_ahead":
        bot.send_message(message.from_user.id, "Ok.....")
        N = queue.index(message.from_user.id)
        queue[N + 1], queue[N] = queue[N], queue[N + 1]
    
    elif message.text =="My_number":
        bot.send_message(message.from_user.id, "Ok.....Your number is ", queue.index(message.from_user.id))

    elif message.text == "Show_queue":
        for i in queue:
        bot.send_message(message.from_user.first_name, i)
      
    elif message.text == "Finish":
        bot.send_message(message.from_user.id, "Oh, I didn't expect you to be such a one-minute man!")
        bot.send.message(message.queue[1], "You are next!!!!!!!!!")
        queue.popleft()

    else: bot.send_message(message.from_user.id, "I can't understand you :c")

bot.polling(none_stop=True, interval=0)
