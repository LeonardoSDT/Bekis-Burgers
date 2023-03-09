# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import selenium.webdriver

from selenium.webdriver.common.by import By


# Create your tests here.

def register_test(self):
    options = selenium.webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')

    driver = selenium.webdriver.Chrome(chrome_options=options)
    driver.get('http://192.168.100.7:5085/register/')

    username = driver.find_element(By.ID, "id_username")
    username.send_keys("topauser")
    email = driver.find_element(By.ID, "id_email")
    email.send_keys("leotorokr@gmail.com")
    password1 = driver.find_element(By.ID, "id_password1")
    password1.send_keys("12345678")
    password2 = driver.find_element(By.ID, "id_password2")
    password2.send_keys("12345678")

    register_button = driver.find_element(By.ID, "btn-register")
    register_button.click()

    print(driver.title)
    driver.close()

def login_test(self):
    options = selenium.webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')

    driver = selenium.webdriver.Chrome(chrome_options=options)
    driver.get('http://192.168.100.7:5085/login/')

    username = driver.find_element(By.ID, "id_username")
    username.send_keys("topauser")
    password = driver.find_element(By.ID, "id_password")
    password.send_keys("12345678")

    login_button = driver.find_element(By.ID, "btn-login")
    login_button.click()

    print(driver.title)
    driver.close()