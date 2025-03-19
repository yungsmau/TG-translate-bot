import telebot
import os
from telebot import types
from googletrans import Translator
from dotenv import load_dotenv

import languages
import buttons


load_dotenv()
token = os.getenv("TELEGRAM_BOT_TOKEN")

bot = telebot.TeleBot(token)

current_language = "en"


# googletrans
def result_info(words, langs):
    result = Translator().translate(words, langs)
    text = {}
    text[1] = result.origin
    text[2] = result.text

    return text


# new starter message
@bot.message_handler(commands=["start"])
def start_message(message):
    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(
        "Выбрать язык", callback_data="change_language"
    )
    keyboard.add(button1)
    bot.send_message(message.chat.id, "Привет!\nГотов переводить.")


# buttons for languages
# each call has a designated page with languages
@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    if call.data == "change_language":
        keyboard = types.InlineKeyboardMarkup()

        page_btn_1 = types.InlineKeyboardButton(".", callback_data=("ignore"))
        page_btn_2 = types.InlineKeyboardButton("2", callback_data=("2"))
        page_btn_3 = types.InlineKeyboardButton("3", callback_data=("3"))
        page_btn_4 = types.InlineKeyboardButton("4", callback_data=("4"))
        page_btn_5 = types.InlineKeyboardButton("5", callback_data=("5"))
        page_btn_6 = types.InlineKeyboardButton("6", callback_data=("6"))

        btns = buttons.create_buttons(1)
        list = []

        for elem in btns[0]:
            list.append(elem)

        x = 0
        for i in range(6):
            keyboard.row(list[x], list[x + 1], list[x + 2])
            x += 3

        keyboard.row(
            page_btn_1, page_btn_2, page_btn_3, page_btn_4, page_btn_5, page_btn_6
        )

        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="Выберите язык:",
            reply_markup=keyboard,
        )

    elif call.data == "1":
        keyboard1 = types.InlineKeyboardMarkup()

        page_btn_1 = types.InlineKeyboardButton(".", callback_data=("ignore"))
        page_btn_2 = types.InlineKeyboardButton("2", callback_data=("2"))
        page_btn_3 = types.InlineKeyboardButton("3", callback_data=("3"))
        page_btn_4 = types.InlineKeyboardButton("4", callback_data=("4"))
        page_btn_5 = types.InlineKeyboardButton("5", callback_data=("5"))
        page_btn_6 = types.InlineKeyboardButton("6", callback_data=("6"))

        btns = buttons.create_buttons(1)
        list = []

        for elem in btns[0]:
            list.append(elem)

        x = 0
        for i in range(6):
            keyboard1.row(list[x], list[x + 1], list[x + 2])
            x += 3

        keyboard1.row(
            page_btn_1, page_btn_2, page_btn_3, page_btn_4, page_btn_5, page_btn_6
        )

        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="Выберите язык:",
            reply_markup=keyboard1,
        )

    elif call.data == "2":
        keyboard2 = types.InlineKeyboardMarkup()

        page_btn_1 = types.InlineKeyboardButton("1", callback_data=("1"))
        page_btn_2 = types.InlineKeyboardButton(".", callback_data=("ignore"))
        page_btn_3 = types.InlineKeyboardButton("3", callback_data=("3"))
        page_btn_4 = types.InlineKeyboardButton("4", callback_data=("4"))
        page_btn_5 = types.InlineKeyboardButton("5", callback_data=("5"))
        page_btn_6 = types.InlineKeyboardButton("6", callback_data=("6"))

        btns = buttons.create_buttons(2)
        list = []

        for elem in btns[0]:
            list.append(elem)

        x = 0
        for i in range(6):
            keyboard2.row(list[x], list[x + 1], list[x + 2])
            x += 3

        keyboard2.row(
            page_btn_1, page_btn_2, page_btn_3, page_btn_4, page_btn_5, page_btn_6
        )

        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="Выберите язык:",
            reply_markup=keyboard2,
        )

    elif call.data == "3":
        keyboard3 = types.InlineKeyboardMarkup()

        page_btn_1 = types.InlineKeyboardButton("1", callback_data=("1"))
        page_btn_2 = types.InlineKeyboardButton("2", callback_data=("2"))
        page_btn_3 = types.InlineKeyboardButton(".", callback_data=("ignore"))
        page_btn_4 = types.InlineKeyboardButton("4", callback_data=("4"))
        page_btn_5 = types.InlineKeyboardButton("5", callback_data=("5"))
        page_btn_6 = types.InlineKeyboardButton("6", callback_data=("6"))

        btns = buttons.create_buttons(3)
        list = []

        for elem in btns[0]:
            list.append(elem)

        x = 0
        for i in range(6):
            keyboard3.row(list[x], list[x + 1], list[x + 2])
            x += 3

        keyboard3.row(
            page_btn_1, page_btn_2, page_btn_3, page_btn_4, page_btn_5, page_btn_6
        )

        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="Выберите язык:",
            reply_markup=keyboard3,
        )

    elif call.data == "4":
        keyboard4 = types.InlineKeyboardMarkup()

        page_btn_1 = types.InlineKeyboardButton("1", callback_data=("1"))
        page_btn_2 = types.InlineKeyboardButton("2", callback_data=("2"))
        page_btn_3 = types.InlineKeyboardButton("3", callback_data=("3"))
        page_btn_4 = types.InlineKeyboardButton(".", callback_data=("ignore"))
        page_btn_5 = types.InlineKeyboardButton("5", callback_data=("5"))
        page_btn_6 = types.InlineKeyboardButton("6", callback_data=("6"))

        btns = buttons.create_buttons(4)
        list = []

        for elem in btns[0]:
            list.append(elem)

        x = 0
        for i in range(6):
            keyboard4.row(list[x], list[x + 1], list[x + 2])
            x += 3

        keyboard4.row(
            page_btn_1, page_btn_2, page_btn_3, page_btn_4, page_btn_5, page_btn_6
        )

        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="Выберите язык:",
            reply_markup=keyboard4,
        )

    elif call.data == "5":
        keyboard5 = types.InlineKeyboardMarkup()

        page_btn_1 = types.InlineKeyboardButton("1", callback_data=("1"))
        page_btn_2 = types.InlineKeyboardButton("2", callback_data=("2"))
        page_btn_3 = types.InlineKeyboardButton("3", callback_data=("3"))
        page_btn_4 = types.InlineKeyboardButton("4", callback_data=("4"))
        page_btn_5 = types.InlineKeyboardButton(".", callback_data=("ignore"))
        page_btn_6 = types.InlineKeyboardButton("6", callback_data=("6"))

        btns = buttons.create_buttons(5)
        list = []

        for elem in btns[0]:
            list.append(elem)

        x = 0
        for i in range(6):
            keyboard5.row(list[x], list[x + 1], list[x + 2])
            x += 3

        keyboard5.row(
            page_btn_1, page_btn_2, page_btn_3, page_btn_4, page_btn_5, page_btn_6
        )

        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="Выберите язык:",
            reply_markup=keyboard5,
        )

    elif call.data == "6":
        keyboard6 = types.InlineKeyboardMarkup()

        page_btn_1 = types.InlineKeyboardButton("1", callback_data=("1"))
        page_btn_2 = types.InlineKeyboardButton("2", callback_data=("2"))
        page_btn_3 = types.InlineKeyboardButton("3", callback_data=("3"))
        page_btn_4 = types.InlineKeyboardButton("4", callback_data=("4"))
        page_btn_5 = types.InlineKeyboardButton("5", callback_data=("5"))
        page_btn_6 = types.InlineKeyboardButton(".", callback_data=("ignore"))

        btns = buttons.create_buttons(6)
        list = []

        for elem in btns[0]:
            list.append(elem)

        x = 0
        for i in range(6):
            if x == 15:
                keyboard6.row(list[x])
                break
            keyboard6.row(list[x], list[x + 1], list[x + 2])
            x += 3

        keyboard6.row(
            page_btn_1, page_btn_2, page_btn_3, page_btn_4, page_btn_5, page_btn_6
        )

        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.message_id,
            text="Выберите язык:",
            reply_markup=keyboard6,
        )

    elif call.data in languages.languages_ru.keys():
        global current_language
        current_language = call.data
        bot.answer_callback_query(
            call.id,
            text=f"Выбран язык: {languages.languages_ru[current_language].capitalize()}",
        )


# answer to translate
@bot.message_handler(content_types=["text"])
def translation(message):
    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(
        "Выбрать язык", callback_data="change_language"
    )
    keyboard.add(button1)
    answer = result_info(message.text, current_language)
    bot.send_message(
        message.chat.id,
        f"Оригинал: {answer[1]}\n\nПеревод: {answer[2]}\n\nЯзык: {languages.languages_ru[current_language].capitalize()}",
        reply_markup=keyboard,
    )


bot.infinity_polling()
