"""
Returns a list of Korean public market(Kospi, Kosdaq, or all) companies
"""


import pandas as pd
from select_recent import get_recent_file_name


def yield_kospi_companies() -> list:
    # TODO: SELECT MOST RECENT FILE IN THE FOLDER
    wrangled_folder_path = "finance_data_csv_wrangled"
    file_name = get_recent_file_name(wrangled_folder_path)

    df = pd.read_csv(f"{wrangled_folder_path}/{file_name}.csv")
    kospi_df = df.loc[df["코스피코스닥"] == "코스피"]
    kospi_companies = kospi_df["회사명"].to_list()
    print("Getting All KOSPI Companies...")
    return kospi_companies


def yield_kosdaq_companies() -> list:
    # TODO: SELECT MOST RECENT FILE IN THE FOLDER
    wrangled_folder_path = "finance_data_csv_wrangled"
    file_name = get_recent_file_name(wrangled_folder_path)

    df = pd.read_csv(f"{wrangled_folder_path}/{file_name}.csv")
    kosdaq_df = df.loc[df["코스피코스닥"] == "코스닥"]
    kosdaq_companies = kosdaq_df["회사명"].to_list()
    print("Getting All KOSDAQ Companies...")
    return kosdaq_companies


def yield_public_companies() -> list:
    # TODO: SELECT MOST RECENT FILE IN THE FOLDER
    wrangled_folder_path = "finance_data_csv_wrangled"
    file_name = get_recent_file_name(wrangled_folder_path)

    df = pd.read_csv(f"{wrangled_folder_path}/{file_name}.csv")
    tot_public_companies = df["회사명"].to_list()
    print("Getting All Public Companies...")
    return tot_public_companies
