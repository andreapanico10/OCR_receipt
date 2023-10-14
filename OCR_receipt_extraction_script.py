from google.oauth2 import service_account
from googleapiclient.discovery import build
from OCR_receipt_call_API import call_asprise_API
from json_reader import json_reader
import io
import os 
import os
from dotenv import load_dotenv
load_dotenv()
from pushbullet import Pushbullet

# Set the paths to your source and destination folders
SOURCE_FOLDER_ID = os.getenv("SOURCE_FOLDER_ID")
DESTINATION_FOLDER_ID = os.getenv("DESTINATION_FOLDER_ID")

# Path to your credentials JSON file
GOOGLE_DRIVE_CREDENTIALS_JSON = os.path.join(os.getcwd(), os.getenv("GOOGLE_DRIVE_CREDENTIALS_JSON"))

TEMP_JSON_FILE = os.path.join(os.getcwd(), os.getenv("TEMP_JSON_FILE"))

# PushBullet
pb = Pushbullet(os.getenv('PUSHBULLET_API_KEY'))

# Create a service account credentials object
credentials = service_account.Credentials.from_service_account_file(
    GOOGLE_DRIVE_CREDENTIALS_JSON, scopes=['https://www.googleapis.com/auth/drive']
)

# Create a Drive API service
drive_service = build('drive', 'v3', credentials=credentials)

# List all files in the folder
results = drive_service.files().list(
    q=f"'{SOURCE_FOLDER_ID}' in parents",
    fields="files(id, name)",
).execute()

files = results.get('files', [])

if not files:
    print(f'Source folder empty.')
else:
    print("Files to elaborate:")
    for file in files:
        print(file)
        file_id = file['id']

        # Retrieve the file content
        image_data = drive_service.files().get_media(fileId=file_id).execute()

        # Create a file-like object from the file data
        file_content = io.BytesIO(image_data)
        
        # Calling The API
        API_return = call_asprise_API(file_content)
        
        if API_return == TEMP_JSON_FILE:
            
            # Extracting the items from the json file and updating the sheet
            json_reader(TEMP_JSON_FILE)

            # Move the file to the destination folder
            drive_service.files().update(
                fileId=file_id,
                addParents=DESTINATION_FOLDER_ID,
                removeParents=SOURCE_FOLDER_ID,
                fields='id, parents'
            ).execute()

            print(f'File "{file}" moved to the destination folder.')
            push = pb.push_note("OCR scontrino effettuato",f'File "{file}" processed through OCR.')

            os.remove(TEMP_JSON_FILE)
