def find_fcf(driver):    
    fcf = "Free cash flow = "
    fcf += driver.find_element_by_xpath('//*[@id="financials"]/table/tbody/tr[26]/td[8]').text + " "
    fcf += driver.find_element_by_xpath('//*[@id="financials"]/table/tbody/tr[26]/td[9]').text + " "
    fcf += driver.find_element_by_xpath('//*[@id="financials"]/table/tbody/tr[26]/td[10]').text
    return fcf