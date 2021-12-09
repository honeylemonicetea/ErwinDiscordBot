# import aiohttp
# import asyncio
#
# async def main():
#
#     async with aiohttp.ClientSession() as session:
#             response = await session.get('https://www.sberbank.ru/ru/quotes/currencies')
#             print("Status:", response.status)
#             print("Content-type:", response.headers['content-type'])
#
#             html = await response.text()
#             print("Body:", html, "...")
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())

# wake up bella skill

import time
import datetime
from pytz import  all_timezones, timezone
def testing_wakeup():
    tz_is = timezone('Europe/Moscow')
    current_time = datetime.datetime.now(tz=tz_is)
    current_hour = current_time.time().hour
    if 23 <= current_hour or 3 >= current_hour >= 1:
        return 'It\'s time for you to have some rest, dear'
    elif 8 <= current_hour <=9:
        return 'Wake Up, Bella!'
    else:
        return None


