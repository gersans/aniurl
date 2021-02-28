import webbrowser
from dearpygui.core import *
from dearpygui.simple import *

from url import urlGenerator, charName, makeList

# display name on clicking button "Generate new character"
def display_name(sender,data):
    fullname = makeList()
    # if fullname is not NoneType
    if fullname != None:
        #for every word in fullname add button before image "Hachi" that calls browserOpen on click
        for i in fullname:
            add_button(i, parent="Anime Name Twitter Url", before="Hachi", callback=browserOpen)   

# on "name click open browser        
def browserOpen(sender,data):
    #make url based on sender name and concate to twitter url
    twituser = 'https://twitter.com/' + sender
    webbrowser.open(twituser)
    #on browser open delete button
    delete_button(sender,sender)
    
# function to delete button    
def delete_button(sender,data):
    delete_item(sender)
    print(sender)

#window settings
set_main_window_size(1200,670)
set_main_window_title("Anilist Twitter")
set_global_font_scale(1)
set_theme("Light")

#main window
with window("Anime Name Twitter Url", width=1000, height=590):
    add_button("Generate new character", callback=display_name, callback_data="Some Data")
    set_window_pos("Anime Name Twitter Url",0,0)
    add_drawing("Hachi", width=1280, height=720)

draw_image("Hachi","yep.jpg",[0,0], [1280,720])

start_dearpygui(primary_window="Anime Name Twitter Url")
