
from telegram import Bot
from telegram import Update
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters
from telegram.ext import CallbackQueryHandler

from echo.config import TG_TOKEN
from echo.config import TG_API_URL

from echo.bot_keyboard import BUTTON1_STATUS
from echo.bot_keyboard import BUTTON2_INFO
from echo.bot_keyboard import BUTTON3_EDITWET
from echo.bot_keyboard import BUTTON4_MANUALWATERING
from echo.bot_keyboard import BUTTON5_PHOTO
from echo.bot_keyboard import get_base_reply_keyboard

# -------------------------------------------------


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

    if text == BUTTON1_STATUS:
        answer = "Starting..."

    elif text == BUTTON2_INFO:
        answer = "Auto watering: {}\n" \
                 "Server time: {}\n" \
                 "Min wet: {}\n" \
                 "Real wet: {}\n" \
                 "Chat ID: {}\n" \
                 "Wait: {}".format("OFF", "UNDEFINED", "50%", "70%", chat_id, "Don`t work")

    elif text == BUTTON3_EDITWET:
        answer = "Old min wet: {}\nEnter new min wet: ".format("50%")

    elif text == BUTTON4_MANUALWATERING:
        #watering...
        answer = "Flower has been watered"

    elif text == BUTTON5_PHOTO:
        #take photo...
        answer = "Here you are!"

    else:
        answer = "Do not understand!"

    bot.send_message(
        chat_id=chat_id,
        text=answer,
    )




"""    elif text == BUTTON3_EDITWET:
        answer = "Old min wet: {}\nEnter new min wet".format("50%")
        wait_wet_val = True

    elif wait_wet_val:
        min_wet = text
        answer = "New min wet: {}".format(text)
        wait_wet_val = False
"""



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
