
from telebot import TeleBot
from structure_example.config_data.config import BOT_TOKEN

bot = TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(m):
    bot.reply_to(m, f'Hello {m.from_user.first_name}!')

@bot.message_handler(func=lambda m: True)
def echo_all(m):
    bot.reply_to(m, m.text)

if __name__ == '__main__':
    bot.infinity_polling()

