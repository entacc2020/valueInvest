from selenium import webdriver
from os import path
from selenium.webdriver.common.keys import Keys
import url
import time
driver = webdriver.Chrome()
f = open(url.company,'w')

def browse():   
   
    driver.get(url.morningstar)
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="ctl00_ucHeader_txtQuote_txtAutoComplete"]').click()
    company_search = driver.find_element_by_xpath('//*[@id="ctl00_ucHeader_txtQuote_txtAutoComplete"]')
    company_search.send_keys(url.company)
    time.sleep(2)
    driver_click = driver.find_element_by_xpath('//*[@id="ui-id-53"]/div/div[2]').click()
    #driver_click.click()
    time.sleep(4)
   
    
   


browse()
driver.close()