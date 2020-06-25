import os
import requests
from bs4 import BeautifulSoup
import lxml
import string
from urllib.parse import urlparse


def get_all_hrefs(SEARCH_KEYWORD: str, PAGE_NUMBER: int) -> list:
    BASE_URL = "http://www.thebell.co.kr/free/content/"
    PERIOD_DAYS = 360
    SEARCH_QUERY = f"Search.asp?page={PAGE_NUMBER}&sdt=&period={PERIOD_DAYS}&part=A&keyword={SEARCH_KEYWORD}"
    href_items_list = []
    spinoff_articles_list = []

    scrape_url = BASE_URL + SEARCH_QUERY

    # get page content response from the web using requests and beautifulsoup
    res = requests.get(scrape_url)
    soup = BeautifulSoup(res.content, "lxml")
    # print(soup)

    for item in soup.find_all("a", href=True):
        href_items_list.append(item["href"])
    # print(href_items_list)
    for query in href_items_list:
        if "ArticleView" in query:
            if f"page={PAGE_NUMBER}" in query:
                url = BASE_URL + query
                spinoff_articles_list.append(url)

    # print(spinoff_articles_list, len(spinoff_articles_list))
    number_spinoff_articles = len(spinoff_articles_list)
    print(f"{number_spinoff_articles} number of spinoff articles got collected")
    print(f"test url is following: {spinoff_articles_list[0]}")
    return spinoff_articles_list


def iterate_avail_articles() -> list:
    total_spinoff_articles = []
    page_num = 1
    while True:
        # get spinoff articles
        fetched_spinoff_articles = get_all_hrefs("인적분할", page_num)

        # determine whether or not to end the loop
        test_article = fetched_spinoff_articles[0]
        parsed_url = urlparse(test_article)
        test_article_query = parsed_url.query
        test_article_key = test_article_query.split("&")[0]
        if any(test_article_key in s for s in total_spinoff_articles):
            print("job finished!")
            print(total_spinoff_articles)
            return total_spinoff_articles

        # stack up spinoff articles along the loop
        total_spinoff_articles += fetched_spinoff_articles
        print(f"total number of {len(total_spinoff_articles)} articles are available")
        page_num += 1


# get_all_hrefs("인적+분할", 1)
# get_all_hrefs("인적분할", 1)

# iterate_avail_articles()

