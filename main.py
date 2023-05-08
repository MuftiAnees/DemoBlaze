import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from colorama import Fore, Back, Style
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "C:\\Users\\mufti\\OneDrive\\Documents\\Github\\Selenium\\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.maximize_window()
driver.get("https://www.demoblaze.com/")
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Nexus 6")))
element.click()
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "btn.btn-success.btn-lg")))
element.click()
sleep(1)
alert = driver.switch_to.alert.accept()
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Cart")))
element.click()
sleep(2)
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "btn.btn-success.btn")))
element.click()
sleep(2)
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "name")))
element.send_keys("Anees")
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "country")))
element.send_keys("Pakistan")
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "city")))
element.send_keys("Islamabad")
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "card")))
element.send_keys("123123123123")
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "month")))
element.send_keys("12")
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "year")))
element.send_keys("2024")
sleep(1)
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR , "#orderModal > div > div > div.modal-footer > button.btn.btn-primary")))
element.click()
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "body > div.sweet-alert.showSweetAlert.visible > div.sa-button-container > div > button")))
sleep(2.5)