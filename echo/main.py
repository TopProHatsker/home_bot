
from subprocess import Popen
from subprocess import PIPE

from telegram import Bot
from telegram import Update
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters

from echo.config import TG_TOKEN
from echo.config import TG_API_URL


# *************************************************

def do_start(bot: Bot, update: Update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text="Send me something...",
    )


def do_help(bot: Bot, update: Update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text="HELP",
    )


def do_time(bot: Bot, update: Update):
    process = Popen(["date"], stdout=PIPE)
    text, error = process.communicate()
    print("client_get_time")
    if error:
        text = "undefined"
    else:
        text = text.decode("utf-8")

    bot.send_message(
        chat_id=update.message.chat_id,
        text=text,
    )


def do_echo(bot: Bot, update: Update):
    chat_id = update.message.chat_id
    text = "Chat id: {}\n\n{}".format(chat_id, update.message.text)
    if text == "yarik" or text == "Yarik":
        text = "DAUN!!!"
        print("Yarik has been planted")

    bot.send_message(
        chat_id=chat_id,
        text=text,
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
    updater.dispatcher.add_handler(CommandHandler("help", do_help))
    updater.dispatcher.add_handler(CommandHandler("time", do_time))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, do_echo))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    print("Start")
    main()
