import requests
from bs4 import BeautifulSoup
url = ('https://www.hotels.com/Hotel-Search?adults=2&d1=2022-12-22&d2=2022-12-23&destination=Cairo%2C%20Cairo%20Governorate%2C%20Egypt&direct=&endDate=2023-01-01&locale=en_GB&pos=HCOM_ME&regionId=767&semdtl=&siteid=310000033&sort=RECOMMENDED&startDate=2022-12-31&theme=&useRewards=false&userIntent=')
page=requests.get(url)
name_hotels =[]
price_nights = []
price_night_incloud_taxes_and_fees= []
rating_place = []
Location =[]
offers=[]
more_offers = []
soup=BeautifulSoup(page.content,'html.parser')
name_hotel = soup.find_all('h2',{'class':'uitk-heading uitk-heading-5 overflow-wrap'})
price_night = soup.find_all('div',{'class':'uitk-text uitk-type-600 uitk-type-bold uitk-text-emphasis-theme'})
total_price = soup.find_all("div",{"class":"uitk-text uitk-type-end uitk-type-200 uitk-text-default-theme"})
rating = soup.find_all("div" ,{"class":"uitk-layout-flex uitk-layout-flex-flex-wrap-wrap"})
location = soup.find_all("div", {"class":"uitk-text uitk-text-spacing-half truncate-lines-2 uitk-type-300 uitk-text-default-theme"})
free = soup.find_all("div",{"class":"uitk-text truncate uitk-type-200 uitk-text-default-theme"})
more_offer = soup.find_all("div",{"class":"uitk-layout-flex-item"})
for element in range(len(name_hotel)) :
    name_hotels.append(name_hotel[element].text)
    price_nights.append(price_night[element].text)
    #price_night_incloud_taxes_and_fees.append(total_price[element].text)
    rating_place.append(rating[element].text)
    Location.append(location[element].text)
    #offers.append(free[element].text)
for i in range(len(total_price)) :
    price_night_incloud_taxes_and_fees.append(total_price[i].text)
for j in range(len (free)):
    offers.append(free[j].text)
for p in range (len(more_offer)) :
    more_offers.append(more_offer[p].text)

print (name_hotels ,"\n", price_nights, "\n",price_night_incloud_taxes_and_fees ,"\n",Location ,"\n",offers , "\n" , rating_place ,"\n",more_offers )



