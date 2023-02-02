import json
import requests
import os

API_KEY = os.environ.get("API_KEY")
CHAT_ID = os.environ.get("CHAT_ID")
POLL_URL = f"https://api.telegram.org/bot{API_KEY}/sendPoll"
MSG_URL = f"https://api.telegram.org/bot{API_KEY}/sendMessage"

pollParameters = {
    'chat_id': CHAT_ID,
    'question': 'Who is coming home for dinner',
    'options': json.dumps(['Yes', 'No']),
    'is_anonymous': False,
    'protect_content': True
}

messageParameters = {
    'chat_id': CHAT_ID,
    'text': 'Please fill in the poll'
}

def send_poll(event, context):
    try:
        requests.get(POLL_URL, pollParameters)
        return {
            'statusCode':200
        }
    except:
        return {
            'statusCode':400
        }
    
def send_message(event, context):
    try:
        requests.post(MSG_URL, messageParameters)
        return {
            'statusCode':200
        }
    except:
        return {
            'statusCode':400
        }

    
