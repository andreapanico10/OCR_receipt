import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import locale
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()
import os 

GOOGLE_SHEET_CREDENTIALS_FILE = os.path.join(os.getcwd(), os.getenv("GOOGLE_SHEET_CREDENTIALS_FILE"))
TEMP_JSON_FILE = os.path.join(os.getcwd(), os.getenv("TEMP_JSON_FILE"))

def get_supermarket_name(supermarket):
    if "conad" in supermarket.lower():
        return "Conad"
    elif "lidl" in supermarket.lower():
        return "Lidl"
    elif "supergest" in supermarket.lower():
        return "Sisa"
    
def open_json_file(json_file_path):
    with open(json_file_path, "r") as f:
        return json.load(f)

def g_drive_credentials(credentials_file):
    
    scope = [
        'https://www.googleapis.com/auth/drive',
        'https://www.googleapis.com/auth/drive.file'
        ]
    creds = ServiceAccountCredentials.from_json_keyfile_name(credentials_file,scope)
    client = gspread.authorize(creds)
    
    return client

def extract_and_clean_valid_items(items):
    #print(f"I tuoi acquisti da: {supermarket_name}\n")

    valid_items = []
    for item in items:
        if type(item['amount']) == float: # Remove misunderstanting in Conad
            if item['amount'] < 0:
                # Algebric sum
                valid_items[-1]['amount'] += item['amount']
            else:
                #if 'conad' in supermarket.lower(): # This behaviour is for all the supermarkets
                    # In Conad receipt, there is a VI sign (useless chars) for the IVA
                if item['description'][-2:] == "VI":
                    item['description'] = item['description'][:-2]
                valid_items.append(item)
    return valid_items

def update_sheet(valid_items, sheet, supermarket_name, shop_date, row_counter):
    for item in valid_items:
        print(f"{item['description']} - € {item['amount']}")

        row = [item['description'], None, None, supermarket_name, locale.atof(str(item['amount'])), None, shop_date]
        python_sheet = sheet.get_all_records()
        index = row_counter + 1
        row_counter += 1
        sheet.insert_row(row,index)

def json_reader(json_file_path):

    data = open_json_file(json_file_path)
    #Authorize the API
    client = g_drive_credentials(GOOGLE_SHEET_CREDENTIALS_FILE)

    sheet = client.open('Receipts').sheet1
    python_sheet = sheet.get_all_records()

    row_counter = len(python_sheet) + 1

    items = data['receipts'][0]['items']
    shop_date = data['receipts'][0]['date']
    input_date_format = "%Y-%m-%d"
    input_date = datetime.strptime(shop_date, input_date_format)
    output_date_format = "%d-%m-%Y"
    shop_date = input_date.strftime(output_date_format)

    supermarket = data['receipts'][0]['merchant_name']
    supermarket_name = get_supermarket_name(supermarket)

    # Extract valid items
    valid_items = extract_and_clean_valid_items(items)
    # Update Receipts Sheet
    update_sheet(valid_items, sheet, supermarket_name, shop_date, row_counter)

if __name__ == '__main__':
    json_reader(TEMP_JSON_FILE)