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
* MAC OS: How to schedule a script execution with Automator

## Pipeline automated

1. Take a picture from your phone and upload it to a "SOURCE" Google Drive folder.
2. The python script will be launched daily from an Automator app and will check if there are files in this SOURCE folder. 
3. If there are any, it means that you are gone to the grocery and the products must be extracted from the receipt photo and saved in our sheet.
4. Acquire the photo from Google Drive and call the OCR API service to extract the text from receipt.
5. Get the response and save it in a JSON file
6. Extract the information of interest (for me: shopping date, supermarket name, items list) and ad hoc correction for the use case
7. Connect to the storage Google Sheet and get the first empty row in order to understand where start to write.  
8. For any item, format the row to insert and add to the sheet.
9. In Google Drive move the already examined file to another Backup folder "DESTINATION" 
10. At the end of process, send a Push Notification to my phone through pushbullet to comunicate the operation. I find this solution faster and easier than a telegram bot
 

## External Sources: Stay updated on my projects and progress

<a href="https://www.linkedin.com/in/andrea-panico-252718201/">
Linkedin
</a>
<a href="https://github.com/andreapanico10">
GitHub
</a>

## How to install: instruction
1. Clone the repository
2. Update your environment with the missing packages: 
```
pip install -r requirements.txt
```
3. Create a Google dashboard with Google Sheet scope for your project: https://console.cloud.google.com/welcome following this fantastic Medium post: https://medium.com/daily-python/python-script-to-edit-google-sheets-daily-python-7-aadce27846c0 and download the user_key that I've called 'client_key.json' and put it in the project folder
4. Create another dashboard with Google Drive scopes with credentials as "Service User", download the auto-generated key json file that I've called 'service.json' and put in the project folder
5. Create a PushBullet account (following this guide: https://www.youtube.com/watch?v=tbzPcKRZlHg&t=164s)
6. Configure a .env file with the following structure:
```
PUSHBULLET_API_KEY = "<The API_KEY obtained in 5.>"
GOOGLE_SHEET_CREDENTIALS_FILE = "< 3.json file relative path wrt project folder>"
GOOGLE_DRIVE_CREDENTIALS_JSON = '< 4.json file relative path wrt project folder>'
TEMP_JSON_FILE = "<Name given to the temp json file, choose what you want>"
LOCAL_RECEPIT_IMAGE_PATH = "<Optional (is the relative parth wrt project folder of a test receipt image)>"
SOURCE_FOLDER_ID = "<Google Drive Source Folder Id>"
DESTINATION_FOLDER_ID = "<Google Drive Source Destination Id>" 
```
7. Run the script: 
```
python OCR_receipt_extraction_script.py 
```


## Collaboration 

This is an example project and if you are interested to expand the project, please clone it and contact me at the email address: andreapanico98@gmail.com

## Find a Bug?

If you find an issue or would like to submit an improvement to this project, please submit an issue using the issues tab above.

## Like this project?

If you are feeling stimulated by this project and want to make me smile, buy me a coffee!
https://www.buymeacoffee.com/andreapynico