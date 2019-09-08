#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

site = "https://texnique.xyz/"

#open driver
driver = webdriver.Firefox()
driver.get(site)

#start game
driver.find_element(By.XPATH, '//*[@id="start-button"]').click()
time.sleep(2)

def solve():
  result = driver.find_element(By.XPATH, '/html/body/main/div/div[3]/div[2]').text.split("\n")[0]
  print result
  
  textbox = driver.find_element(By.XPATH, '//*[@id="user-input"]')
  textbox.clear()
  textbox.send_keys(result)

while True:
  try:
    solve()
  except:
    pass
  time.sleep(1)
