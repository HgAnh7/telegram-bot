from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def songs_keyboard(songs):
    buttons = []
    row = []

    for index, song in enumerate(songs, start=1):
        row.append(
            InlineKeyboardButton(
                text=str(index),
                callback_data=f"nct_song_{index}"
            )
        )
        
        # Thụt lề đồng nhất 8 khoảng trắng
        if len(row) == 5:
            buttons.append(row)
            row = []
            
    if row:
        buttons.append(row)

    return InlineKeyboardMarkup(
        inline_keyboard=buttons
    )




def quality_keyboard():

    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="128K",
                    callback_data="quality_128"
                ),

                InlineKeyboardButton(
                    text="320K",
                    callback_data="quality_320"
                ),

                InlineKeyboardButton(
                    text="Lossless",
                    callback_data="quality_lossless"
                )
            ]
        ]
    )
