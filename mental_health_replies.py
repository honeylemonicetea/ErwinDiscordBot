# identify if you're struggling
# pick a right answer
import random

phrases = [
        'bad', 'sad', 'helpless', 'hopeless', 'aching', 'lost', 'worthless', 'useless', 'stupid', 'stuck', 'untethered', 'adrift',
        'hurting', 'alone', 'afraid', 'unsure', 'insecure', 'despair', 'tired', 'exhausted', 'knackered', 'no one cares',
        'kill myself', 'suicide', 'jump off','no reason to live', 'lonely', 'i have no one',
        'die alone', 'want to die', 'wanna die', 'sick and tired']


responses = [
        'Hey, I\'m right here, just breathe, okay?',
        'Can I do anything to help you?',
        'I would hug if only I were real',
        'Can I help you not to hurt anymore?',
        'Just remember, so far you have survived 100% of your bad days',
        'I know things are difficult right now...',
]


def check_mh(raw_message):
    for word in phrases:
        if word in raw_message:
            return random.choice(responses)
