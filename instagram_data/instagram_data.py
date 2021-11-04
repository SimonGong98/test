import requests
from bs4 import BeautifulSoup
import pymysql
from  selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time as time
import getpass
import urllib.request
import random
from time import sleep
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

insta_dict = {'id':[],
              'date': [],
              'like': [],
              'text': [],
              'hashtag':[]}

driver = webdriver.Chrome('/Users/ksjdo/Downloads/chromedriver')
driver.get("https://www.instagram.com/accounts/login/")
driver.maximize_window()

username = getpass.getpass("Input ID : ")# User ID
password = getpass.getpass("Input PWD : ")# User PWD
hashTag = input("Input HashTag # : ")# Search #HashTag

element_id = driver.find_element_by_name("username")
element_id.send_keys(username)
element_password = driver.find_element_by_name("password")
element_password.send_keys(password)

WebDriverWait(driver,timeout=5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.sqdOP.L3NKy.y3zKF')))
driver.find_element_by_css_selector('.sqdOP.L3NKy.y3zKF').click()
#EC must get tuple type. (())

sleep(2)

driver.get("https://www.instagram.com/explore/tags/{}/".format(hashTag))

WebDriverWait(driver,timeout=5).until(EC.presence_of_element_located((By.CLASS_NAME, 'eLAPa')))
first_post = driver.find_element_by_class_name('eLAPa')
first_post.click()

WebDriverWait(driver,timeout=5).until(EC.presence_of_element_located((By.CSS_SELECTOR, \
'body > div._2dDPU.QPGbb.CkGkG > div.EfHg9 > div > div > div.l8mY4 > button')))
