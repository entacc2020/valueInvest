from selenium import webdriver
from os import path
from selenium.webdriver.common.keys import Keys
import url
import time
driver = webdriver.Chrome()
file_name = url.company + ".txt"
f = open(file_name,'w')

def browse():   
    print("Processing " , url.company)
    driver.get(url.scrneer)
    company_search = driver.find_element_by_xpath('//*[@id="content-area"]/div/div/div/div/input')
    company_search.send_keys(url.company)
    company_search.send_keys(Keys.ENTER)
    time.sleep(4)
    market_cap = driver.find_element_by_xpath('//*[@id="content-area"]/section[1]/ul/li[1]').text
    stock_pe = driver.find_element_by_xpath('//*[@id="content-area"]/section[1]/ul/li[5]').text
    intrest = driver.find_element_by_xpath('//*[@id="profit-loss"]/div[3]/table/tbody/tr[6]/td[13]').text
    net_profit = driver.find_element_by_xpath('//*[@id="profit-loss"]/div[3]/table/tbody/tr[10]/td[13]').text
    intrest_coverage_ratio = net_profit + " / " + intrest
    price_by_book = driver.find_element_by_xpath('//*[@id="content-area"]/section[1]/ul/li[4]').text
    try:
        roe = driver.find_element_by_xpath('//*[@id="content-area"]/section[1]/ul/li[8]/b').text
    except:
        print("Return on Equity not found")
    
    print(market_cap,"\n" ,stock_pe,"\n",price_by_book,"\n" ,"Net profit: ",net_profit,"\n" ,"Intrest Coverage Ratio", intrest_coverage_ratio,"\n" ,"Return on Equity",roe,"\n" , file=f)
    
   


browse()
driver.close()