# request proxy imports
from http_request_randomizer.requests.proxy.requestProxy import RequestProxy
# selenium imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# set up proxies
req_proxy = RequestProxy() 
proxies = req_proxy.get_proxy_list()
us = [] #us is list of us based proxy
for proxy in proxies:
    if proxy.country == 'United States':
        us.append(proxy)
print(us[0].get_address())
print(us[0].country)
PROXY = us[0].get_address()


## check proxy
driver = webdriver.Chrome('./chromedriver.exe')
"""webdriver.DesiredCapabilities.CHROME['proxy']={
    "httpProxy":PROXY,
    "ftpProxy":PROXY,
    "sslProxy":PROXY,
    "proxyType":"MANUAL",
    
}
driver.get("https://vrbo.com")
search_bar = driver.find_element_by_id("react-destination-typeahead")
search_bar.clear()
search_bar.send_keys("San Diego, CA")
#driver.find_element_by_id("btn btn-primary").click()
driver.find_element(By.XPATH, '//*[@id="root"]/header/div[3]/div[2]/div/div/div[2]/div/div[2]/form/div/div[4]/button').click()"""