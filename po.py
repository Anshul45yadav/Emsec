import requests
from bs4 import BeautifulSoup
r = requests.get('https://www.aakash.ac.in/')
print (r)
soup = BeautifulSoup(r.content,'html.parser')

g = soup.find('div',class_="aakash-advantages-block")

con = g.find_all('h5')
co = g.find_all('p')
print(con)
print(co[3].text)
   


