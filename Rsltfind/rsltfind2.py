from selenium import webdriver
from time import sleep
index = int(input("Enter Index number : "))
x=0
browser = webdriver.Chrome('chromedriver/chromedriver.exe')
browser.get("http://www.doenets.lk/result/alresult.jsf?")
print ("Opened URL")
while index <= 6535209 :
    browser.find_element_by_id('frm:username').clear()
    print(index)
    browser.find_element_by_id('frm:username').send_keys(str(index))
    browser.find_element_by_id('frm:btnSubmit').click()
    sleep(3)
    index = index + 1
