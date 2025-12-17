import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import sqlite3

base_url = 'https://books.toscrape.com/catalogue/category/books/'
categories = ["travel_2", "mystery_3"]
books = []

for cat in categories:
    url = f"{base_url}{cat}/index.html"
    while url:
        r = requests.get(url)
        soup = BeautifulSoup(r.text, "html.parser")

        for book in soup.select("article.product_pod"):
            title = book.h3.a["title"]
            price_text = book.select_one(".price_color").text
            price = float(re.sub(r"[^\d.]", "", price_text))
            rating = book.p["class"][1]
            books.append([title, price, cat, rating])

        next_btn = soup.select_one("li.next a")
        if next_btn:
            url = f"{base_url}{cat}/{next_btn['href']}"
        else:
            url = None
        

df = pd.DataFrame(books, columns=["Title", "Price", "Category", "Rating"])
conn = sqlite3.connect("books.db")
df.to_sql("books", conn, if_exists="replace", index=False)
conn.close()

print(df.head())
