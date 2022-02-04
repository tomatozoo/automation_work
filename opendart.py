#import modules
from io import BytesIO
from zipfile import ZipFile
import urllib.request
import xml.etree.ElementTree
import pandas
import csv

# 임원 현황 페이지
# https://opendart.fss.or.kr/guide/detail.do?apiGrpCd=DS002&apiId=2019010

# open dart api key 설정
url = 'https://opendart.fss.or.kr/api/exctvSttus.xml?crtfc_key=c7513744819baa65157dde03ff7904a8bc1b4b0c?corp_code=00434456?bsns_year=2020?reprt_code=11013'
api_key = 'c7513744819baa65157dde03ff7904a8bc1b4b0c'
with urllib.request.urlopen(url) as zipresponse:
    with ZipFile(BytesIO(zipresponse.read())) as zipfile:
        zipfile.extractall('nm')

# DART에 공시된 회사 리스트

# https://opendart.fss.or.kr/api/exctvSttus.json	