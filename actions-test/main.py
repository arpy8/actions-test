import os
import pytz
import datetime
import requests

API_URL = f'https://disdial.onrender.com/data'

_chat_headers = {
    'Authorization': os.environ["CHAT_TOKEN"],
    'Content-Type': 'application/json',
}

def get_time():
    current_time = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
    return current_time.strftime('%Y-%m-%d %H:%M:%S %Z')

def send_message_to_server(message):
    data = {
        'time': get_time(),
        'username': "Github Action",
        'message': message,
    }

    try:
        response = requests.post(API_URL, json=data, headers=_chat_headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return f"Request failed: {e}"


def main():
    try:
        send_message_to_server("Hello World")
        print("Message sent successfully")
    except Exception as e:
        print(e)
        
if __name__ == "__main__":
    main()