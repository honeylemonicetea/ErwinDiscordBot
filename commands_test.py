import discord

from discord.ext import commands


intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(self_bot=True, command_prefix='!', intents=intents)
USER_ID = 660763476943306762


async def send_m():
    user = await bot.fetch_user(USER_ID)
    print(user.__str__())

    try:

        await user.send('hey this is automatic')

        return
    except Exception:
        print('Something is wrong with getting the user')


bot.loop.create_task(send_m())