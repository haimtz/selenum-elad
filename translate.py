import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('chromedriver.exe')
try:
    driver.get('https://translate.google.co.il/')
    time.sleep(5)

    source = driver.find_element_by_id('source')
    source.clear()
    source.send_keys('Whats up?')
    time.sleep(5)

    target = driver.find_element_by_css_selector('.tlid-translation.translation')
    result = target.text
    print(result)
    time.sleep(5)


except Exception as error:
    print(error)
finally:
    driver.close()
    print('finish')
