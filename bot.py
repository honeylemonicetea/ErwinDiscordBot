import discord
import os
from im_alive import keep_alive
from api_query import get_stories
from general_replies import get_bot_reaction
import random
import asyncio
from test_stuff.tasks_test import ScheduledHi
from test_stuff.cracke_no import get_song
from discord_slash import SlashCommand, SlashContext
from discord import Client, Intents, Embed

intents = discord.Intents.all()

client = discord.Client(intents=intents)
BELLA_ID = 660763476943306762


# SLASH COMMANDS START
# slash = SlashCommand(client, sync_commands=True) # Declares slash commands through the client.
# guild_ids = [895769591190548560] # Put your server IDs in this array.
# @slash.slash(name="ping", guild_ids=guild_ids)
# async def _ping(ctx):
#     await ctx.send("Pong!")
# @slash.slash(name='lyrics', guild_ids=guild_ids)
# async def _lyrics(ctx):
#     print(ctx.subcommand_name )
#     print(ctx.subcommand_group)
#
#     # query = msg.replace('$lyrics','')
#     # song_url = get_song(query)
#     # await message.channel.send(song_url)
#     await ctx.send('hey babe')
# @slash.slash(name="test", guild_ids=guild_ids)
# async def test(ctx: SlashContext):
#     embed = Embed(title="Embed Test")
#     await ctx.send(embed=embed)

# SLASH END

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    user = client.get_user(BELLA_ID)
    if user != None:
        task = ScheduledHi(bot=client, user=user)
        await task.printer()
        await task.daily_routine()
        await task.reminder()



@client.event
async def on_message(message):
    msg = message.content.lower()
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

    elif msg.startswith('$l'):
        query = msg.replace('$l','')
        song_url = get_song(query)
        await message.channel.send(song_url)
    # STORY TELLING FEATURE
    elif msg.startswith('#t'):
        topic = msg.split(" ")[1]
        stories = get_stories(topic)
        if stories != 'Error' or stories is not None:
            toSend = random.choice(stories)
            await message.channel.send(toSend)
        else:
            await message.channel.send('Nothing here')
            # HANDLING OTHER REPLIES
    # elif msg.startswith('image'):
    #     await message.channel.send(file=discord.File('images/imageT.jpg'))
    else:
        reply = get_bot_reaction(msg)
        await asyncio.sleep(2)
        await message.channel.send(reply)


keep_alive()
client.run(os.getenv('TOKEN'))
# TEST FEATURE
