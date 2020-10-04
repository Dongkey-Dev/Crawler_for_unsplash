#!/usr/bin/env python
# coding: utf-8

# In[136]:


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


# In[137]:


options = webdriver.ChromeOptions()
# options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
options.add_argument("lang=ko_KR") 
driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=options)


# In[138]:


driver.get('https://unsplash.com/s/photos/object')


# In[25]:


i=1
while (True) :
    driver.execute_script(f'window.scrollTo(0,{i})')
    i+=100


# In[42]:


html = driver.page_source


# In[43]:


s = bs(html, 'html.parser')


# In[22]:


#app > div > div:nth-child(3) > div:nth-child(3) > div > div:nth-child(1) > div > div > div:nth-child(1) > div:nth-child(1) > figure > div > div._3A74U > div
#app > div > div:nth-child(3) > div:nth-child(3) > div > div:nth-child(1) > div > div > div:nth-child(2) > div:nth-child(1) > figure > div > div._3A74U > div
#app > div > div:nth-child(3) > div:nth-child(3) > div > div:nth-child(1) > div > div > div:nth-child(3) > div:nth-child(1) > figure > div > div._3A74U > div

#app > div > div:nth-child(3) > div:nth-child(3) > div > div:nth-child(1) > div > div > div:nth-child(1) > div:nth-child(3) > figure > div > div._3A74U > div
#app > div > div:nth-child(3) > div:nth-child(3) > div > div:nth-child(1) > div > div > div:nth-child(2) > div:nth-child(3) > figure > div > div._3A74U > div

#app > div > div:nth-child(3) > div:nth-child(3) > div > div:nth-child(1) > div > div > div:nth-child(2) > div:nth-child(227) > figure > div > div._3A74U > div

driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')


# In[29]:


new_height = driver.execute_script("return document.body.scrollHeight")


# In[30]:


new_height


# In[28]:


for i in reversed(range(0,5403)) :
    driver.execute_script(f'window.scrollTo(0,{i});')


# In[36]:


driver.execute_script(f'window.scrollTo(0,5000);')


# In[77]:


#app > div > div:nth-child(3) > div:nth-child(3) > div > div:nth-child(1) > div > div > div:nth-child(1) > div:nth-child(1) > figure > div > div._3A74U > div > div > a

#Answer : '#app > div > div:nth-of-type(2) > div:nth-of-type(3) > div > div:nth-of-type(1) > div > div > div:nth-of-type({i(1~3)}) > div:nth-of-type({j(1~320)}) > figure > div > div:nth-of-type(1) > div'
i= 1
resource = []
while (True) : 
    html = driver.page_source
    s = bs(html, 'html.parser')
    try :
        resource.append(s.select(f'#app > div > div:nth-of-type(2) > div:nth-of-type(3) > div > div:nth-of-type(1) > div > div > div:nth-of-type(1) > div:nth-of-type({i}) > figure > div > div > div > div > a')[0]['href'])
        resource.append(s.select(f'#app > div > div:nth-of-type(2) > div:nth-of-type(3) > div > div:nth-of-type(1) > div > div > div:nth-of-type(2) > div:nth-of-type({i}) > figure > div > div > div > div > a')[0]['href'])
        resource.append(s.select(f'#app > div > div:nth-of-type(2) > div:nth-of-type(3) > div > div:nth-of-type(1) > div > div > div:nth-of-type(3) > div:nth-of-type({i}) > figure > div > div > div > div > a')[0]['href'])
    except : 
        print(i)
        break
#         driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
#         time.sleep(5)
    else : 
        i+=1        


# In[139]:


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
#             driver.execute_script('window.scrollTo(0,document.body.scrollHeight);')
#         time.sleep(5)
    else : 
        i+=1 
        
        #app > div > div:nth-child(3) > div:nth-child(3) > div > div:nth-child(1) > div > div > div:nth-child(3) > div:nth-child(383)
        #app > div > div:nth-child(3) > div:nth-child(3) > div > div:nth-child(1) > div > div > div:nth-child(2) > div:nth-child(366)
        #app > div > div:nth-child(3) > div:nth-child(3) > div > div:nth-child(1) > div > div > div:nth-child(1) > div:nth-child(372)


# In[114]:


# driver.find_element_by_css_selector('#app > div > div:nth-child(3) > div:nth-child(3) > div > div:nth-child(1) > div > div > div:nth-child(3) > div:nth-child(13) > figure > div > div._3A74U > div')
driver.find_element_by_css_selector('#app > div > div:nth-child(3) > div:nth-child(3) > div > div:nth-child(1) > div > div > div:nth-child(1) > div:nth-child(1) > figure > div > div._3A74U > a > div')


# In[145]:


resource[0]


# In[111]:


source = []

for i in range(1,320) : 
    for j in range(1,4) : 
        try :
            source.append(driver.find_element_by_css_selector(f'#app > div > div:nth-child(3) > div:nth-child(3) > div > div:nth-child(1) > div > div > div:nth-child({j}) > div:nth-child({i}) > figure > div > div._3A74U > a > div'))
        except : 
            continue
            
len(source)
    


# In[90]:


driver.get(source[0])


# In[93]:


driver.find_element_by_css_selector('#popover-download-button > div:nth-child(1) > button > svg').click()


# In[ ]:





# In[157]:



download_dir = 'H:/deepnatural/[고고리엔지니어링]크롤링/object/'
j=1
for t in tq(resource) : 
    driver.get(t)
    driver.find_element_by_css_selector('#popover-download-button').click()
    html = driver.page_source
    s = bs(html, 'html.parser')
    for i in range(4) :
        try :
            img_size = list(map(int, s.select('#popover-download-button > div:nth-of-type(2) > div > ul:nth-of-type(1) > li > a > span')[i].text[1:-1].split('x')))
            check = [ i>=1920 for i in img_size ]
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


# In[101]:


s.select('#popover-download-button > div:nth-of-type(2) > div > ul:nth-of-type(1) > li:nth-of-type(2) > a')[0]['href']


# In[103]:


source = list(map(int, s.select('#popover-download-button > div:nth-of-type(2) > div > ul:nth-of-type(1) > li > a > span')[1].text[1:-1].split('x')))


# In[105]:


check = [ i>=1920 for i in source ]
check


# In[71]:


list(map(int, s.select('#popover-download-button > div:nth-of-type(2) > div > ul:nth-of-type(1) > li > a > span')[1].text[1:-1].split('x')))


# In[ ]:




