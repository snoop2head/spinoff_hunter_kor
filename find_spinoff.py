import pandas as pd

# TODO: SELECT MOST RECENT FILE IN THE FOLDER
wrangled_folder_path = "finance_data_csv_wrangled"
file_name = "퀀트데이터2020.06.24"

df = pd.read_csv(f"{wrangled_folder_path}/{file_name}.csv")
kospi_df = df.loc[df["코스피코스닥"] == "코스피"]
kosdaq_df = df.loc[df["코스피코스닥"] == "코스닥"]

tot_public_companies = df["회사명"].to_list()
kospi_companies = kospi_df["회사명"].to_list()
kosdaq_companies = kosdaq_df["회사명"].to_list()

