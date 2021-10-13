from pyrogram import *
from pyrogram.types import *

# Attractive Welcome message

def start_message(client, message):
    kkeeyyb = [
        [InlineKeyboardButton("Instructions", callback_data="instructions")],
    ]
    reply_markup = InlineKeyboardMarkup(kkeeyyb)
    pic_url = "https://telegra.ph/file/4134ab4b30a39af7ad712.jpg"
    message.reply_photo(pic_url, caption=f"""**Hy Sweetherat! I am An Advanace Anime Downloader ProBot ⚡**
I Will Provide You Fastest Anime Direct Downloading Link.
Try the instructions button below For Bot instructions ^_^
""", reply_markup=reply_markup, parse_mode="markdown")