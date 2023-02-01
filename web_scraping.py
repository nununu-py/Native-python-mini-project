import requests
import pandas as pd
from bs4 import BeautifulSoup

response = requests.get("https://news.ycombinator.com/")
web_page = response.text

soup = BeautifulSoup(web_page, 'html.parser')
# soup.prettify(web_page)

article_tag = soup.find_all(name='span', class_="titleline")
article_score = soup.find_all(name='span', class_='score')

result = []
for tag1, tag2 in zip(article_tag, article_score):
    a = tag1.find('a')
    link = a.get('href')
    title = a.string
    score = tag2.string.replace('points', '')
    result.append([link, title, score])

for items in result:
    print(f"LINK : {items[0]}, TITLE :  {items[1]}, SCORE: {items[2]}")

df = pd.DataFrame(result, columns=["LINK", "TITLE", "POITNS"])
print(df)
