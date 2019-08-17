from telegram import KeyboardButton
from telegram import ReplyKeyboardMarkup


BUTTON1_STATUS = "OFF"
BUTTON2_INFO = "Info"
BUTTON3_EDITWET = "Edit wet"
BUTTON4_MANUALWATERING = "Manual watering"
BUTTON5_PHOTO = "Photo"


def get_base_reply_keyboard():
    keyboard = [
        [
            KeyboardButton(BUTTON1_STATUS),
            KeyboardButton(BUTTON2_INFO),
            KeyboardButton(BUTTON3_EDITWET),
        ],
        [
            KeyboardButton(BUTTON4_MANUALWATERING),
            KeyboardButton(BUTTON5_PHOTO),
        ],
    ]
    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True,
    )