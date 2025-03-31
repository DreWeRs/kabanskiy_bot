from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_series_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.add(
        InlineKeyboardButton(text='Серия 1', url='https://www.youtube.com/watch?v=Y5BbSKrJxY4'),
        InlineKeyboardButton(text='Серия 2', url='https://www.youtube.com/watch?v=ZDIjdJywfxQ'),
        InlineKeyboardButton(text='Серия 3', url='https://www.youtube.com/watch?v=dRSrJ-qP0ik'),
        InlineKeyboardButton(text='Серия 4', url='https://www.youtube.com/watch?v=maVei5gW0ms'),
        InlineKeyboardButton(text='Серия 5', url='https://www.youtube.com/watch?v=kSvOkMxXCo4&pp=0gcJCXcA-SJGOe9V')
    )
    builder.adjust(2)
    builder.row(InlineKeyboardButton(text='Вернуться', callback_data='back'))
    return builder.as_markup()
