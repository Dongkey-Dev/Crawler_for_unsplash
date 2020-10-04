#!/usr/bin/env python
# coding: utf-8

# In[30]:


import requests
from tqdm import tqdm as tq
import urllib.request as url
import re



def linkFetch(i):
    url = f"https://api.unsplash.com/search/collections?query=ball&page={i}&per_page=30&client_id=t7-iBWFbpX9ZHtB21jSIh2Q2RD230IaJzvwUfkpXD9g"   

    response = requests.get(url)
    data = response.json()
    return data

# response = requests.get(img_url)
# img = Image.open(BytesIO(response.content))
# img.show()

# path = 'H:/deepnatural/[고고리엔지니어링]크롤링/animal/'


# In[10]:


data = linkFetch(1)


# In[11]:


data['total']


# In[31]:


path = 'H:/deepnatural/[고고리엔지니어링]크롤링/ball/'
for j in tq(range(1, 201)) : 
    data = linkFetch(j)
    for i in data['results']:
        img_url = i['cover_photo']['urls']['raw']
        middle =str(img_url.split('/')[-1])
        middle = re.sub('[^a-zA-Z0-9]+', '', middle)
        file_name=middle + '.jpg'
        suffix = '&fm=jpg&cs=tinysrgb&w=1920&fit=max'
        img_url=img_url+suffix
    #     url.urlretrieve(img_url,path,file_name)
        response = requests.get(img_url)
        if response.status_code == 200 :
            with open(path + file_name,'wb') as f :
                f.write(response.content)


# In[13]:


data = linkFetch()


# In[6]:


def linkFetch2(i, name):
    url = f"https://api.unsplash.com/search/collections?query={name}&page={i}&per_page=30&client_id=t7-iBWFbpX9ZHtB21jSIh2Q2RD230IaJzvwUfkpXD9g"   

    response = requests.get(url)
    data = response.json()
    return data


# In[7]:


cnt = 1
while(True) :
    try : 
        linkFetch2(cnt, 'ball')
    except : 
        print(cnt)
        break
    finally : 
        cnt+=1


# In[8]:


linkFetch2(1, 'ball')['total']


# In[29]:


data['results'][10]['cover_photo']['urls']['raw']


# In[ ]:




