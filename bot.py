from pyrogram import *
from pyrogram.handlers import *
from Anime_Downloader_Probot.anime_search import anime_search
from Anime_Downloader_Probot.start_message import start_message
from Anime_Downloader_Probot.dev_info import dev_info
import logging
from Anime_Downloader_Probot.genres import genres
from Anime_Downloader_Probot.genre_results import genre_results
from Anime_Downloader_Probot.get_anime_details import anime_details
from Anime_Downloader_Probot.inline_search import inline_search
from Anime_Downloader_Probot.get_episodes_index import get_epIndex
from Anime_Downloader_Probot.get_episode_link import get_ep_link
from Anime_Downloader_Probot.instructions import instructions
from Anime_Downloader_Probot.airing import airing_eps
from Anime_Downloader_Probot.recently import recently_eps
from Anime_Downloader_Probot.inline_search_results import anime_inline_details
from Anime_Downloader_Probot.get_ep_numbers import get_ep
import config

import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
import os

if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config


# Creating a Session to activate all Handlers
bot = Client(
    "Anime Downloader Probot",
    api_id=Config.APP_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.TG_BOT_TOKEN,
)

# Adding all functions to Handlers in main() function
def main():
    bot.add_handler(MessageHandler(anime_search, filters.regex(r'search')), group=1)
    bot.add_handler(MessageHandler(start_message, filters.command('start')), group=2)
    bot.add_handler(MessageHandler(dev_info, filters.command('info')), group=3)
    bot.add_handler(MessageHandler(genres, filters.command('genres')), group=4)
    bot.add_handler(InlineQueryHandler(inline_search), group=6)
    bot.add_handler(MessageHandler(airing_eps, filters.command("airing")), group=7)
    bot.add_handler(CallbackQueryHandler(anime_details, filters.regex('dt_*')), group=8)
    bot.add_handler(CallbackQueryHandler(get_epIndex, filters.regex('dl_*')), group=9)
    bot.add_handler(CallbackQueryHandler(get_ep_link, filters.regex('eps_*')), group=10)
    bot.add_handler(CallbackQueryHandler(genre_results, filters.regex('genre/')), group=11)
    bot.add_handler(CallbackQueryHandler(instructions, filters.regex('instructions')), group=12)
    bot.add_handler(MessageHandler(anime_inline_details, filters.text), group=13)
    bot.add_handler(CallbackQueryHandler(get_ep, filters.regex('eplink_*')), group=14)
    
    bot.add_handler(MessageHandler(recently_eps, filters.command("recently")), group=15)

# Calling main method and handlers, polling state
if __name__ == '__main__':
    bot.run(main())
