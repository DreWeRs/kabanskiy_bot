from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from emoji import emojize


def get_menu_keyboard():
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text='Все серии', callback_data='all_series')
    )

    builder.row(
        InlineKeyboardButton(text=f'Галерея{emojize(":framed_picture:")}',
                             callback_data='all_photo'),
        InlineKeyboardButton(
            text=f'Над сериалом работали{emojize(":construction_worker:")}',
            callback_data='all_actor')
    )

    builder.row(
        InlineKeyboardButton(text=f'GitHub{emojize(":man_technologist:")}',
                             callback_data='github')
    )

    builder.row(
        InlineKeyboardButton(text='Что дальше?', callback_data='next')
    )

    return builder.as_markup()
