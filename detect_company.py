"""
Checks how many times company names appear on thebell.co.kr's scraped articles
"""
import requests
from bs4 import BeautifulSoup
import lxml

# for url in spinoff_articles_list:
def yield_frequency_data(url: str, companies: list) -> dict:

    res = requests.get(url)
    soup = BeautifulSoup(res.content, "lxml")
    div = soup.find("div", {"class": "viewSection"})
    article_content = div.get_text()

    # set blank values
    frequencyData = {}
    mentioned_companies = []

    # detect companies mentioned in the article
    for company in companies:
        if company in article_content:
            mentioned_companies.append(company)

    # make json file for appearance frequency in single article
    for company in mentioned_companies:
        for word_spaced in article_content.split(" "):
            if company in word_spaced:
                frequencyData[company] = frequencyData.setdefault(company, 0) + 1
    return frequencyData


# one_data = yield_frequency_data(
#     "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201907040100010540000667&lcode=00&page=53&svccode=00"
# )
# print(type(one_data, kospi_companies))

