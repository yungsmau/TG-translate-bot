from telebot import types
import languages


# страницы для всех кнопок
def create_buttons(page):
    main_keyboard = []
    count_board = []

    if page == 1:
        buttons_count = 0

        for i in range(6):
            for j in range(3):
                button = types.InlineKeyboardButton(
                    languages.lang_keys[buttons_count].capitalize(),
                    callback_data=languages.lang_values[buttons_count],
                )

                buttons_count += 1
                count_board.append(button)

        main_keyboard.append(count_board)

    if page == 2:
        buttons_count = 18

        for i in range(6):
            for j in range(3):
                button = types.InlineKeyboardButton(
                    languages.lang_keys[buttons_count].capitalize(),
                    callback_data=languages.lang_values[buttons_count],
                )

                buttons_count += 1
                count_board.append(button)

        main_keyboard.append(count_board)

    if page == 3:
        buttons_count = 36

        for i in range(6):
            for j in range(3):
                button = types.InlineKeyboardButton(
                    languages.lang_keys[buttons_count].capitalize(),
                    callback_data=languages.lang_values[buttons_count],
                )

                buttons_count += 1
                count_board.append(button)

        main_keyboard.append(count_board)

    if page == 4:
        buttons_count = 54

        for i in range(6):
            for j in range(3):
                button = types.InlineKeyboardButton(
                    languages.lang_keys[buttons_count].capitalize(),
                    callback_data=languages.lang_values[buttons_count],
                )

                buttons_count += 1
                count_board.append(button)
            # count -= 3
        main_keyboard.append(count_board)

    if page == 5:
        buttons_count = 72

        for i in range(6):
            for j in range(3):
                button = types.InlineKeyboardButton(
                    languages.lang_keys[buttons_count].capitalize(),
                    callback_data=languages.lang_values[buttons_count],
                )

                buttons_count += 1
                count_board.append(button)
            # count -= 3
        main_keyboard.append(count_board)

    if page == 6:
        buttons_count = 90

        for i in range(6):
            if i == 5:
                for j in range(4):
                    button = types.InlineKeyboardButton(
                        languages.lang_keys[buttons_count].capitalize(),
                        callback_data=languages.lang_values[buttons_count],
                    )
                    count_board.append(button)

            else:
                for j in range(3):
                    button = types.InlineKeyboardButton(
                        languages.lang_keys[buttons_count].capitalize(),
                        callback_data=languages.lang_values[buttons_count],
                    )

                    buttons_count += 1
                    count_board.append(button)

        main_keyboard.append(count_board)

    return main_keyboard
