from selenium import webdriver
from selenium.webdriver.common.by import By
import time

username = input("Enter your user name: ")
password = input("Enter your password: ")

driver = webdriver.Chrome()
driver.get("http://instagram.com")

time.sleep(5)

usernameTxt = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
passwordTxt = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')

usernameTxt.send_keys(username)
passwordTxt.send_keys(password)

time.sleep(2)

loginButton = driver.find_element(By.XPATH, '//button[@type="submit"]')

loginButton.click()
time.sleep(5)

driver.close()