from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://pl.wikipedia.org")
assert driver.title == "Wikipedia, wolna encyklopedia"

print(driver.find_element_by_css_selector(''))
