import telegram
bot = telegram.bot(token='TOKEN') #Replace TOKEN with your token string
from telegram.ext import Updater, CommandHandler, MessageHandler

#Updater: class telegram.ext.Updater(bot, update_queue)[source]
# fetches updates for the bot either via long polling or by starting a webhook server. 
# update_queue: Received updates are enqueued into the update_queue and
# may be fetched from there to handle them appropriately.

#CommandHandler: class telegram.ext.CommandHandler(command, callback, filters=None, block=True)
# BaseHandler class to handle Telegram commands.
# Commands are Telegram messages that start with /, optionally followed by an @ and the bot’s
# name and/or some additional text. The handler will add a list to the CallbackContext 
# named CallbackContext.args. It will contain a list of strings, which is the text
# following the command split on single or consecutive whitespace characters

#MessageHandler: class telegram.ext.MessageHandler(filters, callback, block=True)
#aseHandler class to handle Telegram messages. They might contain text, media or status updates.
updater = Updater(bot, use_context=True) #Replace TOKEN with your token string
dispatcher = updater.dispatcher

def hello(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text='Hello, World')

hello_handler = CommandHandler('hello', hello)
dispatcher.add_handler(hello_handler)

updater.start_polling()