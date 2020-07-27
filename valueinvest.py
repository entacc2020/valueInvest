from selenium import webdriver
from os import path
from selenium.webdriver.common.keys import Keys
import url
import time
import util
driver = webdriver.Chrome(executable_path='chromedriver/chromedriver.exe')
f = open(url.company + ".txt",'a+')

 
def browse_ms(company):   
    print("Morning star")
   
    driver.get(url.morningstar)
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="ctl00_ucHeader_txtQuote_txtAutoComplete"]').click()
    company_search = driver.find_element_by_xpath('//*[@id="ctl00_ucHeader_txtQuote_txtAutoComplete"]')
    company_search.send_keys(company)
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="ui-id-1"]/li[1]').click()
    time.sleep(4)
    driver.find_element_by_xpath('//*[@id="tabs"]/div/mds-button-group/div/slot/div/mds-button[2]/label/input').click()
    time.sleep(4)
    debt_equity ="Debt/Equity = " + str( driver.find_element_by_xpath('//*[@id="siteContent"]/div[2]/div/div/div[1]/div/div/div[2]/div/div[2]/div/div[2]/div[2]/div/div[2]/ul/li[8]/div/div[2]').text)
    
    driver.find_element_by_xpath('//*[@id="siteContent"]/div[2]/div/div/div[1]/div/div/div[2]/div/div[2]/div/div[2]/div[2]/div/div[2]/div[1]/a').click()
    time.sleep(4)
    driver.switch_to_window(driver.window_handles[1])

    fcf = util.find_fcf(driver) + "\n"
    operating_margin_str = util.operating_margin(driver) + "\n"
    range_opm = util.min_max(operating_margin_str) +"\n"
    gross_margin_str = util.gross_margin(driver) + "\n"
    range_gpm = util.min_max(gross_margin_str) + "\n"
    final_str =debt_equity + "\n" + operating_margin_str + range_opm +  gross_margin_str + range_gpm +  fcf 
    print(final_str) 
    print(final_str , file=f)

def intrest_coverage_ratio_error_handle(net_profit , intrest):
    # try:
    #    string_value =  net_profit + " / " + intrest
    #    return string_value
    # except:
    return "NA"

    

def browse(company):  
    print("Processing.. Scrapping Scrneer " , company) 
    driver.get(url.scrneer)
    time.sleep(2)
    #try:
    company_search = driver.find_element_by_xpath('//*[@id="content-area"]/div/div/div/div/input')
    company_search.send_keys(company)
    time.sleep(1)
    company_search.send_keys(Keys.ENTER)

    #company_search.send_keys(Keys.RETURN)
    time.sleep(2)
    company_name = util.error_handle(driver ,'//*[@id="company-info"]/h1' )
    market_cap = util.error_handle(driver ,'//*[@id="content-area"]/section[1]/ul/li[1]')
    stock_pe = util.error_handle(driver ,'//*[@id="content-area"]/section[1]/ul/li[5]')
    price_by_book = util.error_handle(driver ,'//*[@id="content-area"]/section[1]/ul/li[4]')
    intrest = util.error_handle(driver ,'//*[@id="profit-loss"]/div[3]/table/tbody/tr[6]/td[13]')
    net_profit = util.net_profit_fun(driver)
    roe = util.error_handle(driver ,'//*[@id="content-area"]/section[1]/ul/li[8]/b')
            
    intrest_coverage_ratio = intrest_coverage_ratio_error_handle(net_profit , intrest)

    print ( company_name, "\n",market_cap,"\n" ,stock_pe,"\n",price_by_book,"\n" ,"Net profit:",net_profit,"\n" ,"Intrest Coverage Ratio:", intrest_coverage_ratio,"\n" ,"Return on Equity:",roe,"\n" )
    final_str = company_name+ "\n"+market_cap+"\n" +stock_pe+"\n"+ price_by_book+ "\n" + "Net profit:"+ net_profit+ "\n" + "Intrest Coverage Ratio:"+  intrest_coverage_ratio+ "\n" + "Return on Equity:"+ roe+ "\n"
    print(browse_ms(company_name))
    return final_str    
    #except:
        # driver.close()
        # #return "Cudunt retrive data, Please Check the spelling"

#

print(browse(url.company))

