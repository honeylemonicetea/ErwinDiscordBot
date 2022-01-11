from discord.ext import tasks, commands
from .cracke_no import get_dollar, far_cry, get_motivated
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
       
        await self.user.send(f'Dollar costs {dollar} and  {far_c6}')
        if wakeup != None:
            await self.user.send(f'{wakeup}')

    @tasks.loop(hours=6)
    async def daily_routine(self):
        quote = get_motivated()
        print('quotes are functional')
        username = str(self.user).split(' ')[0]
        await self.user.send(f'I know things are complicated right now, {username}, just hold on for me, okay? Here\'s a motivational quote: ')
        await self.user.send(quote)

    @tasks.loop(hours=12)
    async  def reminder(self):
        pass
			 


