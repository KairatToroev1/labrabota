import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

def get_url(url):
    req = requests.get(url)
    return req.text

def writer(data):
    with open('electronic.csv', 'a') as file:
        write = csv.writer(file)
        return write.writerow((
            data['description'],
            data['deplink'],
            data['category']
        ))


def get_data(html, html1):
    soup = BeautifulSoup(html, 'html.parser')
    ads = soup.find('div', class_='list-view').find_all_next('div', class_='item')
    # url = 'https://www.kivano.kg'
    for ad in ads :
        try:
            description = ad.find('div', class_='listbox_title').text
        except:
            description = 'Нет описания'
        try:
            deplink = ad.find('div', class_='listbox_title').find('a').get('href')
        except:
            deplink = 'Нет такой ссылки'
        try:
            category = soup.find('div', class_= 'leftmenu-item').find('a').get('href')
        except:
            category = 'Нет такой категории'

        data = {
            'description': description,
            'deplink': html1 + deplink,
            'category': category
        }
        writer(data)
def hi(url):
    page_part = '?page='
    for i in range(1, 4):
        url_gen = url + page_part + str(i)
        html = get_url(url_gen)
        get_data(html, url)
def main():
    url = 'https://www.kivano.kg/elektronika'
    hi(url)
    url1 = 'https://www.kivano.kg/kompyutery'
    hi(url1)
    url2 = 'https://www.kivano.kg/bytovaya-tekhnika'
    hi(url2)
    url3 = 'https://www.kivano.kg/krasota-i-zdorove'
    hi(url3)


main()
