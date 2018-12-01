import telebot
from collections import deque
queue = deque()  # массив с возможностью расширения и сжатия
queue_name=deque()
# queue.append('name')-добавляет ячейку с информацией (name) в массив queue
# q.popleft()-удаляет нулевой элемент из массива и сдвигает все элементы на 1 влево
bot = telebot.TeleBot("782381386:AAFLzg8wce1km24O2sspt_ObKHUwMeA_5yc")


@bot.message_handler(commands=['start', 'go'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
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
        if message.from_user.id not in queue:
            bot.send_message(message.from_user.id, "You are added to the stack, well done! :)")
            queue.append(message.from_user.id)
            queue_name.append(message.from_user.username)
    
    elif message.text =="Step_ahead":
        N = queue.index(message.from_user.id)
        if len(queue)>1 and N!=(len(queue)-1):
            queue[N + 1], queue[N] = queue[N], queue[N + 1]
            queue_name[N + 1], queue_name[N] = queue_name[N], queue_name[N + 1]
            bot.send_message(message.from_user.id, "Ok.....")            
        else:
            bot.send_message(message.from_user.id,"You one")
    elif message.text =="My_number":
        bot.send_message(message.from_user.id, "Ok.....Your number is ")
        N = queue.index(message.from_user.id)
        bot.send_message(message.from_user.id,(N+1))
        

    elif message.text == "Show_queue":
        for i in queue_name:
            bot.send_message(message.from_user.id, str(i))
      
    elif message.text == "Finish":
        bot.send_message(message.from_user.id, "Oh, I didn't expect you would be such a one-minute man!")
        N = queue.index(message.from_user.id)
        if len(queue)>1 and N==0:
            bot.send.message(queue[1], "You are next!!!!!!!!!")
            queue.popleft()
            queue_name.popleft()
        else:
            queue.pop(N)
            queue_name.pop(N)

    else: bot.send_message(message.from_user.id, "I can't understand you :c")

bot.polling(none_stop=True, interval=0)
