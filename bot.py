import random
from telebot import TeleBot
from generate_data import generate_pizzas


TELEGRAM_TOKEN = ''


bot = TeleBot(TELEGRAM_TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, 'Вас приветствует пиццерия ТоктосунПицца!')


@bot.message_handler(commands=['menu'])
def show_menu(message):
    menu_str = 'Наше меню\n'
    our_pizza_list = generate_pizzas()
    for pizza in our_pizza_list:
        name_price = pizza.get_name_with_price()
        menu_str += f'{name_price}\n'
    bot.reply_to(message, menu_str)


@bot.message_handler(content_types='text')
def reply_to_standard_message(message):
    msg_text = message.text.lower()
    if msg_text in ['привет', 'салам', 'hello', 'hi']:
        response_msg = random.choice(['И вам привет!', 'салам!'])
        bot.reply_to(message, response_msg)
    elif msg_text in ('пока', 'до свидания'):
        bot.reply_to(message, 'Прощайте')
    elif msg_text in ('спасибо', 'благодарю'):
        bot.reply_to(message, 'Вам спасибо.')
    else:
        bot.reply_to(message, 'Я пока не могу на это ответить.')


bot.infinity_polling()

# ДЗ:
# 1. Написать команду /combo который рекомендует одну рандомную пиццу
# и один рандомный напиток.
# 2. Пользоватль вводит название пиццы или напитка, вы находите данный продукт и
# выводите пользователю всю доступную информацию о ней.
