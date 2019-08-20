from telegram import KeyboardButton
from telegram import ReplyKeyboardMarkup
from echo.norm_val import val


def get_base_reply_keyboard():
    keyboard = [
        [
            KeyboardButton(val.BUTTON1_STATUS),
            KeyboardButton(val.BUTTON2_INFO),
            KeyboardButton(val.BUTTON3_EDITWET),
        ],
        [
            KeyboardButton(val.BUTTON4_MANUALWATERING),
            KeyboardButton(val.BUTTON5_PHOTO),
        ],
    ]
    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True,
    )