import json 
import requests
import os
from dotenv import load_dotenv
load_dotenv()

API_URL = "http://ocr.asprise.com/api/v1/receipt"
TEMP_JSON_FILE = os.path.join(os.getcwd(), os.getenv("TEMP_JSON_FILE"))
LOCAL_RECEPIT_IMAGE_PATH = os.getenv("LOCAL_RECEPIT_IMAGE_PATH") 

def call_asprise_API(image):

    res = requests.post(API_URL,
                        data = {
                            'api_key' : 'TEST',
                            'recognizer': 'auto',
                            'ref_no' : 'oct_python_123'
                        },
                        files = {
                            'file' : image
                            #'file' : open(image, 'rb')
                        })

    if not res:
        print("No data received from API")
        return None
    else:
        with open(TEMP_JSON_FILE, "w") as f:
            json.dump(json.loads(res.text), f)
            print("JSON file created")
        return TEMP_JSON_FILE

if __name__ == "__main__":
    call_asprise_API(LOCAL_RECEPIT_IMAGE_PATH)