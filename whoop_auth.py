import requests
import os
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv("WHOOP_CLIENT_ID")
client_secret = os.getenv("WHOOP_CLIENT_SECRET")
redirect_url = "http://localhost:3000/callback"
scopes = "read:recovery read:sleep read:workout offline"
state = "12345678910"


def build_auth_url():

    
    params = {
        "client_id": client_id,
        "redirect_url": redirect_url,
        "response_type": "code",
        "scope":scopes,
        "state":state
    }

    request = requests.Request("GET","https://api.prod.whoop.com/oauth/oauth2/auth", params=params)

    return request.prepare().url


def exchange_code_for_tokens(code):

    data = {
        "grant_type" : "authorization_code",
        "code":code,
        "client_id":client_id,
        "client_secret":client_secret,
        "redirect_url":redirect_url,
    }

    post = requests.post("https://api.prod.whoop.com/oauth/oauth2/token", data = data)
    post.raise_for_status()

    return post.json()

print(build_auth_url())
print("What is your code?:")
data = exchange_code_for_tokens(input())
print(data)
    