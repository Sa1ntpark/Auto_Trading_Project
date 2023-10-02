# -*- encoding: utf-8 -*-
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#테이블 데이터를 다룰 때는 pandas를 사용해준다.
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_countries_by_stock_market_capitalization'
tbl = pd.read_html(url)
print(tbl)
