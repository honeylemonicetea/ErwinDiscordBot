import discord
import os
from im_alive import keep_alive
from api_query import get_stories
from general_replies import get_bot_reaction
import random
import asyncio
from test_stuff.tasks_test import ScheduledHi

intents = discord.Intents.all()

client = discord.Client(intents=intents)
BELLA_ID = 660763476943306762

# user = client.fetch_user(660763476943306762)
# print(user)
# user.send()

# TEST FEATURE END


@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))
	user = client.get_user(BELLA_ID)
	print(user)
	if user != None:
		task = ScheduledHi(bot=client, user=user)
		await task.printer()


@client.event
async def on_message(message):
    msg = message.content.lower()
    # print(msg)

    if message.author == client.user:
        return
    if msg == 'hey baby' or msg == 'hi baby' or msg == 'hello honey' or msg == 'hey honey' or msg == 'hi honey':
        await message.channel.send(f'Hi darling')
    elif "erwin" in msg and ("hi" in msg or "hey" in msg or "hello" in msg):
        user_name = str(message.author).split()[0]
        await message.channel.send(f'Hi {user_name}')
    elif msg.startswith('hello') or msg.startswith('hey') or msg.startswith(
            'hi'):
        await message.channel.send('Greetings stranger!')

    # STORY TELLING FEATURE
    elif msg.startswith('#tell'):
        topic = msg.split(" ")[1]
        print(topic)
        stories = get_stories(topic)
        print(stories)
        if stories != 'Error' or stories is not None:
            toSend = random.choice(stories)
            await message.channel.send(toSend)
        else:
            await message.channel.send('Nothing here')
            # HANDLING OTHER REPLIES
    elif msg.startswith('image'):
        await message.channel.send(file=discord.File('images/imageT.jpg'))
    else:
        reply = get_bot_reaction(msg)
        await asyncio.sleep(2)
        await message.channel.send(reply)


keep_alive()
client.run(os.getenv('TOKEN'))
  #TEST FEATURE
