from collections import Counter

from detect_company import yield_frequency_data


def count_spinoffs(companies: list, articles: list) -> dict:
    # sum two dictionaries as Counter Object
    mergedFrequencyData = {}
    sum_freq_counterObj = Counter(mergedFrequencyData)
    for url in articles:
        frequencyData = yield_frequency_data(url, companies)
        freq_counterObj = Counter(frequencyData)
        sum_freq_counterObj = sum_freq_counterObj + freq_counterObj
        print(sum_freq_counterObj)

    # tranform Counter Object into dictionary
    sum_frequency = dict(sum_freq_counterObj)
    print(sum_frequency)
    return sum_frequency


"""
from crawl_spinoff_info import iterate_avail_articles
from extract_company_list import yield_kospi_companies

spinoff_articles_list = [
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202006241133130960107154&lcode=00&page=1&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202006241132074760108114&lcode=00&page=1&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202006231009195400102978&lcode=00&page=1&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202006220912030400103218&lcode=00&page=1&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202006220946501400103784&lcode=00&page=1&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202006191422511360102743&lcode=00&page=1&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202006191355276840108314&lcode=00&page=1&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202006171057167720103744&lcode=00&page=1&svccode=00",
    "http://www.thebell.co.kr/free/content/ArticleView.asp?key=202006170857397900106488&lcode=00&page=1&svccode=00",
]

kospi_companies = yield_kospi_companies()
count_spinoffs(kospi_companies, spinoff_articles_list)
"""

