from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
import time

options = Options()
options.headless = True
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-dev-shm-usage')
# #options.binary_location='GUIAutomatedTests/ChromeExe/linux/chromedriver_linux64/chromedriver'
# #print("Binary Location",options.binary_location)
# options.add_argument('--start-maximized')
# # options.add_argument("--disable-infobars")
# options.add_argument('--disable-notifications')
# # added these 3 lines for circleci linux
# # options.add_argument('--headless')
#
# # added these 3 lines above for circleci linux
options.add_argument("no-sandbox")
options.add_argument("--disable-extensions")
options.add_argument("--headless")
# #options.add_argument("--headless")
# options.add_argument('--window-size=1920x1080')
# user_agent = \
#     'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)
#     Chrome/86.0.4240.111 Safari/537.36 PTST/1.0'
# options.add_argument('user-agent={0}'.format(user_agent))
# use this code below to execute headless state
driver = webdriver.Chrome(options=options,executable_path=
'GUIAutomatedTests/ChromeExe/linux/chromedriver_linux64/chromedriver')
driver = webdriver.Chrome("/home/circleci/.wdm/drivers/chromedriver/linux64/95.0.4638.17",options=options)
# service = Service("C:\\exe installer\\chrome driver\\chromedriver_win32\\chromedriver.exe")

# driver = webdriver.Chrome(service=service, options=options)

# while deployment
# driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.GOOGLE).install(),options=options)

url_name = "https://staging.blavity.com/"
# url_name = "https://blavity.com/"
actions = ActionChains(driver)
