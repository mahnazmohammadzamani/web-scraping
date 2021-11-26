import mysql.connector
cnx = mysql.connector.connect(user="root", password="1qaz!QAZ",host="127.0.0.1",database="product")
cursor = cnx.cursor()
import requests
from bs4 import BeautifulSoup
import re
kala = input("")
res = requests.get("https://www.truecar.com/used-cars-for-sale/listings/%s/" %(kala))
soup = BeautifulSoup(res.text,"html.parser")
data=soup.find("ul",attrs={"class":"row margin-bottom-3"})
print(data)
vehicle_name = data.find_all("div",attrs={"data-test":"vehicleCardYearMakeModel"})
#vehicle_pic=data.find_all("div",attrs={"class":"img-container img-container-block"})
vehicle_mileage = data.find_all("div",attrs={"data-test":"vehicleMileage"})
price = data.find_all("div",attrs={"class":"heading-3 margin-y-1 font-weight-bold"})
#vehicle_pic1=[re.sub(r"\s+","",item.text).strip() for item in vehicle_pic]
vehicle_mileage1=[re.sub(r"\s+","",item.text).strip() for item in vehicle_mileage]
price1=[re.sub(r"\s+","",item.text).strip() for item in price]
vehicle_name1=[re.sub(r"\s+","",item.text).strip() for item in vehicle_name]
new_vehicle_mileage1 = tuple([x[:-5] for x in vehicle_mileage1])
#print(new_vehicle_mileage1)
#print(price1)
#print(vehicle_name1)
for i in range(0,20): 
    cursor.execute("INSERT INTO vehicle2 VALUES (\"%s\",\"%s\",\"%s\")" 
    %(vehicle_name1[i],new_vehicle_mileage1[i],price1[i]))

cnx.commit()
