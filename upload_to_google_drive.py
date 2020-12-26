import gspread
from select_recent import get_recent_file_name

# Configuration Documentation: https://gspread.readthedocs.io/en/latest/oauth2.html#for-bots-using-service-account


def upload_to_gs(spreadsheet_id):
    # google spreadsheet API enabled credentials
    gc = gspread.service_account(filename="./credentials.json")

    """
    # input google drive spreadsheet file name
    spinoff_google_sheets = gc.open("spinoff_data")
    print(spinoff_google_sheets.sheet1.get("A1"))
    """

    recent_file_name = get_recent_file_name("_spinoff_data")
    content = open(f"_spinoff_data/{recent_file_name}.csv", "r").read()

    # using import_csv function from gspread
    gc.import_csv(spreadsheet_id, content.encode("utf-8"))
    return

