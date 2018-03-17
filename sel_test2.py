from selenium import webdriver


driver = webdriver.Chrome()

driver.get("https://www.microsoft.com/pl-pl/")

support_link = driver.find_element_by_id('l1_support')
support_link.click()


support_link2 = driver.find_element_by_link_text('Office')
support_link2.click()
