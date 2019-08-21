
from RP3.Example import RaspberryPi3B

from telegram import Bot
from telegram import Update
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters
from telegram.ext import CallbackQueryHandler

from echo.config import TG_TOKEN
from echo.config import TG_API_URL
from echo.config import RPI_PUMP_PIN
from echo.config import RPI_WET_PIN
from echo.config import RPI_MIN_WET
"""
from echo.bot_keyboard import BUTTON1_STATUS
from echo.bot_keyboard import BUTTON2_INFO
from echo.bot_keyboard import BUTTON3_EDITWET
from echo.bot_keyboard import BUTTON4_MANUALWATERING
from echo.bot_keyboard import BUTTON5_PHOTO
"""
from echo.norm_val import val
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
    print(str(chat_id)+" --> "+text)

    if text == val.BUTTON1_STATUS:
        if rpi.AutoMode:
            answer = "Stoping..."
            rpi.AutoMode = False
            val.BUTTON1_STATUS = "Auto: OFF"

        else:
            answer = "Starting..."
            rpi.AutoMode = True
            val.BUTTON1_STATUS = "Auto: ON"

    elif text == val.BUTTON2_INFO:
        result = rpi.get_info()
        answer = "Auto watering: {}\n" \
                 "Min wet: {}\n" \
                 "Real wet: {}\n" \
                 "Server time: {}\n" \
                 "Chat ID: {}".format(result[0], result[1], result[2], "UNDEFINED", chat_id)

    elif text == val.BUTTON3_EDITWET:
        answer = "Old min wet: {}%\nEnter new min wet: ".format(rpi.MinWet)
        val.wait_num = 1

    elif val.wait_num == 1:
        rpi.MinWet = text
        answer = "New min wet: {}".format(text)
        val.BUTTON3_EDITWET = "Wet: " + rpi.MinWet + "%"
        val.wait_num = 0

    elif text == val.BUTTON4_MANUALWATERING:
        rpi.manual_watering()
        answer = "Flower has been watered"

    elif text == val.BUTTON5_PHOTO:
        rpi.take_photo()
        answer = "Here you are!"

    else:
        answer = "Do not understand!"


    bot.send_message(
        chat_id=chat_id,
        text=answer,
        reply_markup=get_base_reply_keyboard(),
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
    rpi = RaspberryPi3B(RPI_PUMP_PIN, RPI_WET_PIN, RPI_MIN_WET)
    main()



"""try:

    if __name__ == '__main__':
        print("Start...")
        rpi = RaspberryPi3B(RPI_PUMP_PIN, RPI_WET_PIN, RPI_MIN_WET)
        main()

except KeyboardInterrupt:
    print("Exit pressed Ctrl+C")  # Выход из программы по нажатию Ctrl+C
except:
    print("Other Exception")  # Прочие исключения
finally:
    # GPIO.cleanup()                      # Возвращаем пины в исходное состояние
    print("End of program")  # Информируем о завершении работы программы"""
