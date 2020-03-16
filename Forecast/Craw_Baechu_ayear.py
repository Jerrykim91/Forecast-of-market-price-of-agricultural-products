# 크롤링_ 배추_1년
# 연도를 리스트에 담아서 원하는달만 픽 
# 2019년도로 진행 
# 2019-01-01 ~ 2019-12-31
# 총 12개의달 4번 분리 3*4 =12 
#---

#  크롤링 
from selenium import webdriver   # 웹드라이버 
from selenium.webdriver.common.keys import Keys
import urllib.request

# datetime 
from datetime import datetime
from datetime import timedelta

# 디렉터리 작업용 팩 
import shutil 
import win32com.client   # 이거 파일 확장자 변경시 필요 
# import win32com.client as win32

#  분석용 툴 
import pandas as pd
# import numpy as np
import time, os
#----
# 변수

# itemcategorycode 
# 채소류 : 200, 과일류 : 400
itemcategorycode = 200   
# itemcode : 품목 
# 무 : 231, 배추 : 211
itemcode = 211  
# kindcode : 품종(01, 02, 03, 06), 전체는 ''(공백)
kindcode = ""
# productrankcode : 상품 등급
productrankcode = 0
#----


date_list = [('2019-01-01', '2019-03-31'), ('2019-04-01', '2019-06-30'), ('2019-07-01', '2019-09-30'), ('2019-10-01', '2019-12-31')] 
print(date_list, len(date_list))

# # start_date, end_date
# for i,j in date_list:
#     start_date = i
#     end_date = j
#     print(start_date,type(start_date),end_date)

# 소매
# order_path = 'https://www.kamis.or.kr/customer/price/retail/period.do'
# 도매 
#---- 


# 드라이버옵션설정 
options = webdriver.ChromeOptions()

# options.add_argument('headless') 
options.add_argument("window-size=1920x1080")
# user-agent 
options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')  

# 1년 치 다운로드

for start_date, end_date in date_list:
    name = 'Baechu_wholesale'
    order_path = 'https://www.kamis.or.kr/customer/price/wholesale/period.do'
    action_path = f'?action=daily&startday={start_date}&endday={end_date}&countycode=&itemcategorycode={itemcategorycode}&itemcode={itemcode}&kindcode={kindcode}&productrankcode={productrankcode}&convert_kg_yn=N'

    url = order_path + action_path
    print(url)
    
    # 드라이버 가지고 오기 
    driver_path = '../data/webdriver/chromedriver.exe' 
    driver = webdriver.Chrome(driver_path, options=options)

    # 드라이버에 경로 전달
    driver.get(url)
    time.sleep(1)
    
    # 파일 저장
    xpath = "/html/body/div[1]/div/div[2]/section[3]/div/a"
    target = driver.find_element_by_xpath(xpath)
    target.click()
    time.sleep(3)
    driver.close() 
    
    # 파일 이름 변경
    Downloads_path = 'C:/Users/admin/Downloads/'
    path = 'C:/Forecast-of-market-price/data/input/'
    os.rename(f'{Downloads_path}가격정보.xls', f'{path}{start_date}_{name}.xls')
    time.sleep(1)
    
    # xls를 xlsx로 변경(에러때문)
    # 엑셀이 깔려 있어야 진행 가능
    excel = win32com.client.Dispatch("Excel.Application")
    path = path.replace('/','\\')
    # print(path)
    xlwb = excel.Workbooks.Open(f'{path}{start_date}_{name}.xls')
    xlwb.SaveAs(f'{path}{start_date}_{name}.xlsx', FileFormat = 51)
    xlwb.Close()
    excel.Quit()
    time.sleep(1)
    
    # 파일 삭제
    path = 'C:/Forecast-of-market-price/data/input/'
    os.remove(f'{path}{start_date}_{name}.xls')
    time.sleep(0.5)