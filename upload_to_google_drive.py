import gspread

# Configuration Documentation: https://gspread.readthedocs.io/en/latest/oauth2.html#for-bots-using-service-account

# google spreadsheet API enabled credentials
gc = gspread.service_account(
    filename="/Users/noopy/spinoff_hunter_kor/credentials.json"
)

# input google drive spreadsheet file name
sh = gc.open("퀀트데이터2020.06.24_spinoff")

print(sh.sheet1.get("A1"))

