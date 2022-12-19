import os
import sys
sys.path.append(os.getcwd())
from config import config
import gspread
from googleapiclient.errors import HttpError
import json

def get_value(sheetName,sheetRange):
    try:
        values = config.SHEET.values().get(spreadsheetId=config.GSHEET_ID,
                            range=f'{sheetName}!{sheetRange}').execute()
        return values['values']        
    except:
        return 'None'
def update_values(sheetName,sheetRange, value_input_option, value):
    # pylint: disable=maybe-no-member
    try:
        body = {
            'values': [[value]]
        }
        result = config.SHEET.values().update(
            spreadsheetId=config.GSHEET_ID, range=f'{sheetName}!{sheetRange}',
            valueInputOption=value_input_option, body=body).execute()
        # print(f"{result.get('updatedCells')} cells updated.")
        return result
    except HttpError as error:
        print(f"An error occurred: {error}")
        return error
def check_laballed_status():
    status = get_value('Label_status','A2')
    if status[0][0] == 'False':
        return False
    elif status[0][0] == 'True':
        return True
    else:
        return None

def upload_labelled_data_to_sheet():
    gc = gspread.authorize(config.credentials)
    workSheet = gc.open("Via_infant_data").sheet1

    # Let's say you have some json values
    with open(config.CURRENT_LABELLED_JSON_PATH) as json_file:
        dataJson = json.load(json_file)
    
    print(f'Uploading {len(dataJson)} items....')

    result = []
    for value in dataJson:
        try:
            result.append([value['filename'],value['file_size'],value['file_attributes'],value['region_count'],value['region_id'],value['region_shape_attributes'],value['region_attributes']])
        except:
            pass

    address = 'A2' 
    workSheet.update(str(address), result)
    
    
    
# check_laballed_status()

# update_values('Label_status','C1', 'USER_ENTERED', '1')