from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv_obj=Service("Downloads")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://www.nytimes.com/international/section/us")
lines2= driver.find_element(By.XPATH,"/html/body/div/div[2]/main/section/div[2]/div/section/div[1]/ol/li[6]/div/div[1]/a/h2")
lines3 = driver.find_element(By.XPATH,"/html/body/div/div[2]/main/section/div[2]/div/section/div[1]/ol/li[5]/div/div[1]/a/div[2]/p")
lines = driver.find_element(By.XPATH,"/html/body/div/div[2]/main/section/div[2]/div/section/div[1]/ol/li[6]/div/div[1]/a/p")
print(lines.text)
print(lines2.text)
print(lines3.text)
