"""
Makes and wrangles the most recent excel file into csv file as same file name
./finace_data_csv_wrangled is the end point for data, whereas CSV folder is stop-by point.
"""

import pandas as pd
from select_recent import get_recent_file_name

# TODO: SELECT MOST RECENT FILE IN THE FOLDER
def make_xlsx_to_csv(input_file_name, excel_folder_path, csv_folder_path):
    data_xls = pd.read_excel(
        f"{excel_folder_path}/{input_file_name}.xlsx", "퀀트데이터", index_col=False
    )
    data_xls.to_csv(
        f"{csv_folder_path}/{input_file_name}.csv", encoding="utf-8", index=False
    )

    return


def wrangle_csv(input_file_name, read_csv_folder_path, write_csv_folder_path):
    df = pd.read_csv(f"{read_csv_folder_path}/{input_file_name}.csv", index_col=False)

    # set the second column as dataframe header
    df.columns = df.iloc[1]

    # drop first two rows in the dataframe
    df = df.drop([df.index[0], df.index[1]])

    # drop first column in the dataframe
    df = df.drop([df.columns[0], df.columns[1]], axis="columns")

    df.to_csv(
        f"{write_csv_folder_path}/{input_file_name}.csv", encoding="utf-8", index=False
    )

    return
