import requests
from bs4 import BeautifulSoup


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

    try:
        info = soup.find('', class_='').text.strip()
    except:
        info = 'не нашел'
    data = {'date': date, 'info': info, 'items': items}
    return data
    



def write_to_csv(data):
    import csv
    with open('mchss.csv','w', encoding='utf-8') as file:
        # fieldnames = ['date', 'info', 'items']
        writer = csv.writer(file)
        writer.writerow( (data['date'], data['info'], data['items']))
        print(data)
        

def main():
    all_links = get_html(MAIN_URL)
    for i in all_links:
        html = get_html(MAIN_URL)
        s = get_new_info(html)
        print(s)
        write_to_csv(s)   

if __name__ == '__main__':
    main()