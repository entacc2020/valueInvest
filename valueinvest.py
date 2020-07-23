from selenium import webdriver
import os 
from selenium.webdriver.common.keys import Keys
import url
import time

def error_handle(driver , xpath):
    try:
        scrapping_data = driver.find_element_by_xpath(xpath).text
        return scrapping_data
    except:
        return
        
def intrest_coverage_ratio_error_handle(net_profit , intrest):
    try:
       string_value =  net_profit + " / " + intrest
       return string_value
    except:
       return "NA"

  
     

def browse(company):  
    driver = webdriver.Chrome()
    print("Processing.. " , company) 
    driver.get(url.scrneer)
    time.sleep(2)
    try:
        company_search = driver.find_element_by_xpath('//*[@id="content-area"]/div/div/div/div/input')
        company_search.send_keys(company)
        company_search.send_keys(Keys.ENTER)
        company_search.send_keys(Keys.RETURN)
        time.sleep(2)
        company_name = error_handle(driver ,'//*[@id="company-info"]/h1' )
        market_cap = error_handle(driver ,'//*[@id="content-area"]/section[1]/ul/li[1]')
        stock_pe = error_handle(driver ,'//*[@id="content-area"]/section[1]/ul/li[5]')
        price_by_book = error_handle(driver ,'//*[@id="content-area"]/section[1]/ul/li[4]')
        intrest = error_handle(driver ,'//*[@id="profit-loss"]/div[3]/table/tbody/tr[6]/td[13]')
        net_profit = error_handle(driver ,'//*[@id="profit-loss"]/div[3]/table/tbody/tr[10]/td[13]')
        roe = error_handle(driver ,'//*[@id="content-area"]/section[1]/ul/li[8]/b')
            
        intrest_coverage_ratio = intrest_coverage_ratio_error_handle(net_profit , intrest)

        driver.close()
    
        f = open(company_name + ".txt",'w')
        print ( company_name, "\n",market_cap,"\n" ,stock_pe,"\n",price_by_book,"\n" ,"Net profit:",net_profit,"\n" ,"Intrest Coverage Ratio:", intrest_coverage_ratio,"\n" ,"Return on Equity:",roe,"\n" ,file = f)
        f.close()
        company_data = open(company_name + ".txt" , 'r')
        telegram_format = company_data.read()
        os.remove(company_name+".txt") 
        return telegram_format        
    except:
        driver.close()
        return "Cudunt retrive data, Please Check the spelling"