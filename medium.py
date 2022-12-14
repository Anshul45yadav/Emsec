from selenium import webdriver
import pandas as pd
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="Downloads\chromedriver_win32")
driver.get("https://medium.com/")
data = driver.page_source
alldata = ''.join(data)
soup = BeautifulSoup(alldata, 'html.parser')
Head = []
Para = []
Link = []
Content = []

A = soup.find_all('h2', class_='bv ii kk kl km kn ko kp kq kr ks kt ku kv kw kx ky kz la lb lc ld ct iv iw jd iy ja by')

C = driver.find_elements(By.XPATH, '/html/body/div/div/div/div/div/div/div/section/div/div/div/div/div/div/div/a')

for a in range(len(A)):
    Head.append(A[a].string)

for l in range(len(C)):
    Link.append(C[l].get_attribute('href'))

for o in Link:
    driver.get(o)
    ta = driver.page_source
    aldata = ''.join(ta)
    soup = BeautifulSoup(aldata, 'html.parser')
    D = soup.find_all('div', id="root")
    tem = ""
    for m in range(len(D)):
        tem += D[m].get_text()
    Content.append(tem)

print(len(Content))
print(len(Link))
print(len(Head))


w = pd.DataFrame({'Heading': Head, 'Link': Link, 'Content': Content})
w.to_csv('medium.csv', index=False)
print(w)