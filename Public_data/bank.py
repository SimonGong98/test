import xml.etree.ElementTree as ET
import requests
from lxml import html
from bs4 import BeautifulSoup
import pandas, json
import numpy as np
import os


url = "http://ecos.bok.or.kr/api/StatisticItemList/sample/xml/kr/1/1/028Y001/"
response = requests.get(url)
if response.status_code == 200:
    try:
        contents = response.text
        ecosRoot = ET.fromstring(contents)
        if ecosRoot[0].text[:4] in ("INFO","ERRO"):
            print(ecosRoot[0].text + " : " + ecosRoot[1].text)
        else:
            print(contents)
    except Exception as e:
        print(str(e))

url = "http://ecos.bok.or.kr/api/StatisticItemList/"
key="291U2JENZ8RVO5PTVUVT/"
word=["json/kr/1/1/", "xml/kr/19/19/"]
code="028Y001/MM/"
start="200601/"
end="202012/"
detail="BEEA472/"
params=url+key+word[0]+code+start+end+detail
#params='http://ecos.bok.or.kr/api/StatisticSearch/sample/json/kr/1/10/010Y002/MM/201101/201106/AAAA11/'
Url=requests.get(params)
#response=BeautifulSoup(Url.text.replace("</script\n", "</script>"), "html.parser")

#with open('asdf.txt', 'a+', encoding="UTF-8") as t:
#    t.write(Url.text)

#with open("asdf.txt") as fp:
#    soup = BeautifulSoup(fp, 'html.parser')

#for row in soup.findAll('row'):
#    print(row.time.text, row.data_value.text)


#Url_xml=BeautifulSoup(Url.text.encode('utf-8'),"html.parser")
Url_json=json.loads(Url.text)
raw_data=pandas.json_normalize(Url_json['StatisticItemList'],['row'])
raw_data

#http://ecos.bok.or.kr/api/StatisticSearch/sample/json/kr/1/10/010Y002/201101/201106/AAAA11/
#sample/xml/kr/1/1/043Y070/
#[BEEA425][연%] 010Y002/MM/QQ/YY/
