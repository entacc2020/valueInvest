from selenium import webdriver
from os import path
from selenium.webdriver.common.keys import Keys
import url
import time
driver = webdriver.Chrome(executable_path='chromedriver/chromedriver.exe')
f = open(url.company,'w')

def handle_error(driver ,xpath , i):
    try:
        get_op = driver.find_element_by_xpath(xpath).text + " "
        return get_op
    except:
        return 


def gross_margin(driver):
    op = "Grossprofit margin = "
    for i in range (1 , 10):
        xpath = "//*[@id=\"financials\"]/table/tbody/tr[4]/td["+ str(i) + "]"
        try:
            op += handle_error(driver , xpath ,i)
        except:
            continue
    return op


def operating_margin(driver):
    op = "Operating margin = "
    for i in range (1 , 10):
        xpath = "//*[@id=\"financials\"]/table/tbody/tr[8]/td[" + str(i) + "]"
        try:
            op += handle_error(driver , xpath ,i)
        except:
            continue 
    
    return op

def min_max(list_str):
    arr = list_str.split(" ")
    min_val =1223
    max_val = -1233
    for i in range (1, 13):
        try:
            number = float(arr[i])
            min_val = min(number, min_val)
            max_val = max(number , max_val)
        except:
            continue
    return "min = " + str(min_val) + " max = "+ str(max_val)
    


def find_fcf(driver):    
    fcf = "Free cash flow = "
    fcf += driver.find_element_by_xpath('//*[@id="financials"]/table/tbody/tr[26]/td[8]').text + " "
    fcf += driver.find_element_by_xpath('//*[@id="financials"]/table/tbody/tr[26]/td[9]').text + " "
    fcf += driver.find_element_by_xpath('//*[@id="financials"]/table/tbody/tr[26]/td[10]').text
    return fcf


def browse_ms(company):   
   
    driver.get(url.morningstar)
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="ctl00_ucHeader_txtQuote_txtAutoComplete"]').click()
    company_search = driver.find_element_by_xpath('//*[@id="ctl00_ucHeader_txtQuote_txtAutoComplete"]')
    company_search.send_keys(company)
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="ui-id-1"]/li[1]').click()
    driver.find_element_by_xpath('//*[@id="tabs"]/div/mds-button-group/div/slot/div/mds-button[2]/label/input').click()
    time.sleep(2)
    debt_equity ="Debt/Equity = " + str( driver.find_element_by_xpath('//*[@id="siteContent"]/div[2]/div/div/div[1]/div/div/div[2]/div/div[2]/div/div[2]/div[2]/div/div[2]/ul/li[8]/div/div[2]').text)
    
    driver.find_element_by_xpath('//*[@id="siteContent"]/div[2]/div/div/div[1]/div/div/div[2]/div/div[2]/div/div[2]/div[2]/div/div[2]/div[1]/a').click()
    time.sleep(4)
    driver.switch_to_window(driver.window_handles[1])

    fcf = find_fcf(driver) + "\n"
    operating_margin_str = operating_margin(driver) + "\n"
    range_opm = min_max(operating_margin_str) +"\n"
    gross_margin_str = gross_margin(driver) + "\n"
    range_gpm = min_max(gross_margin_str) + "\n"
    final_str =debt_equity + "\n" + operating_margin_str + range_opm +  gross_margin_str + range_gpm +  fcf 
    print(final_str) 
   


browse_ms(url.company)
driver.close()

