# -*- encoding: utf-8 -*-
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

import requests as rq
from bs4 import BeautifulSoup
import pandas as pd

#Headers 부분에 Request URL
url = 'https://kind.krx.co.kr/disclosure/todaydisclosure.do'

#값이 없는 항목은 입력 안해도 된다.
payload = {
    'method': 'searchTodayDisclosureSub',
    'currentPageSize': '15',
    'pageIndex': '1',
    'orderMode': '0',
    'orderStat': 'D',
    'forward': 'todaydisclosure_sub', 
    'chose': 'S',
    'todayFlag': 'N',
    'selDate': '2023-08-30'
}

data = rq.post(url, data = payload)
html = BeautifulSoup(data.content, 'html.parser')

#BeautifulSoup 에서 파싱한 파서트리를 prettify()함수를 통해
#다시 유니코드 형태로 돌려줍니다.
html_unicode = html.prettify()

tbl = pd.read_html(html_unicode)
print(tbl)