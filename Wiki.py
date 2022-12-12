from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(executable_path="Downloads")
driver.get("https://en.wikipedia.org/wiki/India")
link=driver.find_elements(By.XPATH,'/html/body/div[3]/div[3]/div[5]/div[1]/p[2]/a')
Link=[]



for o in range(5):
    Link.append(link[o].get_attribute('href'))
   
    

Para=[]
Img=[]

for k in Link:
    driver.get(k)
    para=driver.find_elements(By.XPATH,'/html/body/div[3]/div[3]/div[5]/div[1]/p')
    img=driver.find_elements(By.XPATH,'//*[@id="mw-content-text"]/div/div/div/a/img')
    temdd = ""
    cemdd = ""
    for o in range(len(img)):
        temdd+=para[o].text
        cemdd+=img[o].get_attribute('src')
    Para.append(temdd)  
    Img.append(cemdd)

driver.quit()
w=pd.DataFrame({ 'Link':Link,'Img':Img,'Para':Para})
w.to_csv('wiki.csv',index=False)
print(w)         
     
       
      
        
    
    
        
    
