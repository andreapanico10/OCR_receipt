# Python script and flow automation: Market Receipt items extraction with OCR service

## This repo is for those who need to track or carry out analyzes of purchases made in the supermarket without wasting time in manually acquiring the receipt data and/or those who love the automation of the flow between the various tools interconnected to Python (google sheet, google drive, push notifications on the mobile device, etc.)

Given a receipt photo, apply an OCR service of third parties (http://ocr.asprise.com/api/v1/receipt) to extract the items bought and manage data through automatic pipeline, from uploading the image to google drive, then to store the data in a google sheet as storage service. <br> Tasks covered in this Repo are the following:

* Python: Get the file list of a Google Drive folder
* Open the content of an image file in Google Drive as "BytesIO"
* How to call a third parties API service (http://ocr.asprise.com/api/v1/receipt)
* Save API response in a JSON file
* Python: Get the data in a Google Sheet
* Python: Update a sheet in Google Sheet
* Python: Move a file from a Google Drive folder to another

## External Sources: Stay updated on my projects and progress

<a href="https://www.linkedin.com/in/andrea-panico-252718201/">
Linkedin
</a>
<a href="https://github.com/andreapanico10">
GitHub
</a>

<ol>
  <li> pip install -r requirements.txt</li>
  <li> python OCR_receipt_extraction_script.py</li>
</ol>
