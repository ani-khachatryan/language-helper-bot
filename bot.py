import telebot
from words import get_synonyms, get_antonyms
from translation import translate, check_if_lang


token = '5388837562:AAF6kY4Smd2X4n4B6zmrSowoWtewRVAsrTI'
bot = telebot.TeleBot(token)
users = {}


@bot.message_handler(commands=['start'])
def start(message):
    users[message.from_user.id] = 'en'
    bot.reply_to(message, 'Welcome to language helper bot!')

@bot.message_handler(commands=['syn'])
def synonyms(message):
    if len(message.text) == 4:
        bot.reply_to(message, 'Please specify the word after command /syn')
        return
    bot.reply_to(message, get_synonyms(message.text[4:].strip()))

@bot.message_handler(commands=['ant'])
def antonyms(message):
    if len(message.text) == 4:
        bot.reply_to(message, 'Please specify the word after command /ant')
        return
    bot.reply_to(message, get_antonyms(message.text[4:].strip()))


@bot.message_handler(commands=['set_lang'])
def change_lang(message):
    if len(message.text) == 9:
        bot.reply_to(message, 'Please specify the language after command /set_lang')
        return
    lang = check_if_lang(message.text[9:].strip().lower())
    if (lang != False):
        users[message.from_user.id] = lang
        bot.reply_to(message, f'Language successfully changed to {lang}')
    else:
        bot.reply_to(message, f'Error: unable to find the specified language')

@bot.message_handler(content_types = ['text'])
def translate_message(message):
    bot.reply_to(message, translate(message.text, dest_lang = users[message.from_user.id]))
    translate(message.text)

bot.infinity_polling()
