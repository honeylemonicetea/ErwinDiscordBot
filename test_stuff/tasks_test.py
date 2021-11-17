from discord.ext import tasks, commands

class TestCog(commands.Cog):
    def __init__(self, bot):
        self.index = 0
        self.printer.start()
        self.bot = bot

    def cog_unload(self):
        self.printer.cancel()

    @tasks.loop(seconds=5.0)
    async def printer(self):
        print(self.index)
        self.index += 1


class ScheduledHi(commands.Cog):
    def __init__(self, bot, user):
        self.printer.start()
        self.user = user
        self.bot = bot


    @tasks.loop(hours=6)
    async def printer(self):
        await self.user.send('Hello, anything new?')

