from __future__ import print_function

import os
import sys
sys.path.append(os.getcwd())
from config import config
from utils.convertor import convert_csv_to_json, convert_sheet_to_json, add_data_to_json
from utils.sheet_interactor import get_value, update_values, check_laballed_status, upload_labelled_data_to_sheet

import json
import time


viaInfantData = config.SHEET.values().get(spreadsheetId=config.GSHEET_ID,
                            range="Via_infant_data!A1:G1000000").execute()

CSV_PATH = 'D:/Downloads/via_infant_test.csv'




def main():
    if check_laballed_status() == None:
        update_values('Label_status','A2', 'USER_ENTERED', 'True')
    while check_laballed_status() == True:
        print("Please wait a few seconds to try again!!!")
        time.sleep(2)
    print("Nobody's interacting!!!")
    try:
        update_values('Label_status','A2', 'USER_ENTERED', 'True')
        
        # convert new labelled csv file to Json
        convert_csv_to_json(CSV_PATH, config.TEMP_LABELLED_JSON_PATH)

        # write current labelled sheet to current laballed Json
        convert_sheet_to_json(config.LINK_GSHEET_IN_JSON, config.CURRENT_LABELLED_JSON_PATH)
        add_data_to_json(config.TEMP_LABELLED_JSON_PATH, config.CURRENT_LABELLED_JSON_PATH)
        
        with open(config.CURRENT_LABELLED_JSON_PATH, "r") as jsonFile:    
            data = json.load(jsonFile)
        upload_labelled_data_to_sheet()
        totalData = len(data)
        update_values('Label_status','B2', 'USER_ENTERED', str(totalData))
        update_values('Label_status','A2', 'USER_ENTERED', 'False')
        time.sleep(5)
        if check_laballed_status()== False: 
            print('Upload successfully!')
    except:
        pass


if __name__ == '__main__':
    main()

