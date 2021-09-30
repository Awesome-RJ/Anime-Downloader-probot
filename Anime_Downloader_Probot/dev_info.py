from pyrogram import *
from pyrogram.types import *

# Dev Info is Completely Optional

def dev_info(client, message):
    keyb = [
        [InlineKeyboardButton("Supoort", url="https://t.me/Black_Knights_Union_Support")]
    ]
    reply_markup = InlineKeyboardMarkup(keyb)
    message.reply_text("""Made with 💜 in 🇮🇳 by @Black_Knights_Union.
Language: [Python3](https://www.python.org/)
Bot Framework: [Pyrogram Asyncio](https://github.com/pyrogram/pyrogram)
Server: Yūki Cloud
Please share the bot if you like it 💜""", reply_markup=reply_markup, parse_mode="markdown")