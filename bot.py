import random
from telebot import TeleBot


TELEGRAM_TOKEN = ''


bot = TeleBot(TELEGRAM_TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, 'Вас приветствует пиццерия ТоктосунПицца!')


def reply_to_standard_message(message):
    msg_text = message.text.lower()
    if msg_text in ('привет', 'салам', 'hello', 'hi'):
        response_msg = random.choice(['И вам привет!', 'салам!'])
        bot.reply_to(message, response_msg)
    elif msg_text in ('пока', 'до свидания'):
        bot.reply_to(message, 'Прощайте')
    elif msg_text in ('спасибо', 'благодарю'):
        bot.reply_to(message, 'Вам спасибо.')



bot.infinity_polling()
