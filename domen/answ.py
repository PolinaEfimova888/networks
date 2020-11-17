# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 19:22:03 2020

@author: polin
"""
import json
import requests
import pandas as pd

data = pd.read_csv('list')

from urllib.parse import urlparse

urls, domains = [], []
for url in data.urls:
    if type(url) == str and 'https' in url:
        urls.append(url)
        domains.append(urlparse(url).netloc)

domains = set(domains)

def get_json(domain):
    response = requests.get('http://api.whois.vu/?q='+domain)
    bytes_data = response.content
    json_data = bytes_data.decode('utf8')
    data = json.loads(json_data)
    return data

def get_answ(domains):

    answ = []
    answer = open('answer.txt', 'w')
    for domain in domains:
        data = get_json(domain)
        if data['available'] == 'yes':
            answ.append(data['domain'])
            answer.write(data['domain']+'\n')
        if len(answ)==20:
            answer.close()
            return answ

print(get_answ(domains))
