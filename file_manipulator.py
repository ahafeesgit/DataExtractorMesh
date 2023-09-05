
import json
import os
import pandas as pd

class FileManipulator:


    def read_json(file_name):
       f = open(file_name)
       return json.load(f)

    def write_json(file_name,json_data):
        with open(file_name, "w") as outfile:
            json.dump(json_data, outfile)

    def read_excel(src_excel_path):
        if os.path.isfile(src_excel_path):
            read_data = pd.read_excel(src_excel_path)
            return True, read_data
        else:
            return False, ""
        
    def update_excel(src_excel_path):
        if os.path.isfile(src_excel_path):
            read_data = pd.read_excel(src_excel_path)
            return True, read_data
        else:
            return False, ""


