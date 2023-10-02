# -*- encoding: utf-8 -*-
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


import requests as rq
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/news/news_list.naver?mode=LSS2D&section_id=101&section_id2=258'
data = rq.get(url)
html = BeautifulSoup(data.content, 'html.parser')

html_select = html.select('dl > dd.articleSubject > a')
html_titles = [i['title'] for i in html_select]
print(html_titles)