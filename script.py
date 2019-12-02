# import libraries
from urllib.request import urlopen
from bs4 import BeautifulSoup
from datetime import datetime
import time

# specify the url
url = "https://www.amazon.de/gp/product/B01N4ND1T2?pf_rd_p=671e72bc-8864-4ab6-8ef7-60da5d6ead8c&pf_rd_r=FDCX21V5S4DB9GDP475Q"


def check_price():
    # Connect to the website and return the html to the variable ‘page’
    try:
        page = urlopen(url)
    except:
        print("Error opening the URL")

    soup = BeautifulSoup(page, "html.parser")
    # get title and price
    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = price[0:5]
    # print title, price and time
    print(title.strip())
    print("Momentaner Preis: " + converted_price + " Euro")
    print(datetime.now().time().replace(microsecond=0))


while True:
    check_price()
    time.sleep(10)
