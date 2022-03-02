from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
# url = "http://olympus.realpython.org/profiles/dionysus"
url ="https://suvitruf.ru/2022/03/01/10744/weekly-gamedev-59-27-february-2022/"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
# print(soup.get_text())
# Al titles
title = soup.find_all("title")
for i in title:
    print(i.text)
# Headings
headings = soup.find_all("h3")
for i in headings:
    print(i.text)
# All images
print(soup.find_all("img"))
print(soup.title.string)
# All links
links = soup.find_all("a")
for i in links:
    print(i)
paragraf = soup.find_all("p")
for i in paragraf:
    print(i.text,"\n")





# pattern = "<h3.*?>.*?</h3.*?>"
# match_results = re.search(pattern, html, re.IGNORECASE)
# title = match_results.group()
# title = re.sub("<.*?>", "", title) # Remove HTML tags
#print(title)
