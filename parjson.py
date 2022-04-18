import requests
from bs4 import BeautifulSoup
import json

MAIN_URL = 'https://mchs.gov.kg/ru/'
HEADERS = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36" 


def get_html(url):
    heders = {'heders': HEADERS}
    res = requests.get(url)
    return res.text


def get_new_info(html):
    soup = BeautifulSoup(html, 'lxml')
    try:
        items = soup.find('div', id='primary').text.strip() 
    except:
        items = ''
    try:
        date = soup.find('div', class_='date-in-header').text.strip()
    except:
        date = 'не нашел'
    
    data = {'date': date,  'items': items}
    return data
    



def write_to_csv(data):
    with open('mchss.json','w', encoding='utf-8') as file:
        json.dump((data['date'],data['items']), file, indent=3, ensure_ascii=False)
          
        

def main():
    all_links = get_html(MAIN_URL)
    for i in all_links:
        html = get_html(MAIN_URL)
        s = get_new_info(html)
        print(s)
        write_to_csv(s)   

if __name__ == '__main__':
    main()