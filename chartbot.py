import os
from urllib import response
import requests
import sys
import json
from pathlib import Path
from dotenv import load_dotenv
from unittest.mock import call
load_dotenv()
from history import get_history, save_history
import history

try:
    API_KEY = os.environ["NVIDIA_API_KEY"]
    print(API_KEY)
except KeyError:
    print("key not found in .env file. Please set NVIDIA_API_KEY in your .env file.")
    sys.exit(1)


URL = "https://integrate.api.nvidia.com/v1/chat/completions"
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Accept": "application/json",
}


def llm_call(messages):
    json= {  "messages": messages,
    "model": "meta/llama-3.1-8b-instruct",
    }
    try:
        "response = requests.get(URL, headers=headers, json=json) "
        response = requests.post(URL, headers=headers, json=json)  
        """print(response.status_code)
        print(response.text)"""
        response.raise_for_status()
        data = response.json()
        return data['choices'][0]['message']['content']
    except requests.exceptions.ConnectionError:
        print("connection error, please check your internet connection.")
        return None 
    except requests.exceptions.Timeout:
        print("request timed out, try again later.")
        return None   
    
    

def run_chart(message):
    while True:
        user_message = input("please enter message: ").strip().lower()
        if user_message == "quit":
            break
        elif not user_message:
            print("empty message. Please enter a valid message.")
            continue
        messages.append({"role": "user", "content": user_message})
        response= llm_call(messages)
        messages.append({"role": "assistant", "content": response})
        print("Agent:", response)
        "return response"  "the function closes automatically after the first response, so the user can only send one message and get one response. To allow for multiple messages and responses, we can use a while loop that continues until the user types 'quit'."
    return response


conversation_folder = Path("conversations")
file = Path("conversations") / "chart1.json"

if __name__ == "__main__":
    messages = get_history(file)
    run_chart(messages)
    save_history(file, messages)
    


