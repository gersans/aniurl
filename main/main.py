import webbrowser
from dearpygui.core import *
from dearpygui.simple import *

from url import urlGenerator, charName, makeList

def display_name(sender,data):
    fullname = makeList()
    if fullname != None:
        for i in fullname:
            add_button(i, parent="Anime Name Twitter Url", before="Hachi", callback=browserOpen)   

        
def browserOpen(sender,data):
    twituser = 'https://twitter.com/' + sender
    webbrowser.open(twituser)
    delete_button(sender,sender)
    
def delete_button(sender,data):
    delete_item(sender)
    print(sender)

#window settings
set_main_window_size(1200,670)
set_main_window_title("Anilist Twitter")
set_global_font_scale(1)
set_theme("Light")

with window("Anime Name Twitter Url", width=1000, height=590):
    add_button("Generate new character", callback=display_name, callback_data="Some Data")
    set_window_pos("Anime Name Twitter Url",0,0)
    add_drawing("Hachi", width=1280, height=720)

draw_image("Hachi","yep.jpg",[0,0], [1280,720])

start_dearpygui(primary_window="Anime Name Twitter Url")