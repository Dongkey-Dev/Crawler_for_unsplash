#!/usr/bin/env python
# coding: utf-8
import requests
from tqdm import tqdm as tq
import urllib.request as url
import re

def linkFetch(search_query, i):
    url = f"https://api.unsplash.com/search/collections?query={search_query}&page={i}&per_page=30&client_id=t7-iBWFbpX9ZHtB21jSIh2Q2RD230IaJzvwUfkpXD9g"   

    response = requests.get(url)
    data = response.json()
    return data

path = f'{your_local_path}'
for j in tq(range(1, 201)) : 
    data = linkFetch(j)
    for i in data['results']:
        img_url = i['cover_photo']['urls']['raw']
        middle =str(img_url.split('/')[-1])
        middle = re.sub('[^a-zA-Z0-9]+', '', middle)
        file_name=middle + '.jpg'
        suffix = '&fm=jpg&cs=tinysrgb&w=1920&fit=max'
        img_url=img_url+suffix
        response = requests.get(img_url)
        if response.status_code == 200 :
            with open(path + file_name,'wb') as f :
                f.write(response.content)
