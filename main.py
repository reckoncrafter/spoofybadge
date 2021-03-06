#! /usr/bin/python3
import json
import requests
import shutil
import os
from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color

## Retriving Spotify API
try:
    OAUTH_TOKEN = open("OAUTH", "r")
except:
    print("Please create OAUTH file")
    exit()

OAUTH_TOKEN = OAUTH_TOKEN.read()
OAUTH_TOKEN = OAUTH_TOKEN.strip()

if not OAUTH_TOKEN:
    print("No OAuth token found! Please retrive one from")
    print("https://developer.spotify.com/console/get-users-currently-playing-track/")
    print("and place it in the OAUTH file")
    exit()

url = "https://api.spotify.com/v1/me/player/currently-playing"
headers = {'Accept':'application/json', 'Content-Type':'application/json', "Authorization":"Bearer " + OAUTH_TOKEN}
js = requests.get(url, headers=headers)
try:
	js = js.json()
except:
    print(js)
    print("Make sure a song is playing!")
    exit()

## Parsing JSON

try:
    artist = js["item"]["album"]["artists"][0]["name"]
    album_art = js["item"]["album"]["images"][0]["url"]
    title = js["item"]["name"]

    print(title)
    print(artist)
    print(album_art)
except:
    try:
        error = js["error"]["status"]
        if(error == 401):
            print("Your OAUTH token has expired!")
            print("https://developer.spotify.com/console/get-users-currently-playing-track/")
    except:
        print(js)

    exit()

if(len(title) > 25):
    title = title[0:23] + "..."

if(len(artist) > 25):
    artist = artist[0:23] + "..."

## Pulling image

rsp = requests.get(album_art, stream=True)
with open('albumart.bmp', 'wb') as out_file:
    shutil.copyfileobj(rsp.raw, out_file)
del rsp


## Generating bitmap

aart = Image(filename = 'albumart.bmp')
aart.resize(100,100)

with Drawing() as draw:
    with Image(width=400, height=100, background='white') as img:
        draw.font = "FreeMonoBold.otf"
        #            ^ change path to font here
        draw.font_size = 18
        draw.text(110, 25, title)
        #          /\   /\
        #          x    y
        #          \/   \/
        draw.text(110, 50, artist)
        draw(img)

        img.composite(aart, left=0, top=0)
        img.save(filename='badge.png')

