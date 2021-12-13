import requests
from bs4 import BeautifulSoup
import random


def far_cry():

    URL = 'https://www.reddit.com/r/CrackWatch/comments/p9ak4n/crack_watch_games/'
    uncracked = None
    while uncracked == None:

        reqs = requests.get(URL)
        # far cry
        #TABLE CLASS MRH-njmSb5ZTkfb1o4dqv
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

