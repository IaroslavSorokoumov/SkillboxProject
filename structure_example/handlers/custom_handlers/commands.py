from peewee import IntegrityError

from structure_example.database.models import User
from telebot.types import Message
from structure_example.loader import bot
@bot.message_handler(commands=['start'])
def handle_start(m: Message) -> None:
    user_id = m.from_user.id
    username = m.from_user.username
    first_name = m.from_user.first_name
    last_name = m.from_user.last_name

    try:
        User.create(
            user_id=user_id,
            username=username,
            first_name=first_name,
            last_name=last_name,
        )
        bot.reply_to(m,'Добро пожаловать в менеджер задач!')
    except IntegrityError:
        bot.reply_to(m, f"Рад вас снова видеть, {first_name}")