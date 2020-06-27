"""
selects recent file in folder, yields file name without extension
"""

import glob
import os


def get_recent_file_name(folder_name: str) -> str:
    list_of_files = glob.glob(f"./{folder_name}/*")
    latest_file = max(list_of_files, key=os.path.getctime)
    latest_file_without_extension, extension_code = os.path.splitext(latest_file)
    latest_file_name_without_extension = latest_file_without_extension.split("/")[-1]
    print(f"{latest_file_name_without_extension} is the latest file upto date")
    return latest_file_name_without_extension

