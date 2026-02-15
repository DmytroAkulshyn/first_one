from pyrogram import Client, filters
import config
import keyboards
from pyrogram import emoji
import random
import json
from FusionBrain_AI import generate
import base64
from pyrogram.types import ForceReply
import datetime

date_time = datetime.datetime.now()
list = ["Камень", "Ножницы", "Бумага"]
def button_filter(button):
    async def func(_, __, msg):
        return msg.text == button.text

    return filters.create(func, "ButtonFilter", button=button)


bot = Client(
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN,
    name="Купаты"
)


@bot.on_message(filters.command("start"))
async def start(bot, message):
    await message.reply("Добро пожаловать",
                        reply_markup=keyboards.kb_main)
    await bot.send_photo(message.chat.id, "https://upload.wikimedia.org/wikipedia/commons/7/74/A-Cat.jpg")
    with open('users.json', 'r') as file:
        users = json.load(file)
    if str(message.from_user.id) not in users.keys():
        users[message.from_user.id] = 100
        with open('users.json', 'w') as file:
            json.dump(users, file)

@bot.on_message(filters.command("games") | button_filter(keyboards.btn_games))
async def games(bot, message):
        await message.reply('Вот игры', reply_markup=keyboards.km_main)


@bot.on_message(filters.command("back") | button_filter(keyboards.btn_back))
async def back(bot, message):
        await message.reply("Добро пожаловать",
                        reply_markup=keyboards.kb_main)

@bot.on_message(filters.command("rps") | button_filter(keyboards.btn_rps))
async def rps(bot, message):
        await message.reply('Давай сыграем', reply_markup=keyboards.kk_main)
        with open('users.json', 'r') as file:
            users = json.load(file)
        if users[str(message.from_user.id)] >= 10:
            await message.reply('Твой ход', reply_markup=keyboards.kk_main)
        elif users[str(message.from_user.id)] < 10:
            await message.reply(f"Не хватает средств. На твоем счету {users[str(message.from_user.id)]}. Минимельная сумма для игры - 10")
            await message.reply('Вы не можете пользоваться этой функцией', reply_markup=keyboards.kb_main)
@bot.on_message(button_filter(keyboards.btn_rock) |
                button_filter(keyboards.btn_sci) |
                button_filter(keyboards.btn_paper))
async def choice_rps(bot, message):
    with open('users.json', 'r') as file:
        users = json.load(file)


    rock = keyboards.btn_rock.text
    scissors = keyboards.btn_sci.text
    paper = keyboards.btn_paper.text
    user = message.text
    pc = random.choice([rock, scissors, paper])
    if user == pc:
        await message.reply('Ничья')
    elif (user == rock and pc == scissors) or (user == scissors and pc == paper) or (user == paper and pc == rock):
        await message.reply(f'Ты выиграл, бот выбрал {pc}', reply_markup=keyboards.km_main)
        #users[str(message.from_user.id)] += 10
    else:
        await message.reply(f'Ты проиграл, бот выбрал {pc}', reply_markup=keyboards.km_main)
        await bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEPhjFo4uxctPXcAvRqIuvMlnTSdVWv8wACL0oAApYyiUsgpwABEpkt__E2BA')
        users[str(message.from_user.id)] -= 10

    with open('users.json', 'w') as file:
        json.dump(users, file)

@bot.on_message(filters.command('info') | button_filter(keyboards.btn_info))
async def info(bot, message):
    await message.reply('Привет! Тут описание что может этот бот и список команд:\n/games /info /rps /profile /time')

@bot.on_message(filters.command('quest') | button_filter(keyboards.btn_quest))
async def kvest(bot, message):
    await message.reply_text('Хотите ли вы отправиться в увликательное путешествия?',
                             reply_markup=keyboards.inline_kb_start_quest)
@bot.on_callback_query()
async def handle_query(bot, query):
    if query.data == 'start_quest':
        await bot.answer_callback_query(query.id,
                                        text="Добро пожаловать в квест под названием Поиски Затерянного Сокровища",
                                        show_alert=True)

        await query.message.reply_text('Ты стоишь перед двумя дверьми. Какую из них выберешь',
                                       reply_markup=keyboards.inline_kb_choice_door)
    elif query.data == "left_door":
        await query.message.reply_text('Ты входишь в комнату и видишь злого дракона! У тебя есть два варианта действий:',
                                       reply_markup=keyboards.inline_kb_left_door)

    elif query.data == "right_door":
        await query.message.reply_text('Ты входишь в комнату наполненую сокровищами! Но тебе нужно взять лишь одно сокровище:',
                                       reply_markup=keyboards.inline_kb_right_door)
    elif query.data == 'dragon':
        await bot.answer_callback_query(query.id,
                                        text="Ты слишком сильно поверил в себя",
                                        show_alert=True)
        await query.message.reply_text('Твой квест окончен', reply_markup=keyboards.kb_main)
    elif query.data == 'run':
        await bot.answer_callback_query(query.id,
                                        text="Ты убежал но ничего не забрал",
                                        show_alert=True)
        await query.message.reply_text('Твой квест окончен', reply_markup=keyboards.kb_main)
    elif query.data == 'gold_crown':
        await query.message.reply_text('Ты взял корону, что дальше?', reply_markup=keyboards.inline_kb_gold_crown)


    elif query.data == 'silver_dagger':
        await query.message.reply_text('Ты взял кинжал, что дальше?', reply_markup=keyboards.inline_kb_silver_dagger)


    elif query.data == 'old_book':
        await query.message.reply_text('Ты взял книгу, что дальше?', reply_markup=keyboards.inline_kb_old_book)


    elif query.data == 'left2_door':
        await bot.answer_callback_query(query.id,
                                        text="Перед тобой дракон что ты будешь делать? У тебя есть корона",
                                        show_alert=True)
        await query.message.reply_text('Выбирай дальше', reply_markup=keyboards.inline_kb_left2_door)

    elif query.data == 'run2':
        await bot.answer_callback_query(query.id,
                                        text="Теперь то ты сможешь хоть как то зароботать",
                                        show_alert=True)
        await query.message.reply_text('Твой квест окончен', reply_markup=keyboards.kb_main)

    elif query.data == 'left3_door':
        await bot.answer_callback_query(query.id,
                                        text="Перед тобой дракон что ты будешь делать? У тебя есть кинжал",
                                        show_alert=True)
        await query.message.reply_text('Выбирай следующее дейсвие', reply_markup=keyboards.inline_kb_left3_door)

    elif query.data == 'run3':
        await bot.answer_callback_query(query.id,
                                        text="Теперь ты можешь кого то пырнуть",
                                        show_alert=True)
        await query.message.reply_text('Твой квест окончен', reply_markup=keyboards.kb_main)

    elif query.data == 'left4_door':
        await bot.answer_callback_query(query.id,
                                        text="Перед тобой дракон что ты будешь делать? У тебя есть книга",
                                        show_alert=True)
        await query.message.reply_text('Твой квест окончен', reply_markup=keyboards.inline_kb_left4_door)

    elif query.data == 'run4':
        await bot.answer_callback_query(query.id,
                                        text="Ну учись",
                                        show_alert=True)

        await query.message.reply_text('Твой квест окончен', reply_markup=keyboards.kb_main)
    elif query.data == 'run5':
        await bot.answer_callback_query(query.id,
                                        text="Ты мог продолжить квест но ты решил остаться с короной",
                                        show_alert=True)
        await query.message.reply_text('Твой квест окончен', reply_markup=keyboards.kb_main)

    elif query.data == 'run6':
        await bot.answer_callback_query(query.id,
                                        text="Ты мог продолжить квест но ты решил пойти и пырнуть кого то другого ",
                                        show_alert=True)
        await query.message.reply_text('Твой квест окончен', reply_markup=keyboards.kb_main)

    elif query.data == 'run7':
        await bot.answer_callback_query(query.id,
                                        text="Ну учись",
                                        show_alert=True)
        await query.message.reply_text('Твой квест окончен', reply_markup=keyboards.kb_main)

    elif query.data == 'dragon2':
        await bot.answer_callback_query(query.id,
                                        text="Не знаю на что ты надеялся когда с короной пытаешься победить дракона",
                                        show_alert=True)
        await query.message.reply_text('Твой квест окончен', reply_markup=keyboards.kb_main)

    elif query.data == 'dragon3':
        await bot.answer_callback_query(query.id,
                                        text="Молодец ты смог победить дракона",
                                        show_alert=True)
        await query.message.reply_text('Твой квест окончен', reply_markup=keyboards.kb_main)

    elif query.data == 'dragon4':
        await bot.answer_callback_query(query.id,
                                        text="Не, кинув книгу ты не победишь дракона",
                                        show_alert=True)
        await query.message.reply_text('Твой квест окончен', reply_markup=keyboards.kb_main)

@bot.on_message(filters.command('image'))
async def image(bot, message):
    if len(message.text.split()) > 1:
        query = message.text.replace('/images', '')
        await message.reply_text(f'Генерирую изображение по запросу {query}, подождите немного')
        images = await generate(query)
        if images:
            image_data = base64.b64decode(images[0])
            img_num = random.randint(1, 99)
            with open(f'images/image{img_num}.jpg', 'wb') as file:
                file.write(image_data)
            await bot.send_photo(message.chat.id, f'images/image{img_num}.jpg',
                                 reply_to_message_id=message.id, reply_markup=keyboards.kb_main)
        else:
            await message.reply_text('Ошибка попробуй еще раз',
                                     reply_to_message_id=message.id, reply_markup=keyboards.kb_main)
    else:
        await message.reply_text('Введите запрос')

query_text = 'Введите запрос для генерации изображения'
@bot.on_message(button_filter(keyboards.btn_image))
async def image_command(bot, message):
    await message.reply(query_text, reply_markup=ForceReply(True))

@bot.on_message(filters.reply)
async def reply(bot, message):
    if message.reply_to_message.text == query_text:
        query = message.text
        await message.reply_text(f'Генерирую изображение по запросу {query}')
        images = await generate(query)
        if images:
            image_data = base64.b64decode(images[0])
            img_num = random.randint(1, 99)
            with open(f'images/image{img_num}.jpg', 'wb') as file:
                file.write(image_data)
            await bot.send_photo(message.chat.id, f'images/image{img_num}.jpg',
                                 reply_to_message_id=message.id, reply_markup=keyboards.kb_main)
        else:
            await message.reply_text('Ошибка попробуй еще раз',
                                     reply_to_message_id=message.id, reply_markup=keyboards.kb_main)
    else:
        await message.reply_text('Введите запрос')

@bot.on_message(filters.command('profile') | button_filter(keyboards.btn_profile))
async def profile(bot, message):
    with open('users.json', 'r') as file:
        users = json.load(file)
        await bot.send_message(
            chat_id=message.chat.id,
            text=f'<b>ID:</b> {message.from_user.id}\n<b>Деньги:<b/> {users[str(message.from_user.id)]}\n'
        )
@bot.on_message(filters.command('time') | button_filter(keyboards.btn_time))
async def time(bot, message):
    await message.reply(f'Текущие дата и время: {datetime.datetime.now()}')
bot.run()
