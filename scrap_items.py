from bs4 import BeautifulSoup
from openpyxl import Workbook
from selenium import webdriver
import statistics
from selenium import webdriver
import openpyxl as ox
import pandas as pd

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import matplotlib.pyplot as plot


def shop1():
    PATH = r'D:/Desktop/chromedriver.exe'
    driver = webdriver.Chrome(PATH)
    driver.get("https://www.pcgarage.ro/procesoare/filtre/serie-intel-core-i9/")
    # https://www.emag.ro/procesoare/filter/familie-procesor-f2666,intel-core-i9-v29361/c?ref=lst_leftbar_2666_29361
    # https://altex.ro/procesoare-calculator/cpl/filtru/tip-procesor-7195/intel-core-i9/
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    response = soup.find_all("p", {"class": "price"})
    data = []

    for item in response:
        data.append(item.text.strip("RON"))

    #print(data)
    mod_data = []
    for item in data:
        item = item.replace('.', '')
        item = item.replace(',', '.')
        item = mod_data.append(float(item))
    print(mod_data)
    return mod_data


def shop2():
    PATH = r'D:/Desktop/chromedriver.exe'
    driver = webdriver.Chrome(PATH)
    driver.get(
        "https://www.emag.ro/procesoare/filter/familie-procesor-f2666,intel-core-i9-v29361/c?ref=lst_leftbar_2666_29361")

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    response = soup.find_all("p", {"class": "product-new-price"})

    data = []

    for item in response:
        data.append((item.text.strip("Lei")))

    #print(data)
    mod_data = []
    for item in data:
        item = item.replace('.', '')
        item = item.replace(',', '.')
        item = mod_data.append(float(item))
    print(mod_data)
    return mod_data


def shop3():
    PATH = r'D:/Desktop/chromedriver.exe'
    driver = webdriver.Chrome(PATH)
    driver.get("https://altex.ro/procesoare-calculator/cpl/filtru/tip-procesor-7195/intel-core-i9/")

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    response = soup.find_all("span", {"class": "Price-int leading-none"})

    data = []

    for item in response:
        data.append((item.text.strip("lei")))

    #print(data)
    mod_data = []
    for item in data:
        item = item.replace('.', '')
        item = item.replace(',', '.')
        item = mod_data.append(float(item))
    print(mod_data)
    return mod_data


print("GARAJ")
extracted_data1 = shop1()
print("EMAG")
extracted_data2 = shop2()
print("ALTEX")
extracted_data3 = shop3()

mag1 = statistics.mean(extracted_data1)
mag2 = statistics.mean(extracted_data2)
mag3 = statistics.mean(extracted_data3)
print(mag1, mag2, mag3)


wb = Workbook()
ws = wb.active
ws['A1'] = "GARAJ"
for i, name in enumerate(extracted_data1):
    ws[f"A{i + 2}"] = (name)
ws['B1'] = "EMAG"
for i, name in enumerate(extracted_data2):
    ws[f"B{i + 2}"] = (name)
ws['C1'] = "ALTEX"
for i, name in enumerate(extracted_data3):
    ws[f"C{i + 2}"] = (name)
wb.save("data.xlsx")
