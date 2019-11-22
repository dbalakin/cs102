import telebot
from telebot import apihelper

access_token = '965696888:AAGfuxg8heeJBX0MqU18fte8Bvtvsw8-cTQ'
apihelper.proxy = {'https':'http://78.41.53.39:8080'}

# Создание бота с указанным токеном доступа
bot = telebot.TeleBot(access_token)


# Бот будет отвечать только на текстовые сообщения
@bot.message_handler(content_types=['text'])
def echo(message: str) -> None:
    bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    bot.polling()


