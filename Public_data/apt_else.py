from lxml import html
from urllib.parse import urlencode, quote_plus, unquote
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import requests
import json
import pandas as pd
import PublicDataReader as pdr
import os
import pickle
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
import pickle
import seaborn as sns
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers


path = '/usr/share/fonts/truetype/nanum/NanumGothicEco.ttf'
font_name = fm.FontProperties(fname=path, size=10).get_name()

plt.rc('font', family=font_name)

fm._rebuild()

df=pd.read_pickle("/content/gdrive/Shareddrives/Altair/분당구.pkl")
df

df1=df.query('80<전용면적<90',engine='python')
df_apt=df1['아파트']
df_apt_dict={}
for i in df_apt:
  df_apt_dict['{}'.format(i)]=0
apt_name=list(df_apt_dict.keys())

def trading(start, end, df):
  df1=df.query('{0}<전용면적<{1}'.format(start, end),engine='python')
  df_apt=df1['아파트']
  df_apt_dict={}
  for i in df_apt:
    df_apt_dict['{}'.format(i)]=0
  apt_name=list(df_apt_dict.keys())

  df2_date=[]; df2_price=[]
  for i in apt_name:
    df2=df1.query('아파트.str.contains("{}")'.format(i),engine='python')
    df2_price.append(list(df2['거래금액']))
    df2_date.append(list(pd.to_datetime(df2['거래일']).astype(int)/ 10**9))
  trading=pd.DataFrame({'date':[df2_date_],'price':[df2_price]})
  return trading

  trading(80,100,df)

  years=[str(x) for x in range(2006,2021)]
day=[str(x) for x in range(1,13)]
days=[]; date=[]
for i in day:
  if len(i)==1:
    i='0'+i
    days.append(i)
  if '0' not in i:
    days.append(i)
for i in years:
  for j in days:
    date.append(i+j)

date1=[202001,202101]

item=[]
xmlUrl = 'http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcSHTrade'
My_API_Key = '+1nyiavwxqEmgF0X6kdfo6PB9BqSPkanWYpIUjiBIMhS2hLzqjQACi3JzkaxY90zft552sah5V3nuvSgqOAuJg=='

for x in date1:
  queryParams = '?' + urlencode(
      {
          quote_plus('ServiceKey') : My_API_Key,
          quote_plus('LAWD_CD') : '41135',
          quote_plus('DEAL_YMD') : '{}'.format(x)
      }
  )

  response = requests.get(xmlUrl + queryParams).text.encode('utf-8')
  xmlobj = bs4.BeautifulSoup(response, 'html.parser')
  item_list=xmlobj.findAll('items')
  item.append(item_list)

number=[0,4,6,8,10,12,13,16,18]
price1=[]; build_year1=[]; ground_area1=[]; place1=[]; area1=[]; M1=[]; D1=[]; A1=[]; code1=[]
vowel=[price1, build_year1, ground_area1, place1, area1, M1, D1, A1, code1]
price=[]; build_year=[]; ground_area=[]; place=[]; area=[]; M=[]; D=[]; A=[]; code=[]
a=['<', '거', '래', '금', '액', '>', ' ', '년', '대', '지', '면', '적','법', '정', '동','연', '면', '적','월','주', '택', '유', '형','지', '역', '코', '드']

for i in item:
  price1.append(i[0]); build_year1.append(i[4]); ground_area1.append(i[6])
  place1.append(i[8]); area1.append(i[10]); M1.append(i[12])
  D1.append(i[13]); A1.append(i[16]); code1.append(i[18])
for j in vowel[0]:
  j=''.join(x for x in j if x not in a)
  price.append(j)
for j in vowel[1]:
  j=''.join(x for x in j if x not in a)
  build_year.append(j)
for j in vowel[2]:
  j=''.join(x for x in j if x not in a)
  ground_area.append(j)
for j in vowel[3]:
  j=''.join(x for x in j if x not in a)
  place.append(j)
for j in vowel[3]:
  j=''.join(x for x in j if x not in a)
  area.append(j)
for j in vowel[4]:
  j=''.join(x for x in j if x not in a)
  M.append(j)
for j in vowel[5]:
  j=''.join(x for x in j if x not in a)
  D.append(j)
for j in vowel[6]:
  j=''.join(x for x in j if x not in a)
  A.append(j)
for j in vowel[7]:
  j=''.join(x for x in j if x not in a)
  code.append(j)

catalog=pd.DataFrame(data=Dict)

Dict={};
Dict['price']=price; Dict['build_year']=build_year; Dict['gound_area']=ground_area
Dict['place']=place; Dict['area']=area; Dict['M']=M; Dict['D']=D; Dict['A']=A; Dict['code']=code
for i in range(len(item)):
  for j in number:
    Dict['{}'.format(j)]=list(item[i][j])
    catalog=pd.DataFrame(Dict, columns=number)
  print(Dict)
#0:거래금액 4:건축년도 6:대지면적 8:법정동 10:연면적 12:월 13:일 16:다가구 18:지역코드

a=['<', '거', '래', '금', '액', '>', ' ', '년', '대', '지', '면', '적','법', '정', '동','연', '면', '적','월','주', '택', '유', '형','지', '역', '코', '드']
for i in price:
  i=''.join(x for x in i if x not in a)
