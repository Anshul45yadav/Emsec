
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
serv_obj=Service("Downloads")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://www.nytimes.com/section/technology")
heading= driver.find_elements(By.XPATH,"//*[@id='stream-panel']/div/ol/li/div/div/a/h2")
line = driver.find_elements(By.XPATH,"//*[@id='stream-panel']/div/ol/li/div/div/a/p")
author = driver.find_elements(By.XPATH,"//*[@id='stream-panel']/div/ol/li/div/div/a/div/p/span")
date = driver.find_elements(By.XPATH,"//*[@id='stream-panel']/div/ol/li/div/div/span")
Title =[]
Para =[]
Date=[]
Author=[]

  
for i in range(len(heading)):    
    Title.append(heading[i].text)
    Para.append(line[i].text)
    Date.append(date[i].text)
    Author.append(author[i].text)
driver.close 

a=pd.DataFrame({'Title':Title, 'Paragraph':Para ,'Date':Date,'Author':Author})
a.to_csv('text.csv',index=False)
print(a)

  

  
  





