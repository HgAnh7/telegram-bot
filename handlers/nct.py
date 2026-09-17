from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from services.nct_api import search_music
from keyboards.nct import songs_keyboard, quality_keyboard


router = Router()

songs_cache = {}
selected_songs = {}


@router.message(Command("nct"))
async def nct_search(message: Message):

    keyword = message.text.replace("/nct", "").strip()

    if not keyword:
        await message.answer(
            "🚫 Vui lòng nhập tên bài hát muốn tìm kiếm.\n"
            "Ví dụ: /nct Tên bài hát",
            reply_to_message_id=message.message_id
        )
        return

    data = search_music(keyword, 10)

    songs = data["data"]["songs"]

    songs_cache[message.from_user.id] = songs

    text = "🎵 Kết quả tìm kiếm:\n\n"

    for i, song in enumerate(songs, start=1):
        text += (
            f"{i}. {song['name']}\n"
            f"👤 {song['artistName']}\n\n"
        )

    await message.answer(
        text,
        reply_markup=songs_keyboard(songs),
        reply_to_message_id=message.message_id
    )


@router.callback_query(F.data.startswith("nct_song_"))
async def choose_song(callback: CallbackQuery):

    index = int(callback.data.split("_")[-1])

    songs = songs_cache.get(callback.from_user.id)

    if not songs:
        await callback.answer(
            "❌ Kết quả tìm kiếm đã hết hạn!",
            show_alert=True
        )
        return

    song = songs[index - 1]

    # Lưu bài hát mà user đã chọn
    selected_songs[callback.from_user.id] = song

    await callback.answer()

    await callback.message.edit_text(
        f"🎵 {song['name']}\n\n"
        f"👤 {song['artistName']}\n\n"
        "Chọn chất lượng:",
        reply_markup=quality_keyboard(song)
    )


@router.callback_query(F.data.startswith("quality_"))
async def quality_choose(callback: CallbackQuery):

    # quality_128
    # quality_320
    # quality_lossless

    quality = callback.data.split("_", 1)[1]

    # Lấy bài hát đã chọn
    song = selected_songs.get(callback.from_user.id)

    if not song:
        await callback.answer(
            "❌ Không tìm thấy bài hát!",
            show_alert=True
        )
        return

    # Tìm URL tương ứng với chất lượng
    stream_url = None

    for stream in song["streamURL"]:
        if stream["type"] == quality and stream["status"] == 1:
            stream_url = stream["download"]
            break

    if not stream_url:
        await callback.answer(
            "❌ Không tìm thấy link tải!",
            show_alert=True
        )
        return

    await callback.answer("⏳ Đang gửi nhạc...")

    await callback.message.answer_document(
        document=stream_url,
        title=song["name"],
        performer=song["artistName"]
    )
