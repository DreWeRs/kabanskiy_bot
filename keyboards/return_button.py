from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_return_button():
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text='Вернуться', callback_data='back'))
    return builder.as_markup()
