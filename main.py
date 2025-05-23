# This is a sample Python script.
import json
import os

from dotenv import load_dotenv
import requests
import base64
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def get_spotify_token():
    url = "https://accounts.spotify.com/api/token"
    auth_sting =  f"{os.getenv('CLIENT_ID')}:{os.getenv('CLIENT_SECRET')}"
    auth_bytes = auth_sting.encode('utf-8')
    auth_base64 = base64.b64encode(auth_bytes).decode('utf-8')
    headers = {
        "Authorization": f"Basic {auth_base64}"
    }
    form = {
        "grant_type": "client_credentials"
    }
    response = requests.post(url, headers=headers, data=form)
    return response.json()['access_token']

def search_album(token, query):
    url = f"https://api.spotify.com/v1/search?q={query}&type=album"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(url, headers=headers)
    return response.json()

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    print("hello")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    load_dotenv()
    token = get_spotify_token()
    album = search_album(token, "Mutter")
    print(type(album))
    print(json.dumps(album, indent=2))
    print(
        album['albums']['items'][0]['artists'][0]['name']
    )

    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
