from telegram import Bot
from telegram import Update
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters
from telegram.ext import CallbackQueryHandler

from echo.config import TG_TOKEN
from echo.config import TG_API_URL

from echo.bot_keyboard import BUTTON1_HELP
from echo.bot_keyboard import BUTTON2_TIME
from echo.bot_keyboard import BUTTON3_MYID
from echo.bot_keyboard import get_base_reply_keyboard


# *************************************************

def do_start(bot: Bot, update: Update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text="Send me something...",
        reply_markup=get_base_reply_keyboard(),
    )


def do_echo(bot: Bot, update: Update):
    chat_id = update.message.chat_id
    text = update.message.text

    if text == BUTTON1_HELP:
        answer = "No help today"

    elif text == BUTTON2_TIME:
        answer = "Samoe time"

    elif text == BUTTON3_MYID:
        answer = "Chat id: {}".format(chat_id)

    elif text == "yarik" or text == "Yarik":
        answer = "DAUN!!!"
        print("Yarik has been planted")

    else:
        answer = "Do not understand"

    bot.send_message(
        chat_id=chat_id,
        text=answer,
    )


# *************************************************

def main():
    bot = Bot(
        token=TG_TOKEN,
        base_url=TG_API_URL,
    )
    updater = Updater(
        bot=bot,
    )

    updater.dispatcher.add_handler(CommandHandler("start", do_start))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, do_echo))
    updater.dispatcher.add_handler(CallbackQueryHandler(callback=0))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("Start...")
    main()
