def get_lyrics():
    pass


# import requests
#
# url = "https://genius.p.rapidapi.com/artists/16775/songs"
#
# headers = {
#     'x-rapidapi-host': "genius.p.rapidapi.com",
#     'x-rapidapi-key': "i5DswOlsXg4DeraCqZD0sQnxUK8-YHVIEvvF9ovjHPKAMN_RV29VWbEPjB6uzhUp"
#     }
#
# response = requests.request("GET", url, headers=headers)
#
# print(response.text)

from rauth import OAuth1Service

genie = OAuth1Service(
    consumer_key='fK8aBjnHannAuYJgwon1-4xudgR-Z69aJQlq_t7IOc3DPrYe596DJkRLKrQk1wZL',
    consumer_secret='6-Ksfvz08jfOGf9esoQtFTRGVBOjgGdBnv09D8APSyErYFoOSFn4nhkEKXK1hxC7z6nrCuR9MeRBYiT-MCAnbg',
    name='Genius',
    request_token_url='api.genius.com',

)