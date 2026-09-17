from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

BUTTONS_PER_ROW = 5


def songs_keyboard(songs):
    buttons = []
    row = []

    for index in range(1, len(songs) + 1):
        row.append(InlineKeyboardButton(text=str(index), callback_data=f"nct_song_{index}"))
        if len(row) == BUTTONS_PER_ROW:
            buttons.append(row)
            row = []

    if row:
        buttons.append(row)

    return InlineKeyboardMarkup(inline_keyboard=buttons)


def quality_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(text="128K", callback_data="quality_128"),
        InlineKeyboardButton(text="320K", callback_data="quality_320"),
        InlineKeyboardButton(text="Lossless", callback_data="quality_lossless"),
    ]])
