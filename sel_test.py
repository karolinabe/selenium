from selenium import webdriver

# stworz obiekt chrome driver
driver = webdriver.Chrome()

# otworz strone Hello world z wikipedii
driver.get("https://pl.wikipedia.org/wiki/Hello_world")
