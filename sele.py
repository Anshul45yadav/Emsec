from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
serv_obj=Service("Downloads")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://www.nytimes.com/international/section/us")
lines = driver.find_element(By.CLASS_NAME,"css-1kv6qi")

print(lines.text)
