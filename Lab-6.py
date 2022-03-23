# Program written by Brandan Wood COMP 593 Lab 6
# Description: Uses functions and requests modules to paste pokemon abilities to PasteBin.
# Run with: Python Lab-6.py param
# Param = name of a pokemon

# lab 6 poke api stuff

import sys
import requests

# working with python functions
def pokemon1(pokename):
    print("Getting pokemon info...")
    pokenameurl = 'https://pokeapi.co/api/v2/pokemon/' + pokename  # puts pokemon name into the url
    r = requests.get(pokenameurl)  # storing request into r variable

    if r.status_code == 200:
        print('Successful!')
        return r.json()
    else:
        print("Failed to obtain pokemon info, Code: " + str(r.status_code))
        return

pokename = sys.argv[1]  # argv for pokemon name
jsonData = pokemon1(pokename)

def pastestuff():
    title = pokename.capitalize() + "'s Abilities"
    body = ""
    for ability in jsonData['abilities']:  # takes json dictionary and loops through it to get ability names
        body += "- " + ability['ability']['name'] + "\n"
    body = body[:-1]
    pastelist = [title, body]
    return pastelist

pokebody = pastestuff()[1]
poketitle = pastestuff()[0]

# pastebin stuff
def pastebin(title, body):
    header = {'Content-Type': 'application/x-www-form-urlencoded'}
    pasteBinApi = "f4R0OTFza_qTQ1NZJYLjoCeLqoHQux4X"
    requestParams = {
        'api_dev_key': pasteBinApi,
        'api_option': 'paste',
        'api_paste_code': body,
        'api_paste_name': title
    }
    rp = requests.post('https://pastebin.com/api/api_post.php', data=requestParams, headers=header)
    print("Pasting data to Pastebin...")
    if rp.status_code == 200:
        print("Paste Successful!")
        return print(rp.text)
    else:
        print("Paste failed! Code: " + str(rp.status_code))


pastebin(poketitle, pokebody)