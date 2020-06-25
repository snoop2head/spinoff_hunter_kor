import pandas as pd


def yield_kospi_companies() -> list:
    # TODO: SELECT MOST RECENT FILE IN THE FOLDER
    wrangled_folder_path = "finance_data_csv_wrangled"
    file_name = "퀀트데이터2020.06.24"

    df = pd.read_csv(f"{wrangled_folder_path}/{file_name}.csv")
    kospi_df = df.loc[df["코스피코스닥"] == "코스피"]
    kosdaq_df = df.loc[df["코스피코스닥"] == "코스닥"]

    kospi_companies = kospi_df["회사명"].to_list()
    print("Getting All KOSPI Companies...")
    return kospi_companies


def yield_kosdaq_companies() -> list:
    # TODO: SELECT MOST RECENT FILE IN THE FOLDER
    wrangled_folder_path = "finance_data_csv_wrangled"
    file_name = "퀀트데이터2020.06.24"

    df = pd.read_csv(f"{wrangled_folder_path}/{file_name}.csv")
    kospi_df = df.loc[df["코스피코스닥"] == "코스피"]
    kosdaq_df = df.loc[df["코스피코스닥"] == "코스닥"]

    kosdaq_companies = kosdaq_df["회사명"].to_list()
    print("Getting All KOSDAQ Companies...")
    return kosdaq_companies


def yield_public_companies() -> list:
    # TODO: SELECT MOST RECENT FILE IN THE FOLDER
    wrangled_folder_path = "finance_data_csv_wrangled"
    file_name = "퀀트데이터2020.06.24"

    df = pd.read_csv(f"{wrangled_folder_path}/{file_name}.csv")
    kospi_df = df.loc[df["코스피코스닥"] == "코스피"]
    kosdaq_df = df.loc[df["코스피코스닥"] == "코스닥"]

    tot_public_companies = df["회사명"].to_list()
    print("Getting All Public Companies...")
    return tot_public_companies
