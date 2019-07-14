from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.PhantomJS(executable_path = r'C:\Users\Michael\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe')

url = 'https://stats.nba.com/players/list/'

driver.get(url)

#print(driver.page_source)

soup = BeautifulSoup(driver.page_source, 'lxml')

ul = soup.find('ul', class_ = 'players-list__names')

#print(ul)

for li in ul.find_all('li', class_ = 'players-list__names'):
	for a in li:
		print(a.text)

driver.quit()