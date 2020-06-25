import requests
from bs4 import BeautifulSoup
import lxml

from get_spinoff_info import iterate_avail_articles
from extract_company_list import yield_kospi_companies


# spinoff_articles_list = iterate_avail_articles()
kospi_companies = yield_kospi_companies()

# for url in spinoff_articles_list:
url = "http://www.thebell.co.kr/free/content/ArticleView.asp?key=201907040100010540000667&lcode=00&page=53&svccode=00"
res = requests.get(url)
soup = BeautifulSoup(res.content, "lxml")
div = soup.find("div", {"class": "viewSection"})
article_content = div.get_text()
for company in kospi_companies:
    if company in article_content:
        print(company)
