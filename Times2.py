from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path="Downloads")
driver.get("https://timesofindia.indiatimes.com/explainers/health")
heading=driver.find_elements(By.XPATH,'//*[@id="app"]/div/div/div/div/div/div/div/div/div/ul/li/a/div/h5')
link =driver.find_elements(By.XPATH,'//*[@id="app"]/div/div[5]/div/div[2]/div/div/div/div[1]/div[2]/ul/li/a')
img =driver.find_elements(By.XPATH,'//*[@id="app"]/div/div/div/div/div/div/div/div/div/ul/li/a/div/img')
Head=[]
Link=[]
Img=[]
for o in range(5):
    Link.append(link[o].get_attribute('href'))
    Img.append(img[o].get_attribute('src'))
    Head.append(heading[o].text)
print(Head)

Paras=[]

for lnk in Link:
    driver.get(lnk)
    para=driver.find_elements(By.CLASS_NAME,'readmore_span')
    temdd = ""

    for o in range(len(para)):
        temdd+=para[o].text
    Paras.append(temdd)  
print(Paras)    
     

driver.quit()


p=pd.DataFrame({ 'Heading':Head,'Img':Img,'Link':Link,'Para':Paras})
p.to_csv('times2links.csv',index=False)
print(p)





