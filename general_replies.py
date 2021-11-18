import random

reply_options = {
    'toGratitude': [
        'You\'re welcome!',
        'You’re very welcome',
        'That’s all right',
        'No problem',
        'No worries',
        'Don’t mention it',
        'It’s my pleasure',
        'My pleasure',
        'Anytime',
        'It was the least I could do',
        'Glad to help',
        'Sure!',
        'Thank YOU'
    ],
    'toLove': [
        'I know',
        'Love you, too',
        'I will never ever get tired of hearing that',
        'You\'re my downfall, You\'re my muse. My worst distraction, my rhythm and blues',
        'My head\'s under water, but I\'m breathin\' fine. You\'re crazy and I\'m out of my mind',
        'I’m so happy that we found each other',
        'You mean the world to me',
        'You are the best thing that has ever happened to me',
        'I love you to the moon and back!',
        'I can’t believe you picked me'

    ],
    'toMiss': [
        'I miss you too',
        'I’ve been thinking about you too',
        'I wish you were here.',
        'I can’t wait to see you again',
        'I am counting down the days until we’re together again',
        'I keep myself sane by staring at our pictures',
        'Not having you here is driving me crazy.',

    ],
    'howRU':[
        'Pretty good',
        'Not too bad',
        'Same old, same old',
        'Thanks for asking. Doing just great',
        'I think I\'m okay. You?'
    ],

    'soothing': [

    ]
}


def get_bot_reaction(message):
    if "thank" in message:
        replies = reply_options.get('toGratitude')
        reply = random.choice(replies)
        return reply
    elif 'love' in message:
        replies = reply_options.get('toLove')
        reply = random.choice(replies)
        return reply
    elif 'miss you' in message:
        replies = reply_options.get('toMiss')
        reply = random.choice(replies)
        return reply
    elif 'how are you' in message or 'how is it going' in message or 'what\'s up' in message:
        replies = reply_options.get('howRU')
        reply = random.choice(replies)
        return reply

    elif message == "我爱你":
        return "我也爱你😘"

    # SOME SPECIAL REpliES SECTION
    elif message == 'i took an arrow to the heart':
        return 'I never kissed a mouth that tastes like yours'
    elif message == 'i feel so extraordinary':
        return 'Something\'s got a hold on me\n I get this feeling\nI\'m in motion\nA certain sense of liberty\nI don\'t care \'cause I\'m not there\nAnd I don\'t care if I\'m here tomorrow\nAgain and again I\'ve taken too much\nOf the things that cost you too much'
    else:
        return 'Please, be patient. Doing the best I can to understand what you want. I\'m not perfect yet'
