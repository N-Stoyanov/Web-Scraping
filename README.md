# 📚 Books Web Scraper

![Python](https://img.shields.io/badge/python-3.13-blue)
![SQLite](https://img.shields.io/badge/sqlite-3.38-orange)

This project scrapes book data from **Books to Scrape**, stores it in a SQLite database, and provides SQL queries for analysis.

---

## 💡 Overview

The project consists of multiple files:

- `scraper.py` — Python script that scrapes book data and saves it in a SQLite database  
- `books.db` — SQLite database containing the scraped book data  
- `queries.sql` — Sample SQL queries for analysis    
- `README.md` — Project documentation  

The scraper demonstrates a full data workflow: **Scraping → Cleaning → Storage → Analysis**, showcasing skills in Python, web scraping, SQL, and data handling.

---

## ⚙️ Tech Stack

| Tool          | Purpose                     |
|---------------|----------------------------|
| Python        | Scraper and data handling  |
| BeautifulSoup | HTML parsing               |
| requests      | HTTP requests to website   |
| pandas        | Data cleaning and storage  |
| SQLite        | Database storage           |
| SQL           | Analytical queries         |
# 🧠 Usage Instructions

This document explains how to run the scraper and execute SQL queries on the collected book data.

---

## 1. Run the Scraper

The scraper collects book data from the website and stores it in a SQLite database.

1. Open your terminal and navigate to the project folder.
2. Run the scraper:
python3 scraper.py

- This will populate or update `books.db`.
- The scraper fetches book data from the selected categories defined in `scraper.py`.

---

## 2. Run SQL Queries

After scraping, you can explore the data using the included SQL queries.

### Option A: SQLite Command Line

1. Open SQLite with the database:

sqlite3 books.db

2. Execute the SQL queries:

.read queries.sql

3. Exit SQLite:

.exit

### Option B: Python Runner (Optional)

1. Ensure `queries.py` is in the project folder.
2. Run the Python script:

python3 queries.py


- This will execute the queries from `queries.sql` and print results in the terminal.

---

## Notes

- Make sure you have all dependencies installed (`pandas`, `requests`, `BeautifulSoup4`) as listed in `requirements.txt`.
- If `books.db` does not exist, running `scraper.py` will automatically create it.
- The SQL queries included cover tasks such as:
  - Average price by category
  - Top 10 most expensive books
  - Count of books by rating
  - Filtering books by category or price
  - 
