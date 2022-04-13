from selenium import webdriver
import time
import os
import stat
from selenium.webdriver.chrome.options import Options

DAVE_SONGVIEW = 'https://repertoire.bmi.com/Search/Catalog?num=F%252btAzu6fjIiTIo1SFOajWQ%253d%253d&cae=evPJVZlCDO5H8s2jCKN5rQ%253d%253d&partType=WriterList&search=%7B%22Main_Search_Text%22%3A%22afi%22%2C%22Sub_Search_Text%22%3A%22%22%2C%22Main_Search%22%3A%22Catalog%22%2C%22Sub_Search%22%3Anull%2C%22Search_Type%22%3A%22all%22%2C%22View_Count%22%3A100%2C%22Page_Number%22%3A1%2C%22Part_Type%22%3A%22PerformerList%22%2C%22Part_Id%22%3A%22HvNjLwM%252bQ%252bvky%252bX4HQW1bQ%253d%253d%22%2C%22Part_Id_Sub%22%3Anull%2C%22Part_Name%22%3Anull%2C%22Part_Cae%22%3Anull%2C%22Original_Search%22%3A%22Performer%22%2C%22DisclaimerViewed%22%3Anull%7D&resetPageNumber=True&partIdSub=YO0HedHMatLb45JzS23DVw%253d%253d#'

# driver = webdriver.Chrome(executable_path='https://replit.com/@honeylemonicete/ErwinDiscordBot#chromedriver.exe')

st = os.stat('chromedriver')
os.chmod('chromedriver', st.st_mode | stat.S_IEXEC)
chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome('chromedriver', options=chrome_options)


def get_song_num():
    # as of april 2022 Dave has 269 songs, if this amount is higher, means that he registered a new one

    driver.get(DAVE_SONGVIEW)

    time.sleep(3) #waiting for the page to load
    accept_btn = driver.find_element_by_id('btnAccept')
    accept_btn.click()

    song_num = driver.find_element_by_class_name('results-font')
    number_str = song_num.text
    number = int(number_str[0:3])
    print(number)
    if number > 269:
        return 'New songs?!! Go check out'
    else:
        return 'Nothing new'

