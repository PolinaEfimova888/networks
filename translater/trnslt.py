# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 03:26:55 2020

@author: polin
"""
import requests
import json

code = "82e622ccc27b4ad0af0918182329a742"
region = 'westeurope'

def extract(obj, arr, code):
    if isinstance(obj, dict):
        for k, v in obj.items():
            if isinstance(v, (dict, list)):
                extract(v, arr, code)
            elif k == code:
                arr.append(v)
    elif isinstance(obj, list):
        for item in obj:
            extract(item, arr, code)
    return arr

def translate(string, lg):
    json = [{'Text': string}]
    headers = {
        'Ocp-Apim-Subscription-code': code,
        'Ocp-Apim-Subscription-Region': region,
        'Content-Type': 'application/json'
    }

    url = "https://api.cognitive.microsofttranslator.com/translate?api-version=3.0&to=" + lg
    request = requests.post(url, headers=headers, json=json)
    values = extract(request.json(), [], 'text')
    return ''.join(values)


file = open("text.txt", "r", encoding="utf-8")
lg = input('Your language: ')
output = open("translate_text.txt", "a+")

for line in file.readlines(): 
    string = translate(line, lg)
    output.write(string)
print('done')
