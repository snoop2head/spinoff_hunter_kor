""" 
Yields Quantking xlsx file to spinoff candidate companies' csv file 
"""

import pandas as pd

from _get_spinoff_info import get_spinoff_info
from select_recent import get_recent_file_name
from make_csv import make_xlsx_to_csv, wrangle_csv
from upload_to_google_drive import upload_to_gs


def main(market, search_keyword, input_file_name):
    """ Market is either 'kospi', 'kosdaq', 'all' """

    # get companies involved in spinoff event crawled from thebell.co.kr
    spinoff_info = get_spinoff_info(market, search_keyword)
    spinoff_related_companies = spinoff_info.keys()
    print(spinoff_related_companies)

    # TODO: SELECT MOST RECENT FILE IN THE FOLDER
    # fetch wrangled finance data
    wrangled_folder_path = "finance_data_csv_wrangled"
    df = pd.read_csv(f"{wrangled_folder_path}/{input_file_name}.csv", index_col=False)
    spinoff_dataframes = []

    # extract finance data for companies involved with spinoff event
    for spinoff_candidate in spinoff_related_companies:
        df_finance_info = df.loc[df["회사명"] == spinoff_candidate]
        if df_finance_info["업종\n(대)"].values[0] != "금융":
            df_finance_info.insert(2, "기사등장횟수", spinoff_info[spinoff_candidate])
            spinoff_dataframes.append(df_finance_info)
        if df_finance_info["업종\n(대)"].values[0] == "금융":
            finance_company = df_finance_info["회사명"].values[0]
            print(f"{finance_company} is just finance company")

    # concat one-row spinoff involved companies dataframe for a csv file
    df_spinoff_candidate = pd.concat(spinoff_dataframes)
    print(df_spinoff_candidate)

    # save result as csv
    write_csv_folder_path = "_spinoff_data"
    df_spinoff_candidate.to_csv(
        f"{write_csv_folder_path}/{input_file_name}_spinoff.csv",
        encoding="utf-8",
        index=False,
    )
    return


if __name__ == "__main__":
    # Makes and wrangles the most recent excel file into csv file as same file name
    excel_folder_path = "finance_data_xlsx"
    csv_folder_path = "finance_data_csv"
    wrangled_folder_path = "finance_data_csv_wrangled"
    file_name = get_recent_file_name(excel_folder_path)

    make_xlsx_to_csv(file_name, excel_folder_path, csv_folder_path)
    wrangle_csv(file_name, csv_folder_path, wrangled_folder_path)

    # Makes spinoff company candidates csv file on ./_spinoff_data folder
    market = "KOSPI"
    search_keyword = "인적분할"
    main(market, search_keyword, file_name)

    # import csv file for the google spreadsheet
    google_spreadsheet_id = "1chJ2NKHVc0gKjsMaQI1UHEPxdjneV1ZWaTGHseQvxP4"
    upload_to_gs(google_spreadsheet_id)
