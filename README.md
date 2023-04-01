# telegram-bot
This is a simple implementation of a Telegram bot to show concepts and how to use it. 

A bot is a software application programmed to perform certain tasks. Bots often mimic or replace the behaviour of a human user. 

## Get the API
Before starting to code, we need a Telegram Bot API. 
1) Create an account on telegram.
2) Search for BotFather: it is an official telegram bot that provides API to create more bots. 
3) When you reach the BotFather, open the Telegram chat, just write: /start and send. 
4) The BatFather will reply you with a long text, without reading the text you can type /newbot, and click on reply. 
5) Then, BotFather will reply again with a long text, asking about a good name for your Telegram bot. You can write any name on it.
6) Next step is to give a username to your bot. It should be in a format Namebot or Name_bot. Important thing to notice is that your username should be an unique one, it should not match any other username all around the world.
7) Now after typing an unique username, it will send you an API key between a long message, you need to copy that username and get started with Python.

# Token
create a file with a .env extension that will store the token providede by the BotFather. Like this: 
export BOT_TOKEN=your-bot-token-here. 
After that, run the source .env command to read the environment variables from the .env file
## Dependencies
pip install pyTelegramBotAPI
