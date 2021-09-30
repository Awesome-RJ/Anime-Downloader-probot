from pyrogram import *
from pyrogram.types import *

# Totally Optional

def instructions(client, callback_query):
    query = callback_query
    query.answer("Please Read Carefully!!!")
    keyb = [
        [InlineKeyboardButton("Search Anime Inline", switch_inline_query_current_chat="")]
    ]
    reply_markup = InlineKeyboardMarkup(keyb)
    query.edit_message_caption(caption="""**This Bot can help you to Get your favourite Anime & provides FREE Download Links in multiple quality with a fastest server. ❤️😍**

**🗒️ Note:**
➜ Since GogoAnime changes their domain often, The bot will go for frequent maintenance. Don't worry, the bot will still be online during maintenance.
➜ For Streaming in mobile, open the links with MX Player. You can also use VLC Media Player.
➜ For Streaming in PC, use VLC media player network stream.
➜ For downloads, just open the links in a browser (Chrome).

**That's it, Just Start and Enjoy your favourite Anime ⛩️**

**Type /search to Search for an Anime...**""", parse_mode="markdown", reply_markup=reply_markup)
