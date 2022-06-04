import requests
import time

channelID = 112233445566778899  # CHANNEL ID YOU WANT TO SPAM
headers = {
    "authorization": "YOUR AUTH TOKEN HERE"}

file = open("test.txt", "r")
Lines = file.readlines()

for line in Lines:
    requests.post(
        f"https://discord.com/api/v9/channels/{channelID}/messages", headers=headers, json={"content": line})
