from pyrogram import *
from pyrogram.types import *
import requests
from bs4 import BeautifulSoup

# Get anime Details on anime_search callback_data

def anime_details(client, callback_query):
    global list_more_anime
    query = callback_query
    dt = query.data
    dt1 = dt.split("_")
    data = dt1[1]
    query.answer("⏳ Fetching Anime Details...")
    animelink = 'https://gogoanime2.org/category/{}'.format(data)
    response = requests.get(animelink)
    plainText = response.text
    soup = BeautifulSoup(plainText, "lxml")
    source_url = soup.find("div", {"class": "anime_info_body_bg"}).img
    # url of anime image
    imgg = source_url.get('src')
    # title name of the anime
    tit_url = soup.find("div", {"class": "anime_info_body_bg"}).h1.string
    lis = soup.find_all('p', {"class": "type"})
    plot_sum = lis[1]
    pl = plot_sum.get_text().split(':')
    pl.remove(pl[0])
    sum = ""
    plot_summary = sum.join(pl)
    type_of_show = lis[0].a['title']
    ai = lis[2].find_all('a')  # .find_all('title')
    # get list of genres by using genres variable
    genres = [link.get('title') for link in ai]
    # get released year
    year = lis[3].get_text()
    # status completed or airing,,,
    status = lis[4].a.get_text()
    # other names
    oth_names = lis[5].get_text()
    lnk = soup.find(id="episode_page")
    source_url = lnk.find("li").a
    # ending ep no
    try:
        source_url = lnk.findAll("li")
        for link in source_url:
            list_more_anime = []
            list_more_anime.append(link.a)
        ep_num = list_more_anime[0].get("ep_end")
    except:
        source_url = lnk.find("li").a
        ep_num = source_url.get("ep_end")
    kkeeyyb = [
        [InlineKeyboardButton("📥 Download", callback_data=f"dl_{data}")],
    ]
    reply_markup = InlineKeyboardMarkup(kkeeyyb)
    query.edit_message_text(f"""
**🎬 Title: [{tit_url}]({imgg})**
**{oth_names}**
**📅 Year:** ({year})
**◼️ Type:** {type_of_show}
**◼️ Status: **{status}
**◼️ Genres: **{genres}
**◼️ Episodes: **{ep_num}
**◼️ Summary: **{plot_summary}""", reply_markup=reply_markup, parse_mode="markdown")
