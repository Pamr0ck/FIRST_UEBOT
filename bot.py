import telebot
from collection import deque
queue=deque()
#queue.append('name')-добавляет ячейку с информацией (name) в массив queue
#q.popleft()-удаляет нулевой элемент из массива и сдвигает все элементы на 1 влево
bot = telebot.TeleBot("782381386AAFLzg8wce1km24O2sspt_ObKHUwMeA_5yc")


@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text == "Hi":
        bot.send_message(message.from_user.id, "Hello! I am HabrahabrExampleBot. How can i help you?")

    elif message.text == "How are you?" or message.text == "How are u?":
        bot.send_message(message.from_user.id, "I'm fine, thanks. And you?")

    elif message.text == "Cofee":
        bot.send_message(message.form_user.id, "You are added to the stack, well done! :)")
        # добавить чувака в стэк

    elif message.text=='Finish':
        bot.send_message(message.from_user.id, "Oh, I didn't expect you to be such a one-minute man!")
        bot.send_message(message.from_user.id, '')


    else:
        bot.send_message(message.from_user.id, "Sorry, i dont understand you.")