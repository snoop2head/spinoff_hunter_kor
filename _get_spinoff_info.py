from count_spinoffs import count_spinoffs
from extract_company_list import (
    yield_kospi_companies,
    yield_kosdaq_companies,
    yield_public_companies,
)
from crawl_spinoff_info import iterate_avail_articles


def get_spinoff_info(bundle: str) -> dict:
    bundle.lower()
    # fetching lists for the main function
    spinoff_articles_list = iterate_avail_articles("인적분할")

    if bundle == "kospi":
        companies = yield_kospi_companies()
    elif bundle == "kosdaq":
        companies = yield_kosdaq_companies()
    elif bundle == "all":
        companies = yield_public_companies()
    else:
        print("choose out of kospi, kosdaq, all")
    spinoff_dictionary = count_spinoffs(companies, spinoff_articles_list)
    print("SPINOFF DICTIONARY FORMED!")
    print(spinoff_dictionary)
    return spinoff_dictionary

