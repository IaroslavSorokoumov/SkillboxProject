from telebot.types import Message

from structure_example.config_data.config import DEFAULT_COMMANDS
from structure_example.loader import bot


@bot.message_handler(commands=["help"])
def bot_help(message: Message):
    text = [f"/{command} - {desk}" for command, desk in DEFAULT_COMMANDS]
    bot.reply_to(message, "\n".join(text))
