from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()

driver.get("https://www.facebook.com")

name = driver.find_element_by_id('u_0_n')
name.send_keys('Phoebe')

surname = driver.find_element_by_id('u_0_p')
surname.send_keys('Buffay')

email = driver.find_element_by_id('u_0_s')
email.send_keys('smellycat@yahoo.com')

email2 = driver.find_element_by_id('u_0_v')
email2.send_keys('smellycat@yahoo.com')

password = driver.find_element_by_id('u_0_z')
password.send_keys('Smelly123')

birth_day = Select(driver.find_element_by_id('day'))
birth_day.select_by_index(3)

birth_month = Select(driver.find_element_by_id('month'))
birth_month.select_by_visible_text('lut')

birth_year = Select(driver.find_element_by_id('year'))
birth_year.select_by_value('1968')

sex = driver.find_element_by_id('u_0_b')
sex.click()
