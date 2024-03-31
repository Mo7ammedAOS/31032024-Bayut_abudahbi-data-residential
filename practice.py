from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wdw
from selenium.webdriver.support import expected_conditions as ec
import os
import time

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0'

# 1
path = os.path.join(os.getcwd(),'msedgedriver.exe')
driver = webdriver.Edge()
edge_service = Service(path)
edge_options = Options()
edge_options.add_argument(f'user-agent={user_agent}')
edge_options.add_experimental_option("detach",True)

browser = webdriver.Edge(service=edge_service,options=edge_options)
browser.get('https://www.bayut.com/for-sale/apartments/abu-dhabi/')
wdw(browser,10)
container_links =browser.find_elements(By.CLASS_NAME,'_287661cb')
edge_options.add_argument('headless')
browser = webdriver.Edge(service=edge_service,options=edge_options)
for link in container_links:
    plink = link.get_attribute('href')
    browser.get(plink)
    price = browser.find_element(By.CLASS_NAME,'_105b8a67').text
    location = browser.find_element(By.CLASS_NAME,'_1f0f1758').text 
    area = int(browser.find_element(By.XPATH,'//*[@id="body-wrapper"]/main/div[2]/div[4]/div[1]/div[3]/div[3]/span[2]/span/span').text.split(' ')[0].replace(',',''))
    print(price,'|||',location,'|||',area)

# print(container_link.get_attribute('href'))