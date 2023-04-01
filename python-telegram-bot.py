import os # to read the environment variables stored in our system

import telebot

BOT_TOKEN = os.environ.get('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)

# We then need to register message handlers. These message handlers contain filters that a message must pass.
# If a message passes the filter, the decorated function is called and the incoming message is supplied as an argument.
#This is a message handler that handles incoming /start and /hello commands

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

# Any name is acceptable for a function that is decorated by a message handler, but it can only have one parameter (the message).
# Let’s add another handler that echoes all incoming text messages back to the sender.
# The code below uses a lambda expression to test a message.
# Since we need to echo all the messages, we always return True from the lambda function

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()