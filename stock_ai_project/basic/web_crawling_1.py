# cp949 codec으로 되어 있던것을 utf-8 로 변경한다. 이것을 통해 기존에 발생했던 오류 UnicodeEncodeError 해결
# -*- encoding: utf-8 -*-
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

import requests as rq

url  = 'https://quotes.toscrape.com/'
quote = rq.get(url) #GET 방식
quote.encoding = 'utf-8'

#quote <Response 200>

#quote.content: HTML 정보

from bs4 import BeautifulSoup

#HTML 요소에 접근하기 쉬운 BeautifulSoup 객체로 변경
quote_html = BeautifulSoup(quote.content, features = "html.parser") 
#print(quote_html)

#div 태그에서 class가 quote인 것에 접근
quote_div = quote_html.find_all('div', class_ = 'quote')
 

#### 명언 ####
# 1번째 하부에 span태그에 class가 text인것에 접근 
# -> 리스트 속 0번째 인덱스에 text 를 통해 text만 뽑아내기
text_1 = quote_div[0].find_all('span', class_ = 'text')[0].text

#list 속 for문을 통해 한번에 처리하기
quote_list_1 = [ i.find_all('span', class_ = 'text')[0].text for i in quote_div]

#find_all() 함수 대신에 select() 함수 이용하여 데이터 한번에 접근하기
quote_text = quote_html.select('div.quote > span.text')
quote_list_2 = [i.text for i in quote_text]

#print(quote_list_2)


#### 명언을 말한 사람 ####
quote_author = quote_html.select('div.quote > span > small.author')
quote_author_list = [i.text for i in quote_author]
#print(quote_author_list)


#### 명언을 말한 사람에 대한 정보 링크 ####
quote_link = quote_html.select('div.quote > span> a')

#인덱스0을 통해 리스트를 들어간 후, ['href']를 통해 링크 접근 가능
#print(quote_link[0]['href']) 

quote_link_list = [i['href'] for i in quote_link]
print(quote_link_list)
