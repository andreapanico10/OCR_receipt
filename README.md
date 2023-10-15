# Python script and flow automation: Market Receipt items extraction with OCR service

## This repo is for those who need to track or carry out analyzes of purchases made in the supermarket without wasting time in manually acquiring the receipt data and/or those who love the automation of the flow between the various tools interconnected to Python (google sheet, google drive, push notifications on the mobile device, etc.)

Given a receipt photo, apply an OCR service of third parties (http://ocr.asprise.com/api/v1/receipt) to extract the items bought and manage data through automatic pipeline, from uploading the image to google drive, then to store the data in a google sheet as storage service. <br> Tasks covered in this Repo are the following:

* Extract text from Receipt with OCR techniques
* Python: Get the file list of a Google Drive folder
* Open the content of an image file in Google Drive as "BytesIO"
* How to call a third parties API service (http://ocr.asprise.com/api/v1/receipt)
* Save API response in a JSON file
* Python: Get the data in a Google Sheet
* Python: Update a sheet in Google Sheet
* Python: Move a file from a Google Drive folder to another
* Python: Send push notification to mobile phone with PushBullet

## External Sources: Stay updated on my projects and progress

<a href="https://www.linkedin.com/in/andrea-panico-252718201/">
Linkedin
</a>
<a href="https://github.com/andreapanico10">
GitHub
</a>

## How to install: instruction
1. Clone the repository
2. Update your environment with the missing packages: pip install -r requirements.txt
3. Create a Google dashboard with Google Sheet scope for your project: https://console.cloud.google.com/welcome following this fantastic Medium post: https://medium.com/daily-python/python-script-to-edit-google-sheets-daily-python-7-aadce27846c0 and download the user_key that I've called 'client_key.json' and put it in the project folder
4. Create another dashboard with Google Drive scopes with credentials as "Service User", download the auto-generated key json file that I've called 'service.json' and put in the project folder
5. Create a PushBullet account (following this guide: https://www.youtube.com/watch?v=tbzPcKRZlHg&t=164s)
6. Configure a .env file with the following structure:
PUSHBULLET_API_KEY = "<The API_KEY obtained in 5.>"
GOOGLE_SHEET_CREDENTIALS_FILE = "< 3.json file relative path wrt project folder>"
GOOGLE_DRIVE_CREDENTIALS_JSON = '< 4.json file relative path wrt project folder>'
TEMP_JSON_FILE = "<Name given to the temp json file, choose what you want>"
LOCAL_RECEPIT_IMAGE_PATH = "<Optional (is the relative parth wrt project folder of a test receipt image)>"
SOURCE_FOLDER_ID = "<Google Drive Source Folder Id>"
DESTINATION_FOLDER_ID = "<Google Drive Source Destination Id>" 

7. Run the script: python OCR_receipt_extraction_script.py 
