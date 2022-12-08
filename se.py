from bs4 import BeautifulSoup
from selenium import webdriver
driver = webdriver.Chrome(executable_path="Downloads")
driver.get("https://www.nytimes.com/international/section/us")
Data = driver.page_source
allData = ''.join(Data)
soup = BeautifulSoup(allData,'html.parser')
arrhead=[]
soup=BeautifulSoup(allData,'html.parser')
for d in soup.find_all('div',id='app'):
    title=d.find_all('h2')
for u in range(len(title)):
    arrhead.append(title[u].text)
print("this is heading",arrhead[4])











