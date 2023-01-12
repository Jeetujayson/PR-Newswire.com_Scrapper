from operator import contains
from bs4 import BeautifulSoup
import requests
import time
from random import randint
import csv

Article_list = []
Article_title = []
English_articles = []
page = 1
number_of_pages_to_scrape = 3

with open('All_Consumer_Technology_July.csv', 'w', encoding="utf-8", newline="") as f:
    thewriter = csv.writer(f)

    while page < number_of_pages_to_scrape:
        url = "https://www.prnewswire.com/news-releases/consumer-technology-latest-news/consumer-technology-latest-news-list/?month=08&day=01&year=2022&hour=00&page=" + \
            str(page)+"&pagesize=100"
        print(url)
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})

        soup = BeautifulSoup(response.text, "html.parser")

        # finds all the article links
        links = soup.find_all(
            "a", class_="newsreleaseconsolidatelink display-outline")
        for link in links:

            h3 = link.find_all("h3")
            line = []

            for each in h3:
                ll = link.find_all("span", class_="langspan")
                if ll == []:

                    print("###########################################")
                    print(each)
                    date = each.find("small").text.strip()

                    line.append(date)

                    href = ('https://www.prnewswire.com/'+link["href"])
                    line.append(href)

                    title = (each.text.strip())
                    title = title.replace(date, "")
                    title = (title.strip())
                    line.append(title)

                    print("###########################################")
                    print(line)
                    thewriter.writerow(line)

                else:
                    pass

        time.sleep(randint(3, 4))
        page += 1
        print("Page No: " + str(page))
