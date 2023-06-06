import requests
import re
from bs4 import BeautifulSoup

url = requests.get('https://webscraper.io/test-sites/e-commerce/allinone/phones')
soup = BeautifulSoup(url.text, 'html.parser')

# print(soup)

# 1. find()
# find_header = soup.find('header')
find_header = soup.header
# untuk mengambil atribut tambahkan .attrs
find_header_attrs = soup.header.attrs


find_div = soup.find('div', {'class':'container test-site'}).text
# print(find_div)

find_h4 = soup.find('h4', {'class':'pull-right price'})
find_h4_2 = soup.find('h4', class_ = 'pull-right price')
# print(find_h4)

# 2. find_all()
price = soup.find_all('h4', {'class':'pull-right price'})[6:]

# jika ingin mengambil salah satu, misal yang pertama [0]
# print(price[0])
title = soup.find_all('a', {'class':'title'})

review = soup.find_all('p', {'class':'pull-right'})
# print(price)

find_tag = soup.find_all(['h4','p','a'])
# print(find_tag)

find_id = soup.find_all(id = True) # mencari id
# print(find_id)

find_string = soup.find_all(string='Iphone')
# print(find_string)

# menggunakan re.compile & class_
find_string_2 = soup.find_all(string = re.compile('Nok'))
# print(find_string_2)
find_string_3 = soup.find_all(string = ['Iphone', 'Nokia 123'])
print(find_string_3)
find_pull = soup.find_all(class_ = re.compile('pull'))
# print(find_pull)
find_pull_2 = soup.find_all('p', class_ = re.compile('pull'))
# print(find_pull_2)
find_pull_3 = soup.find_all('p', class_ = re.compile('pull'), limit = 3)
# print(find_pull_3)


