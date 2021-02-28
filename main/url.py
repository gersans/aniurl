import webbrowser
import requests
import random
from bs4 import BeautifulSoup
from dearpygui.core import *
from dearpygui.simple import *

#generate url based on anilist max characters
def urlGenerator():
    urlID = random.randint(1,200000)
    return (str(urlID)

#grab character name from anilist            
def charName():
    url='https://anilist.co/character/' + urlGenerator()
    
    #response from url
    resp=requests.get(url)

    #if response is okay call soup to inspect html
    if resp.status_code==200:
        soup=BeautifulSoup(resp.text,'html.parser')

        #if soup finds and does not equal None set name to what was found
        if soup.find("h1",{"class":"name"})!=None:
            name=soup.find("h1",{"class":"name"})
            return name.text

# makes list based on text found in charName()
def makeList():
    names = None
    characterName = charName()
    
    if characterName != None:
        names = characterName.split()
        return names

