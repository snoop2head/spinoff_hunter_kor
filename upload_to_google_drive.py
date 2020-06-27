import gspread
from select_recent import get_recent_file_name

# Configuration Documentation: https://gspread.readthedocs.io/en/latest/oauth2.html#for-bots-using-service-account

# google spreadsheet API enabled credentials
gc = gspread.service_account(
    filename="/Users/noopy/spinoff_hunter_kor/credentials.json"
)

# input google drive spreadsheet file name
spinoff_google_sheets = gc.open("spinoff_data")

# print(spinoff_google_sheets.sheet1.get("A1"))

recent_file_name = get_recent_file_name("_spinoff_data")
content = open(f"_spinoff_data/{recent_file_name}.csv", "r").read()

# using import_csv function from gspread
gc.import_csv("1chJ2NKHVc0gKjsMaQI1UHEPxdjneV1ZWaTGHseQvxP4", content.encode("utf-8"))

