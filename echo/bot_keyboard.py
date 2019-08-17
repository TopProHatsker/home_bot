from telegram import KeyboardButton
from telegram import ReplyKeyboardMarkup


BUTTON1_HELP = "Help"
BUTTON2_TIME = "Time"
BUTTON3_MYID = "My ID"


def get_base_reply_keyboard():
    keyboard = [
        [
            KeyboardButton(BUTTON1_HELP),
            KeyboardButton(BUTTON2_TIME),
            KeyboardButton(BUTTON3_MYID),
        ],
    ]
    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True,
    )
