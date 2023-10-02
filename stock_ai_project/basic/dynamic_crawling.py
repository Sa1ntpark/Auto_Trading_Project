# -*- encoding: utf-8 -*-
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup

#크롬 브라우저의 버전을 탐색한 다음, 버전에 맞는 웹드라이버를 다운로드하여 해당 경로를 셀레니움에 전달
#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#driver = webdriver.Chrome(ChromeDriverManager().install())

#옛날에는 위의 주석 코드처럼 해야했으나, 셀레니움이 업데이트 되어 필요 없음
#ChromeDriverManager가 필요없음
driver = webdriver.Chrome()

#해당 주소로 이동
url = 'https://www.naver.com'
driver.get(url)
time.sleep(2)

#해당 페이지 html 정보 
#print(driver.page_source)

#경제 버튼 클릭
# print("경제 element = ")
# print(driver.find_element(By.LINK_TEXT, value = '경제'))
# print("#############")
# driver.find_element(By.LINK_TEXT, value = '경제').click()

#뉴스 아이콘 클릭
#driver.find_element(By.CLASS_NAME, value = 'type_news').click()

#뒤로 가기
#driver.back()

#특정 검색어 검색하기
driver.find_element(By.CLASS_NAME, value = 'search_input').send_keys('파이썬')
driver.find_element(By.CLASS_NAME, value = 'ico_btn_search').click()


#기존 검색어 지운 후 새로운 단어 입력하고 검색버튼 클릭
# time.sleep(1) #로딩 대기
# driver.find_element(By.CLASS_NAME, value = 'box_window').clear()
# driver.find_element(By.CLASS_NAME, value = 'box_window').send_keys('c++')
# driver.find_element(By.CLASS_NAME, value = 'bt_search').click()

#XPATH: HTML이나 XML중 특정 값의 태그나 속성을 찾기 쉽게 만든 주소
# time.sleep(1)
# driver.find_element(By.XPATH, value = '//*[@id="lnb"]/div[1]/div/ul/li[5]/a').click()


#페이지 다운
#execute_script를 통해 js 명령어 실행
#화면 하단 끝까지 scroll
driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
#아래 코드도 가능
#driver.find_element(By.TAG_NAME, value = 'body').send_keys(Keys.PAGE_DOWN)

#페이지 끝까지 아래로 스크롤
# prev_height = driver.execute_script('return document.body.scrollHeight')

# while True:
#     driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
#     time.sleep(2) #로딩대기
#     current_height = driver.execute_script('return document.body.scrollHeight')
#     if current_height == prev_height:
#         break
#     prev_height = current_height


#페이지 꺼짐 방지
a = True
while (a):
    b = input("break: ")
    if (b == "break"):
        a = False

