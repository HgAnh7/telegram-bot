from aiogram.utils.keyboard import InlineKeyboardBuilder

BUTTONS_PER_ROW = 5
QUALITY_LABELS = {"128": "128K", "320": "320K", "lossless": "Lossless"}


def songs_keyboard(songs):
    kb = InlineKeyboardBuilder()

    for index in range(1, len(songs) + 1):
        kb.button(text=str(index), callback_data=f"nct_song_{index}")

    kb.adjust(BUTTONS_PER_ROW)
    return kb.as_markup()


def quality_keyboard(song, allow_vip=False):
    qualities = []

    for stream in song.get("streamURL", []):
        if stream.get("status") != 1:
            continue
        #if stream.get("onlyVIP") and not allow_vip:
            continue
        qualities.append(stream["type"])

    if not qualities:
        return None

    kb = InlineKeyboardBuilder()

    for quality in qualities:
        kb.button(
            text=QUALITY_LABELS.get(quality, quality),
            callback_data=f"quality_{quality}",
        )

    kb.adjust(len(qualities))
    return kb.as_markup()