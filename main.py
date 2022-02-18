import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup

import time
import random
from multiprocessing.pool import ThreadPool

URL = 'https://find-different-color.vercel.app'

options = webdriver.ChromeOptions()

driver_path = input('chrome driver path: ')
nickname = input('your nick name: ')
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.set_window_size(800, 800)
driver.get(url=URL)
driver.find_element(By.CLASS_NAME, 'sc-bYoBSM.iyIJpi').click()
driver.find_element(By.CLASS_NAME, 'sc-bBHxTw.dScklU').send_keys(nickname)
driver.find_element(By.CLASS_NAME, 'sc-cxpSdN.sc-llYSUQ.fqhoOa.tfvPv').click()

try:
    while(True):
        t = random.randrange(0, 2)
        soup = BeautifulSoup(driver.page_source, 'lxml')
        table = soup.select_one('.sc-bdvvtL.kGfETR')
        color_dict = {}
        for box in table.select('div'):
            if(box['color'] not in color_dict):
                color_dict[box['color']] = [box]
            else:
                color_dict[box['color']].append(box)
        for key in color_dict.keys():
            divs = color_dict[key]
            if(len(divs) == 1):
                class_name = '.'.join(color_dict[key][0]['class'])
                time.sleep(t)
                driver.find_element(By.CLASS_NAME, class_name).click()
                break
finally:
    time.sleep(15)
    driver.quit()
    print('end')
