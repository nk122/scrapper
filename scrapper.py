#Neeraj.K.Rawat
#ROLL no.-CS19M009
#Scrapping of software clone from Github till 4 pages 
#importing required libraries
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
import time  # used for adding delay on next_page button
import pandas as pd # used pandas for creating dataframe and csv file

df=pd.DataFrame() #creating dataframe named df
driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://github.com/login") # directing to github url 
login=driver.find_element_by_id("login_field")
login.send_keys("nk134") #login through username
password = driver.find_element_by_id("password") #searching by id
password.send_keys("dummyscrape1!")# sending password
sign = driver.find_element_by_name("commit")
sign.click()# login click
search=driver.find_element_by_name("q")
search.send_keys("software clone")# topic to be searched for 
search.send_keys(Keys.ENTER)
#Creating list for storing information 
list=[] 
list2=[]



for i in range(1,5):
	if i>=2:
	
		time.sleep(10)#adding delay of 10 seconds	
			#path = driver.find_element_by_xpath("/html/body/div[4]/main/div/div[3]/div/div[2]/div/a["+str(i)+"]").click()
			
			#WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".next_page"))).click()
		for var in range(1,10):
			title = driver.find_element_by_xpath("/html/body/div[4]/main/div/div[3]/div/ul/li["+str(var)+"]/div[2]/div[1]/a")
			describ = driver.find_element_by_xpath("/html/body/div[4]/main/div/div[3]/div/ul/li["+str(var)+"]/div[2]/p")
			
			list.append(title.text)# adding titles to list
			list2.append(describ.text) #adding description to list2
			
		driver.find_element_by_css_selector('.next_page').click()						
	else:
		
		for var in range(1,10):

			title = driver.find_element_by_xpath("/html/body/div[4]/main/div/div[3]/div/ul/li["+str(var)+"]/div[2]/div[1]/a")
			describ = driver.find_element_by_xpath("/html/body/div[4]/main/div/div[3]/div/ul/li["+str(var)+"]/div[2]/p")
	
			list.append(title.text) # adding titles to list
			list2.append(describ.text)  #adding description to list2
			
	
	
	
#print(list)	

df[0]=list #writing in column 0
df[1]=list2 #writing in column 1
df.columns = ['Title','Description']# adding header to dataframe
df.to_csv("CS19M009.csv")#creating csv file named CS19M009.csv