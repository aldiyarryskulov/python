import requests
from bs4 import BeautifulSoup as bs

URL = 'https://kolesa.kz/cars/honda/civic/?auto-car-volume[from]=1.8&auto-car-volume[to]=2&year[from]=2007&year[to]=2008'

page = requests.get(URL)

soup = bs(page.content, 'html.parser')

def loop():
	title = each.find('span', attrs = {'a-el-info-title'}).text
	price = each.find('span', attrs = {'price'}).text
	date = each.find('span', attrs = {'date'}).text
	region = each.find('div', attrs = {'list-region'}).text
	region = region.replace(' ', '')
	title = title.replace(' ', '')
	price = price.replace(' ', '')
	date = date.replace(' ', '')
	print('_________________________________')
	print(title + price + '\t' + date + region)
	
for each in soup.find_all('div', attrs = {'row vw-item list-item a-elem'}):
	loop()

for each in soup.find_all('div', attrs = {'row vw-item list-item blue a-elem'}):
	loop()

