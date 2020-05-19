# -*- coding: utf-8 -*-
from selenium import webdriver
# Optionsのimport
from selenium.webdriver.chrome.options import Options
import time
url = "file:///C:/Users/writer/study_work/html/menu.html"
# オプション指定
options = Options()
options.add_argument('--incognito')
options.add_argument('--window-size=500,300')
# オプションを渡す
driver = webdriver.Chrome(options=options)
driver.get(url)
time.sleep(3)
driver.quit()