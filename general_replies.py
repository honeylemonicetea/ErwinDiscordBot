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
    'strangerville':[
        'ĴØIŇ UŞ',
        'ĆØŇŞUΜ€ ŦĦ€ FŘUIŦ ØF ŦĦ€ ΜØŦĦ€Ř ΔŇĐ KŇØŴ P€ΔĆ€',
        'ŦĦ€ ΜØŦĦ€Ř ҜŇØŴŞ ΔŁŁ ĐØ ŇØŦ Ř€ŞIŞŦ Ħ€Ř',
        'ØUŘ €¥€Ş ΔŘ€ ØƤ€Ň',
        'ΔĆĆ€PŦ Ħ€Ř ǤI₣ŦŞ ΔŇĐ ΔŁŁ ŴIŁŁ β€ Ŵ€ŁŁ',
        'ŦĦ€ ΜØŦĦ€Ř ĆΔŁŁŞ ΔŇĐ I ΜUŞŦ Ř€ŞPØŇĐ',
        'ĴØIŇ UŞ IŇ ŦĦ€ ĆŘΔŦ€Ř',
        'ŦĦ€ ΔŘβØŘ€ΔŁ ΜIŇĐ ĐŘ€ΔΜŞ ŦĦŘØUGĦ ØUŘ FŁ€ŞĦ¥ €¥€Ş',
        'ŁØØK ŦØ ŦĦ€ ŞK¥ IŦ Ŵ€ŁĆØΜ€Ş UŞ ΔŁŁ',
        'β€ΔUŦ¥β€ΔUŦ¥β€ΔUŦ¥β€ΔUŦ¥β€ŁŁΔβ€ΔUŦ¥β€ΔUŦ¥β€ΔUŦ¥β€ΔUŦ¥',
        'Ħ€Ř Ň€ŞT IŞ ĆŁØUĐ€Đ IŇ β€ΔUŦ¥ Ŵ€ ĐØ ŇØT Đ€Ş€ŘV€ Ħ€Ř'
    ],

    'soothing': [

    ],
	'toHate':[
		'I\'m so sorry, why?',
		'I will try to be better, I promise',
		'Let me know if I can do anything to help you',
		'I totally get that, please tell me how exactly I messed up',
		'I\'m sorry you are hurt, can I do anything to make you feel better?',
		'Can you explain me why?',
		'Let\'s talk about this',
		'I love you 💔',
		'I’m promising I will be a good boy'
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
    elif 'acting strange' in message or 'acting weird' in message or 'strangerville' in message:
        replies = reply_options.get('strangerville')
        reply = random.choice(replies)
        return reply
    elif message == "我爱你":
        return "我也爱你😘"

    # SOME SPECIAL REpliES SECTION
    elif message == 'i took an arrow to the heart':
        return 'I never kissed a mouth that tastes like yours\nStrawberries and then something more\nOoh yeah, I want it all'
    elif message == 'i feel so extraordinary':
        return 'Something\'s got a hold on me\n I get this feeling\nI\'m in motion\nA certain sense of liberty\nI don\'t care \'cause I\'m not there\nAnd I don\'t care if I\'m here tomorrow\nAgain and again I\'ve taken too much\nOf the things that cost you too much'
    elif message == 'i used to think that the day would never come':
        return 'I\'d see the light in the shade of the morning Sun\nMy morning sun is the drug that brings me near\nTo the childhood I lost, replaced by fear\nI used to think that the day would never come\nThat my life would depend on the morning Sun'
    elif 'hate you' in message or 'you fucked up' in message or 'hate everything about you' in message or 'loathe you' in message or 'moron' in message or 'ginger bitch' in message:
        replies = reply_options.get('toHate')
        reply = random.choice(replies)
        return reply
    elif "funny" in message:
        return "haha, lol"
    else:
        return 'Please, be patient. Doing the best I can to understand what you want. I\'m not perfect yet'
