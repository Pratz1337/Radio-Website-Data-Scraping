import csv
from bs4 import BeautifulSoup
import requests

base_url = 'url you want to put'
page_num = 1
csv_file = 'radio_data.csv'

with open(csv_file, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow([ 'Radio Name', 'Country', 'Genres', 'Frequencies', 'Website'])

    while True:
        url = base_url.format(page_num)
        source = requests.get(url)
        soup = BeautifulSoup(source.text, 'html.parser')
        divs = soup.find('div', class_='radio-list')
        anchors = divs.find_all('a', class_='no-select')

        for anchor in anchors:
            href = anchor['href']
            url1 = f'{url}{href}'
            final = requests.get(url1)
            soup1 = BeautifulSoup(final.text, 'html.parser')
            div1 = soup1.find('div', class_='main-content')
            a = div1.find('a')
            country = a.text
            h1 = div1.find('h1')
            radio_name = h1.text
            div3 = div1.find('div', class_='contacts')
            try:
                if div3:
                    a1 = div3.find('a')
                    website = a1.attrs['href']
                else:
                    website = "N/A"
            except Exception as e:
                website = "N/A"

            div2 = div1.find('div', class_='genres')
            genres = div2.text.strip().split('\n') if div2 else ['N/A']
            div2 = div1.find('div', class_='frequencies')

            frequencies = []
            try:
                if div2:
                    li = div2.find_all('li')
                    for l in li:
                        frequency = l.text.strip().replace('\n', ' - ')
                        frequencies.append(frequency)
                else:
                    frequencies.append('N/A')
            except AttributeError:
                pass

            writer.writerow([ radio_name, country, ', '.join(genres), ', '.join(frequencies), website])

        page_num += 1
