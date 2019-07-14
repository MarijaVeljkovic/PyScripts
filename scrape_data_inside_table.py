from bs4 import BeautifulSoup

soup = BeautifulSoup(open('sample.html'), 'lxml')

#print(soup.prittify())

for tr in soup.find_all('tr'):
	for td in tr.find_all('td'):
		print(td.text)