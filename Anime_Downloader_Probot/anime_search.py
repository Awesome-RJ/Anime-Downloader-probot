import random
from pyrogram import *
from pyrogram.types import *
from requests_html import HTMLSession
from bs4 import BeautifulSoup

# Searching anime by regex pattern "/search <space> Anime Name"

STICKERS = (
    "CAACAgUAAxkBAAECXWJgtiefn2bNuYvjcasry5Lq-mzdswACRQUAAo8k-yWDStn_vuRiJx8E",
    "CAACAgUAAxkBAAECXWRgtiex1-92fGAkCL6F4hUljcB-DwACRgUAAo8k-yXR5cffI3xb1B8E",
    "CAACAgUAAxkBAAECXWZgtifCTWcP5tD80Hu8rWXM7twZhwACSAUAAo8k-yVTtcAPPm0Fnh8E",
    "CAACAgUAAxkBAAECXWpgtifaRvjk3b-9miZNQBJlWnEc1AACSwUAAo8k-yVXsvrfR6PybB8E",
    "CAACAgUAAxkBAAECXWpgtifaRvjk3b-9miZNQBJlWnEc1AACSwUAAo8k-yVXsvrfR6PybB8E",
    "CAACAgUAAxkBAAECXW5gtif6Cc44r_2jzFxHAT7BRLvJ6QACYgUAAo8k-yUovgRpFjZxVB8E",
    "CAACAgUAAxkBAAECXXBgtigEMhqhaSJ9OKqAVd3ZhgQhDQACTQUAAo8k-yWqQEy4R3jDdh8E",
    "CAACAgUAAxkBAAECXXJgtigNL2b1BUB4ZxiMMUEe9gABgXgAAk4FAAKPJPslJNVyFsxkQ9kfBA",
    "CAACAgUAAxkBAAECXXRgtigb_YIPjCi_2zPYmTwrkKrHjgACTwUAAo8k-yWWnH54i3OHVx8E",
    "CAACAgUAAxkBAAECXXZgtigpzpjfIlF5QnmA2YKIc2EccAACXgUAAo8k-yVXChZTI-azSR8E",
    "CAACAgUAAxkBAAECXXhgtig7fwOVW7o1xn2ewd_km1jI5QACUAUAAo8k-yWa5t8K4xD6_R8E",
    "CAACAgUAAxkBAAECXXpgtihDoP7nXX2tr7UgyZq2tGz2CAACVAUAAo8k-yV9eFBSbQQRMR8E",
    "CAACAgUAAxkBAAECXXxgtihL-2iP1zBYQiB1y7KOUt60NgACUgUAAo8k-yWc-JioTAk_oh8E",
    "CAACAgUAAxkBAAECXX5gtihVC1vZVzR5MAL3yr_dTW0n0AACUwUAAo8k-yV3JqRPKrQSah8E",
    "CAACAgUAAxkBAAECXYBgtihfb9-gOSFFwiuqpSOdWI6yrwACZAUAAo8k-yWRqCeZ1KsG0B8E",
    "CAACAgUAAxkBAAECXYJgtihoH4WyFDWPoYTwlkPVrgOibQACWwUAAo8k-yVus6mAugABQOUfBA",
    "CAACAgUAAxkBAAECXYRgtihxlPGl8dwgo4ogUqni10ctRgACXwUAAo8k-yUQk3HMByo3-R8E",
    "CAACAgUAAxkBAAECXYZgtih66JTGQzzxcMjRM5Bv-vLJ4QACYAUAAo8k-yVRM8Gp-b6C9x8E",
    "CAACAgUAAxkBAAECXYhgtiiDGi3GkpuWr6Mj_epVgsGxhQACcgUAAo8k-yWL7DaqHVNvqR8E",
    "CAACAgUAAxkBAAECXYpgtiiK60ASuhzn5HF1hqlCyeWYHQACYQUAAo8k-yU17VzPXRipPB8E",
    "CAACAgUAAxkBAAECXYxgtiieT0cYvIYTwqzAPPOi-x-IIgACYwUAAo8k-yVtsLZX7RZPZx8E",
)


def anime_search(client, message):
    q = message.text
    q1 = q.split()
    q1.remove(q1[0])
    str = " "
    query = str.join(q1)
    if query == "":
        # If no query string is mentioned
        message.reply_sticker(random.choice(STICKERS))
        message.reply_text(
            text="""**Your Query should be in This format:** \x1f\x1f`/search <space> Name of the Anime you want to Search.`\x1fFor ex: /search one piece\x1f""",
            parse_mode="markdown",
        )

    else:
        url = f"https://gogoanime2.org/search.html?keyword={query}"
        session = HTMLSession()
        response = session.get(url)
        response_html = response.text
        soup = BeautifulSoup(response_html, 'html.parser')
        animes = soup.find("ul", {"class": "items"}).find_all("li")
        # print(animes)
        keyb = []
        for anime in animes:  # For every anime found
            tit = anime.a["title"]
            urll = anime.a["href"]
            r = urll.split('/')
            # aAnimes.append({"title" : anime.a["title"] , "link" : "https://www2.gogoanime.pe{}".format(anime.a["href"])})
            keyb.append([InlineKeyboardButton("{}".format(tit), callback_data="dt_{}".format(r[2]))])
        if not keyb:
            # If returned list is empty, Send the following message.
            message.reply_text("❌ No results found, Check your Spelling and Search Again...")
        else:
            rep = InlineKeyboardMarkup(keyb)
            message.reply_text(text=f"Here is Your Search Results for **{query}**", reply_markup=rep, parse_mode="markdown")

