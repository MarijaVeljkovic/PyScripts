from selenium import webdriver

#driver = webdriver.Chrome(executable_path= r'C:\Users\Michael\chromedriver_win32\chromedriver.exe')

driver = webdriver.PhantomJS(executable_path = r'C:\Users\Michael\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe')

driver.get('http://python.org')

html_doc = driver.page_source

print (html_doc)