# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import selenium.webdriver

# Create your tests here.

options = selenium.webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')

driver = selenium.webdriver.Chrome(chrome_options=options)
driver.get('https://www.python.org/')
print(driver.title)
driver.close()