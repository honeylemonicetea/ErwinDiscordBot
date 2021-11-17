import requests
import json


def get_stories(topic):
    r = requests.get('https://gentle-basin-15677.herokuapp.com/stories')
    reply_list = r.text
    raw_text = json.loads(reply_list)
    raw_dict = dict(raw_text[0])


    try:
        story_list = raw_dict.get(topic)
    except Exception:
        story_list = 'Error'

    return story_list


