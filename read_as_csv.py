import pandas as pd

input_file_name = "퀀트데이터2020.06.24"
data_xls = pd.read_excel(
    f"finance_data_xlsx/{input_file_name}.xlsx", "퀀트데이터", index_col=None
)
data_xls.to_csv(f"finance_data_csv/{input_file_name}.csv", encoding="utf-8")

