import pandas as pd


# TODO: MAKE II TO FIND MOST RECENT FILE
def make_xlsx_to_csv(input_file_name, excel_folder_path, csv_folder_path):
    data_xls = pd.read_excel(
        f"{excel_folder_path}/{input_file_name}.xlsx", "퀀트데이터", index_col=None
    )
    data_xls.to_csv(f"{csv_folder_path}/{input_file_name}.csv", encoding="utf-8")

    return


def wrangle_csv(input_file_name, read_csv_folder_path, write_csv_folder_path):
    df = pd.read_csv(f"{read_csv_folder_path}/{input_file_name}.csv")

    # set the second column as dataframe header
    df.columns = df.iloc[1]

    # drop first two rows in the dataframe
    df = df.drop([df.index[0], df.index[1]])

    df.to_csv(f"{write_csv_folder_path}/{input_file_name}.csv")

    return


excel_folder_path = "finance_data_xlsx"
csv_folder_path = "finance_data_csv"
wrangled_folder_path = "finance_data_csv_wrangled"
file_name = "퀀트데이터2020.06.24"

make_xlsx_to_csv("퀀트데이터2020.06.24", excel_folder_path, csv_folder_path)
wrangle_csv("퀀트데이터2020.06.24", csv_folder_path, wrangled_folder_path)
