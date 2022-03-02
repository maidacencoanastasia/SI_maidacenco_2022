import requests
from bs4 import BeautifulSoup
import argparse

URL = "https://pythonjobs.github.io"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
# print(soup)

#results = soup.find(class_="job")
#print(results)
#
title = soup.find_all("title")
for i in title:
    print(i.text)

headings = soup.find_all("h1")
for i in headings:
    print(i.text)

job_elements = soup.find_all("div", class_="job")
for job_element in job_elements:
    print(job_element.text, "\n")

job_info = soup.find_all("span", class_="info")
for i in job_info:
    print(i.text, "\n")

job_detail = soup.find_all("p", class_="detail")
for i in job_detail:
    print(i.text, "\n")


for i in range(0,len(headings)):
    print(headings[i].text,"\n")
    print(job_info[i].text)

