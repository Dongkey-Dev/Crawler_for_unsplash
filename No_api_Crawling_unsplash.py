#!/usr/bin/env python
# coding: utf-8
import sys
import pandas as pd 
import numpy as np 
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager 
import openpyxl
import xlrd
from tqdm import tqdm as tq
import time
import requests

options = webdriver.ChromeOptions()
# options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
options.add_argument("lang=ko_KR") 
driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=options)

driver.get(f'https://unsplash.com/s/photos/{query}') 

resource = []
i= 1
j = [s for s in range(2000,180000, 1500)]
k=j[0]
cnt=1
while (True) : 
    html = driver.page_source
    s = bs(html, 'html.parser')
    try :
        resource.append(s.select(f'#app > div > div:nth-of-type(2) > div:nth-of-type(3) > div > div:nth-of-type(1) > div > div > div:nth-of-type(1) > div:nth-of-type({i}) > figure > div > div > div > div > a')[0]['href'])
        resource.append(s.select(f'#app > div > div:nth-of-type(2) > div:nth-of-type(3) > div > div:nth-of-type(1) > div > div > div:nth-of-type(2) > div:nth-of-type({i}) > figure > div > div > div > div > a')[0]['href'])
        resource.append(s.select(f'#app > div > div:nth-of-type(2) > div:nth-of-type(3) > div > div:nth-of-type(1) > div > div > div:nth-of-type(3) > div:nth-of-type({i}) > figure > div > div > div > div > a')[0]['href'])
    except : 
        print(i)
        while(True) : 
            driver.execute_script(f'window.scrollTo(0,{k});')
            k+=20
            if k == j[cnt] : 
                cnt+=1
                break
    else : 
        i+=1 

driver.find_element_by_css_selector('#popover-download-button > div:nth-child(1) > button > svg').click()


download_dir = f'{your_local_path}'
j=1
for t in tq(resource) : 
    driver.get(t)
    driver.find_element_by_css_selector('#popover-download-button').click()
    html = driver.page_source
    s = bs(html, 'html.parser')
    for i in range(4) :
        try :
            img_size = list(map(int, s.select('#popover-download-button > div:nth-of-type(2) > div > ul:nth-of-type(1) > li > a > span')[i].text[1:-1].split('x')))
            check = [ i>=1920 for i in img_size ] #download only over 1920 pixel(w or h)
            if any(check) : 
                url = s.select(f'#popover-download-button > div:nth-of-type(2) > div > ul:nth-of-type(1) > li:nth-of-type({i+1}) > a')[0]['href']
                response = requests.get(url)
                if response.status_code == 200 :
                    with open(download_dir + f'object_{j}.jpg','wb') as f :
                        f.write(response.content)
                        j+=1
                        break
            else : 
                continue
        except : 
            break
