from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

import time

chrome_options = Options()
chrome_options.add_argument("--headless")
browser = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=chrome_options)
url = "https://www.abc.net.au/news/australia/"

browser.get(url)
time.sleep(2)
available = ''

try: 
    headlines = browser.find_elements_by_class_name("_7fOxm")
except:
    pass

for headline in headlines:
    print(headline.text)