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


QUALITY_LABELS = {"128": "128K", "320": "320K", "lossless": "Lossless"}
def quality_keyboard(song, allow_vip=False):
    buttons = []

    for stream in song["streamURL"]:
        if stream["status"] != 1:
            continue
        if stream["onlyVIP"] and not allow_vip:
            continue

        buttons.append(
            InlineKeyboardButton(
                text=QUALITY_LABELS.get(stream["type"], stream["type"]),
                callback_data=f"quality_{stream['type']}"
            )
        )

    return InlineKeyboardMarkup(inline_keyboard=[buttons])
