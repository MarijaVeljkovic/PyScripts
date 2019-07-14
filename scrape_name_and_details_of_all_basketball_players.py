from selenium import webdriver
from bs4 import BeautifulSoup

class Player():
	def __init__(self):
		self.name = ""
		self.link = ""


def get_player_list():		
	driver = webdriver.PhantomJS(executable_path = r'C:\Users\Michael\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe')

	url = 'https://stats.nba.com/players/list/'

	driver.get(url)

	#print(driver.page_source)

	soup = BeautifulSoup(driver.page_source, 'lxml')

	div = soup.find('div', class_ = 'large-10 columns')

	#print(div)

	for li in div.find_all('li'):
		for a in li:
			#print(a['href'])
			#print(a.text)
			new_player = Player()
			new_player.name = a.text
			new_player.link = a['href']
			player_list.append(new_player)

		for one_player in player_list:

			print(one_player.name)
			print(one_player.link)

	driver.quit()
	return player_list


get_player_list()