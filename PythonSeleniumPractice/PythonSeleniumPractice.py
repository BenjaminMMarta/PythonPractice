from selenium import webdriver
#from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://vuoriclothing.com/")

title = driver.title

driver.implicitly_wait(100000)

print(title)

driver.quit()