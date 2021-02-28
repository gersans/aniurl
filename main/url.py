import webbrowser
import requests
import random
from bs4 import BeautifulSoup
from dearpygui.core import *
from dearpygui.simple import *

def urlGenerator():
    urlID = random.randint(1,200000)
    return ''.join(str(urlID))

def charName():
    url='https://anilist.co/character/' + urlGenerator()

    resp=requests.get(url)

    if resp.status_code==200:
        print("Success")
        soup=BeautifulSoup(resp.text,'html.parser')

        if soup.find("h1",{"class":"name"})!=None:
            name=soup.find("h1",{"class":"name"})
            print(name.text)
            return name.text
        else:
            print("Invalid ID")

    else:
        print("error")

def makeList():
    names = None
    characterName = charName()
    
    if characterName != None:
        names = characterName.split()
        return names
    else:
        print('Generate new url')

