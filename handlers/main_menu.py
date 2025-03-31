
from aiogram import F, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import FSInputFile, Message
from aiogram.utils.media_group import MediaGroupBuilder

from keyboards.menu_keyboard import get_menu_keyboard
from keyboards.return_button import get_return_button
from keyboards.series_keyboard import get_series_keyboard

router = Router()


@router.message(Command('start'))
async def welcome_message(message: Message):
    await message.answer(
        text='Приветствую тебя! Это фанатский бот легендарного сериала Кабан, '
             'создан BukingemCo',
        reply_markup=get_menu_keyboard()
    )


@router.callback_query(F.data == 'all_series')
async def get_all_series(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(
        text='Список всех серий сериала Кабан:',
        reply_markup=get_series_keyboard()
    )


@router.callback_query(F.data == 'all_photo')
async def get_all_photo(callback: types.CallbackQuery):
    album = MediaGroupBuilder()
    album.add_photo(media=FSInputFile('assets/photo_bandito.jpg'))
    album.add_photo(media=FSInputFile('assets/photo_povar.jpg'))
    album.add_photo(media=FSInputFile('assets/photo_phone_breaker.jpg'))

    await callback.message.delete()
    await callback.message.answer_media_group(media=album.build())
    await callback.message.answer(
        'Вернуться в меню',
        reply_markup=get_return_button()
    )


@router.callback_query(F.data == 'back')
async def back_to_menu(callback: types.CallbackQuery):
    await callback.message.delete()
    await callback.message.answer(
        text='Приветствую тебя! Это тестовый бот легендарного сериала Кабан,'
             'создан BukingemCo',
        reply_markup=get_menu_keyboard()
    )


@router.callback_query(F.data == 'all_actor')
async def get_all_actor(callback: types.CallbackQuery):
    text = '''Над сериалом работало огромное количество людей:
<b>Тигран</b> - режиссер, сценарист, оператор и какой-то там англичанин
<b>Илья</b> - главный герой (кабан)
<b>Мирон</b> - инвестор и программист
<b>Артур</b> - главарь бандитов
<b>Дима</b> и <b>Яков</b> - его подчиненные
<b>Слава</b> - комик вроде
<b>Давид</b> - шоумен
<b>И массовка</b>.'''
    await callback.message.answer(text=text,
                                  parse_mode=ParseMode.HTML,
                                  reply_markup=get_return_button()
                                  )
