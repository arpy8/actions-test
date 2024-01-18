import os
import logging
import requests

from scraper import return_last_issue

CHANNEL_ID = os.environ["CHANNEL_ID"]
BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_TOKEN = os.environ["CHAT_TOKEN"]

logging.basicConfig(filename='data.log', level=logging.INFO)

def update_log(message):
    with open("data.log", "w") as file:
        file.write(message)
        return message
    
def check_log(message):
    with open("data.log", "r") as f:
        log = f.read()
    if message in log:
        return True
    return False

def send_message(message):
    response = requests.post(
        url=f'https://discord.com/api/v10/channels/{str(CHANNEL_ID)}/messages', 
        headers={
            'Authorization': f'Bot {BOT_TOKEN}',
            'Content-Type': 'application/json',
        },
        json={
            'content': f"New issue found: {message}",
        }
    )

    if response.status_code != 200:
            return "Error sending message"

def main():
    try:
        with open("url.txt", "r") as f:
            data = f.read()
            url = data.strip()
            
        message = return_last_issue(url)
        check = check_log(message)

        if check:
            print("No new issues")
        else:
            print("New issues found: ", message)
            send_message(message)
            update_log(message)
            
    except Exception as e:
        print("Error", e)
        
if __name__ == "__main__":
    main()