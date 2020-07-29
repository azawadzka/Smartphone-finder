# Creates a list of dictionaries in which each dictionary contains model description of one smartphone.
# Data: MediaMarkt Spain (mediamarkt.es), smartphones section.
# Serializes the data to 'smartphones.pickle' file using pickle.
#
# ref:
# https://www.youtube.com/watch?v=E5cSNSeBhjw
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/

import pandas as pd
import pickle
import requests
from bs4 import BeautifulSoup

smartphone_links_list = []
smartphones = []
brands = ["apple", "samsung", "huawei", "newlife", "honor", "xiaomi", "sony", "motorola", "realme", "oppo", "alcatel", "crosscall", "nokia", "oneplus", "tcl", "bq", "gigaset", "palm", "lg", "hammer", "asus", "meizu", "weimei", "vsmart", "moto", "lenovo"]

i = 1
while True: # indefinite iteration
    page = requests.get("https://www.mediamarkt.es/es/category/_smartphones-701189.html?page=" + str(i))
    soup = BeautifulSoup(page.content, 'html.parser')
    listing = soup.find(id="category")
    items = listing.find_all(class_='to-details button block arrow clickable')

    if len(items) == 0: break
    else: i += 1

    links_list = [item.get('data-clickable-href') for item in items]
    smartphone_links_list.extend(links_list)


for link in smartphone_links_list:
    print(link)
    page = requests.get('https://www.mediamarkt.es' + link)
    soup = BeautifulSoup(page.content, 'html.parser')
    section = soup.find(id='features')
    # dt = term
    # dd = description
    dts = section.find_all("dt")
    dds = section.find_all("dd")
    dts_list = [str(item.string) for item in dts]  # str() added to convert a custom soup datatype into one that pickle can handle.
    dds_list = [str(item.string) for item in dds]

    # brand
    section = soup.find(id='product-details')
    title = section.find_all("h1")
    string = str(title[0].string.lower())
    for brand in brands:
        if brand in string:
            dts_list.append("Marca")
            dds_list.append(brand)
            break

    # price
    section = soup.find(id='product-sidebar')
    item = section.find_all(class_='price big')
    price = str(item[0].string)
    dts_list.append("Precio")
    dds_list.append(price)

    # web address
    dts_list.append("Link")
    dds_list.append(link)

    new_dict = dict(zip(dts_list, dds_list))
    assert('Marca' in new_dict.keys())
    assert(new_dict['Marca'] is not None)
    assert(new_dict['Precio'] is not None)

    smartphones.append(new_dict)

print(len(smartphones))

with open('data_raw.pickle', 'wb') as handle:
    pickle.dump(smartphones, handle, protocol=pickle.HIGHEST_PROTOCOL)
