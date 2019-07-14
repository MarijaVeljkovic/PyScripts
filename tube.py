from selenium import webdriver
from bs4 import BeautifulSoup

driver = webdriver.PhantomJS(executable_path = r'C:\Users\Michael\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe')

url = 'https://www.tubegalore.com/'

driver.get(url)
soup = BeautifulSoup(driver.page_source, 'lxml')

ul = soup.find_all('span', class_ = 'thumb-image')
print(ul)