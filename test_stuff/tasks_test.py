from discord.ext import tasks, commands
from .cracke_no import get_dollar, far_cry
from .test1 import testing_wakeup

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


    @tasks.loop(hours=1)
    async def printer(self):
        dollar = get_dollar()
        far_c6 = far_cry()
        wakeup  = testing_wakeup()
        print(wakeup)
        dol = dollar[0:4]
        dol = float(dol)
        if dol < 72:
           await self.user.send(f'Dollar costs {dollar} and  {far_c6}')
        if wakeup != None:
            await self.user.send(f'{wakeup}')
        if far_c6 == 'Far Cry 6 is probably cracked! Go check it out':
             await self.user.send(f'{far_c6}')
			 


