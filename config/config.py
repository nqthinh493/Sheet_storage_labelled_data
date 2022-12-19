
DATA_DIR = './Data/images/'

IMPLEMENTER = 'NQTHINH'

CURRENT_LABELLED_JSON_PATH = './json_labelled/current_labelled.json'      # convert from main labelled sheet (DON'T TOUCH!!!  that is important sheet)
TEMP_LABELLED_JSON_PATH = './json_labelled/temp_labelled.json'            # convert from new downloaded csv labelled file

GSHEET_ID = '1UX1bEemFJ3d0rtJn-Yov1Gi6PND3D7V2xj0s6vTdD68'
LINK_GSHEET_IN_JSON = 'https://opensheet.elk.sh/'+ GSHEET_ID + '/A:G'



###########################################################################
#Google API 
###########################################################################
import json
import requests

import gspread
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/spreadsheets',
          'https://spreadsheets.google.com/feeds',
          'https://www.googleapis.com/auth/drive']
SERVICE_ACCOUNT_FILE = './keys.json'
credentials = None
credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes = SCOPES)
# The ID and range of a sample spreadsheet.
service = build('sheets', 'v4', credentials=credentials)
# Call the Sheets API

SHEET = service.spreadsheets()

# Via_infant_data = SHEET.values().get(spreadsheetId=GSHEET_ID,
#                             range="Via_infant_data!A1:G1000000").execute()



