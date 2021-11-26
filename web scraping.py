import mysql.connector
cnx = mysql.connector.connect(user="root", password="1qaz!QAZ",host="127.0.0.1",database="product")
cursor = cnx.cursor()
import requests
from bs4 import BeautifulSoup
import re
kala=input("")
page=requests.get("https://www.digikala.com/search/?q=%s&sortby=22" %(kala))
soup=BeautifulSoup(page.content,"html.parser")
data=soup.find(class_="c-listing__items")
product=data.find_all(class_="c-product-box__title")
product1=[re.sub(r"\s+","",item.text).strip() for item in product]
price=data.find_all(class_="c-price__value-wrapper")
price1=[re.sub(r"\s+","",item1.text).strip() for item1 in price]
price_tag=list()
for item1 in price1:
    item1=''.join(item1.split('\u200c'))
    price_tag.append(item1)

for i in range(0,20): 
    cursor.execute("INSERT INTO product VALUES (\"%s\",\"%s\")" %(product1[i],price1[i])) 

cnx.commit()
