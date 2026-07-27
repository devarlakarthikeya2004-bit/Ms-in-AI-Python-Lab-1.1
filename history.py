import os
from unittest.mock import call
import requests
from dotenv import load_dotenv
import json
import sys
from pathlib import Path

conversation_folder = Path("conversations")
conversation_file = conversation_folder / "chart1.json"

def get_history(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            messages = json.load(f)
        return messages

    except json.JSONDecodeError:
        print("conversation file is empty or corrupted. Creating a new one.")

        return [
            {"role": "system", "content": "You are a helpful assistant."}
        ]
    except FileNotFoundError:
        print("conversation file not found. Creating a new one.")
        return [
            {"role": "system", "content": "You are a helpful assistant."}
        ]




def save_history(path, messages):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(messages, f, indent=4)