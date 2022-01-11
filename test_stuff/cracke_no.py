import os

import requests
from bs4 import BeautifulSoup
import random
import pylast


def far_cry():
    URL = 'https://www.reddit.com/r/CrackWatch/comments/p9ak4n/crack_watch_games/'
    uncracked = None
    while uncracked == None:

        reqs = requests.get(URL)
        # far cry
        # TABLE CLASS MRH-njmSb5ZTkfb1o4dqv
        soup = BeautifulSoup(reqs.content, 'lxml')
        # print(soup.prettify())
        uncracked = soup.find(class_='MRH-njmSb5ZTkfb1o4dqv')
        if uncracked != None:
            uncracked_res = uncracked.text
            if 'Far Cry 6' in uncracked_res:
                return 'Far Cry 6 is still among the uncracked games'
            else:
                return 'Far Cry 6 is probably cracked! Go check it out'
        else:
            print('couldn\'t find it sorry')


def get_dollar():
    DOLLAR_URL = 'https://www.xe.com/currencyconverter/convert/?Amount=1&From=USD&To=RUB'
    dollar_req = requests.get(DOLLAR_URL)
    soup2 = BeautifulSoup(dollar_req.content, 'lxml')
    # print(soup2.prettify())
    tag = soup2.find(class_="result__BigRate-sc-1bsijpp-1 iGrAod")
    # dollar rate
    return tag.get_text()


def get_motivated():
    with open('resources/motivation.txt', encoding='utf-8') as file:
        data = file.read()
        quotes = data.split("\n")
    # print(quotes)
    quote = random.choice(quotes)
    return quote


def get_song(query):
    headers = {
        'Authorization': os.getenv('GENIUS')
    }
    API_URL = 'http://api.genius.com/'
    search_params = {
        'q': query
    }
    req = requests.get(API_URL + 'search?', headers=headers, params=search_params)
    print(req.status_code)
    req_c = req.json()
    song_link = req_c['response']['hits'][0]['result']['url']
    return song_link



# LAST FM
API_KEY = ''
API_SECRET = ''

username = "BellaLeto"
password_hash = pylast.md5('')

network = pylast.LastFMNetwork(
    api_key=API_KEY,
    api_secret=API_SECRET,
    username=username,
    password_hash=password_hash,
)
user = network.get_user('BellaLeto')
# Now you can use that object everywhere
def get_artists_week():
    arts = []
    top_week = user.get_top_artists(limit=6, period=pylast.PERIOD_7DAYS)
    for num, top in enumerate(top_week):
        artist = top.item.name
        arts.append(f"{num}. {artist}")
    print(arts)


def get_songs_week():
    songs = []
    songs_week = user.get_top_tracks(period=pylast.PERIOD_7DAYS, limit=6)
    for num, top in enumerate(songs_week):
        song = f"{num}. {top.item}. Times played: {top.weight}"
        songs.append(song)
    print(songs)
# for i in range(50):
#     time.sleep(60)
#     arts = network.scrobble('Ed Sheeran','Stop the Rain', timestamp=time.time())
#     print(arts)
# Type help(pylast.LastFMNetwork) or help(pylast) in a Python interpreter
# to get more help about anything and see examples of how it works

