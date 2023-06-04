import requests
from bs4 import BeautifulSoup

url = requests.get('https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops')
soup = BeautifulSoup(url.text, 'html.parser')

# print(soup)

# 1. find()
# find_header = soup.find('header')
find_header = soup.header
# untuk mengambil atribut tambahkan .attrs
find_header_attrs = soup.header.attrs

find_div = soup.find('div', {'class':'container test-site'})

# find_h4 = soup.find('h4', {'class':'pull-right price'})
# find_h4 = soup.find('h4', class_ = 'pull-right price')
# print(find_h4)

# 2. find_all()
price = soup.find_all('h4', {'class':'pull-right price'})[6:]

# jika ingin mengambil salah satu, misal yang pertama [0]
# print(price[0])
title = soup.find_all('a', {'class':'title'})

review = soup.find_all('p', {'class':'pull-right'})
print(price)


