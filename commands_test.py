import discord
import os

from discord.ext import commands
from test_stuff.tasks_test import ScheduledHi
intents = discord.Intents.all()

client = discord.Client(intents=intents)
channelID = 895769591190548563
BELLA_ID = 660763476943306762

@client.event
async def on_ready():
    user = client.get_user(BELLA_ID)
    print(user)
    task = ScheduledHi(bot=client, user=user)
    await task.printer()

client.run(os.getenv('TOKEN'))

