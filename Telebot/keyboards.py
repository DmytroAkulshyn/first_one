from pyrogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton,InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import emoji

btn_image = KeyboardButton(f'{emoji.FRAMED_PICTURE} Сгенерировать изображение')
btn_info = KeyboardButton(f"{emoji.INFORMATION} Инфо")
btn_games = KeyboardButton(f"{emoji.VIDEO_GAME} Игры")
btn_profile = KeyboardButton(f"{emoji.PERSON} Профиль")
btn_time = KeyboardButton(f"{emoji.TIMER_CLOCK} Время")

kb_main = ReplyKeyboardMarkup(
    keyboard=[
        [btn_info, btn_games, btn_profile],
        [btn_image],
        [btn_time]
    ],
    resize_keyboard=True
)

btn_rps = KeyboardButton('Камень Ножницы Бумага')
btn_quest = KeyboardButton('Квест')
btn_back = KeyboardButton('Назад')

km_main = ReplyKeyboardMarkup(
    keyboard=[
        [btn_rps],
        [btn_quest,btn_back]
    ],
    resize_keyboard=True
)


btn_rock = KeyboardButton('Камень')
btn_paper = KeyboardButton('Бумага')
btn_sci = KeyboardButton('Ножницы')
btn_back  = KeyboardButton('Назад')

kk_main = ReplyKeyboardMarkup(
    keyboard=[
        [btn_rock, btn_paper, btn_sci],
        [btn_back]
    ],
    resize_keyboard=True
)

inline_kb_start_quest = InlineKeyboardMarkup([
    [InlineKeyboardButton('Пройти квест',
                          callback_data="start_quest")]
])

inline_kb_choice_door = InlineKeyboardMarkup([
    [InlineKeyboardButton('<--- Левая дверь', callback_data='left_door')],
    [InlineKeyboardButton('Правая дверь --->', callback_data='right_door')]
])

inline_kb_left_door = InlineKeyboardMarkup([
    [InlineKeyboardButton('Сражаться с драконом', callback_data='dragon')],
    [InlineKeyboardButton('Попытаться убежать', callback_data='run')]
])

inline_kb_right_door = InlineKeyboardMarkup([
    [InlineKeyboardButton('Золотая корона', callback_data='gold_crown')],
    [InlineKeyboardButton('Серебряный кинжал', callback_data='silver_dagger')],
    [InlineKeyboardButton('Старая книга', callback_data='old_book')]

])

inline_kb_gold_crown = InlineKeyboardMarkup([
    [InlineKeyboardButton('Пойти в левую дверь', callback_data='left2_door')],
    [InlineKeyboardButton('Убежать из замка', callback_data='run2')]

])

inline_kb_silver_dagger = InlineKeyboardMarkup([
    [InlineKeyboardButton('Пойти в левую дверь', callback_data='left3_door')],
    [InlineKeyboardButton('Убежать из замка', callback_data='run3')]

])

inline_kb_old_book = InlineKeyboardMarkup([
    [InlineKeyboardButton('Пойти в левую дверь', callback_data='left4_door')],
    [InlineKeyboardButton('Убежать из замка', callback_data='run4')]

])

inline_kb_left2_door = InlineKeyboardMarkup([
    [InlineKeyboardButton('Сражаться с драконом используя корону', callback_data='dragon2')],
    [InlineKeyboardButton('Попытаться убежать', callback_data='run5')]

])

inline_kb_left3_door = InlineKeyboardMarkup([
    [InlineKeyboardButton('Сражаться с драконом используя кинжал', callback_data='dragon3')],
    [InlineKeyboardButton('Попытаться убежать', callback_data='run6')]

])

inline_kb_left4_door = InlineKeyboardMarkup([
    [InlineKeyboardButton('Сражаться с драконом используя старую книгу', callback_data='dragon4')],
    [InlineKeyboardButton('Попытаться убежать', callback_data='run7')]

])