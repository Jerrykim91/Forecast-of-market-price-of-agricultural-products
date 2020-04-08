# 크롤링 툴 
# !pip install selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 시간 툴
import time
from datetime import datetime
from datetime import timedelta

# 분석 툴 
import pandas as pd
import numpy as np


# 드라이버 생성 
options = webdriver.ChromeOptions()

# options.add_argument('headless') 
options.add_argument("window-size=1920x1080")
options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')  # user-agen


def make_date(date): # date

    year = str(date.year)
    # month
    if date.month >= 10:
        month = str(date.month)
    else:
        month = "0" + str(date.month)
    # day
    if date.day >= 10 :
        day = str(date.day)
    else:
        day = "0" + str(date.day)
    
    # hour
    hour = str(date.hour)

    f_date = year + "." + month + "." + day + "." + hour + ":00"
    return f_date


start = time.time()

# 드라이버 가지고 오기 
driver_path = './data/webdriver/chromedriver.exe' 
driver = webdriver.Chrome(driver_path, options=options )

driver.get('https://www.weather.go.kr/w/weather/now.do')
time.sleep(1)

xpath = '//*[@id="sfc-city-weather"]/div[1]/div/div/label'
target = driver.find_element_by_xpath(xpath)
target.click()

time.sleep(1)
# driver.close() 

#  여기서부터 뭐가 뭐를 뜻하는지 모르겠다. 

class_name1 = driver.find_element_by_class_name('sub-select-wrap')
class_name2 = class_name1.find_element_by_class_name('time')
class_name3 = class_name2.find_element_by_tag_name('input')

text = "2020.01.01.14:00" # 시간 입력 란에 들어가는 거 
class_name3.clear()
class_name3.send_keys(text)
class_name3.send_keys(Keys.RETURN)
time.sleep(0.5)

# 

need = [1, 5, 6, 7, 8, 10, 11, 12, 13] 
fli =list()
xpath = '//*[@id="sfc-city-weather"]/div[3]/div/div[2]/div/table/tbody/tr[16]'
target_q = driver.find_element_by_xpath(xpath)
xpath_q_2 = target_q.find_elements_by_tag_name('td')

for i in need:
    print(xpath_q_2[i].text)


time.sleep(1)
text = "2010.01.01.14:00"
class_name3.clear()
class_name3.send_keys(text)
class_name3.send_keys(Keys.RETURN)


xpath = '//*[@id="sfc-city-weather"]/div[3]/div/div[2]/div/table/tbody/tr[16]'
q1= driver.find_element_by_xpath(xpath)
q2 = q1.find_elements_by_tag_name('td')
for i in range(len(q2)):
    print(q2[i].text)