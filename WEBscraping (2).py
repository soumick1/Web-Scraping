import requests
from bs4 import BeautifulSoup
import pandas
import connect


page = requests.get('https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card')
soup = BeautifulSoup(page.content, "html.parser")

connect.connect("GC_info.db")

containers = soup.findAll("div", {"class": "item-container"})
scraped_info_list=[]

for container in containers:
    dict = {}
    dict['Product_Name'] = container.find("a", {"class": "item-title"}).text
    dict['Product_Price'] = container.find("li", {"class": "price-current"}).text.strip()
    dict['Shipping_Price'] = container.find("li", {"class": "price-ship"}).text.strip()
    try:
        dict['Rating'] = container.find("a", {"class": "item-rating"}).i["class"][1]
        dict['Number_of_reviews'] =  container.find("a", {"class": "item-rating"}).text
    except AttributeError:
        dict['Rating'] = "no ratings yet"
        dict['Number_of_reviews'] = "no reviews"
    scraped_info_list.append(dict)
    connect.insert_info_table("GC_info.db", tuple(dict.values()))

dataFrame = pandas.DataFrame(scraped_info_list)
dataFrame.to_csv("Graphics_Cards.csv")
connect.get_graphics_card_info("GC_info.db")







