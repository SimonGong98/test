import requests
from bs4 import BeautifulSoup
import pymysql
from  selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time as time
import getpass
import urllib.request
import random
from time import sleep
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


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

sleep(1.5)

driver.find_element_by_css_selector('.sqdOP.L3NKy.y3zKF').click()

sleep(3)

driver.get("https://www.instagram.com/explore/tags/{}/".format(hashTag))

insta_dict = {'id':[],
              'date': [],
              'like': [],
              'text': [],
              'hashtag':[]}

sleep(1.5)

first_post = driver.find_element_by_class_name('eLAPa')
first_post.click()

sleep(1.5)

seq = 0
start = time.time()

while True:
    # id 정보 수집
    try:
        info_id=driver.find_element_by_css_selector("div.e1e1d").text
        insta_dict['id'].append(info_id)
    except:
        info_id = driver.find_element_by_css_selector('div.C4VMK').text.split()[0]
        insta_dict['id'].append(info_id)


    # 시간정보 수집
    time_raw = driver.find_element_by_css_selector('time')
    time_info = pd.to_datetime(time_raw.get_attribute('datetime')).normalize()
    insta_dict['date'].append(time_info)

    # like 정보 수집
    try:
        driver.find_element_by_css_selector('a.zV_Nj')
        like = driver.find_element_by_css_selector('a.zV_Nj').text
        like=''.join([x for x in like.split()[1] if '개' not in x])
        insta_dict['like'].append(like)

    except:
        insta_dict['like'].append('영상')



    #text 정보수집
    raw_info = driver.find_element_by_css_selector('div.C4VMK').text.split()
    text = []
    for i in range(len(raw_info)):
        if i == 0:
            pass
        else:
            if '#' in raw_info[i]:
                pass
            else:
                text.append(raw_info[i])
    clean_text = ' '.join(text)
    insta_dict['text'].append(clean_text)

    #HashTag 수집
    raw_tags = driver.find_elements_by_css_selector('a.xil3i')
    hash_tag = []
    for i in range(len(raw_tags)):
        if raw_tags[i].text == '':
            pass
        else:
            hash_tag.append(raw_tags[i].text)

    insta_dict['hashtag'].append(hash_tag)

    seq += 1

    driver.find_element_by_css_selector(\
    "body > div._2dDPU.QPGbb.CkGkG > div.EfHg9 > div > div > div.l8mY4 > button").send_keys(Keys.ENTER)

    print('{}번째 수집'.format(seq), time.time() - start, sep = '\t')

    time.sleep(5)

    if seq == 3:
        print("수집 종료")
        break

### Reference: BK_Paul, https://data-marketing-bk.tistory.com/10?category=897751
