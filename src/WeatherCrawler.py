## Imports
from infi.systray import SysTrayIcon 
import requests
from bs4 import BeautifulSoup
from tkinter import messagebox
import os

## Static Link
r = requests.get("https://forecast7.com/de/50d9811d03/erfurt/")
doc = BeautifulSoup(r.content, 'html.parser')


#############################################################################################

def get_temp(num):
    items = [
        item.get_text(strip=True) for item in doc.find_all(class_="hiTemp")
    ]
    if num == None:
        return items
    else:
        return items[num]
    
#############################################################################################

def get_info(num):
    items = [
        item.get_text(strip=True) for item in doc.find_all(class_="summary")
    ]
    if num == None:
        return items
    else:
        return items[num]

#############################################################################################

def get_day(num):
    items = [
        item.get_text(strip=True) for item in doc.find_all(class_="time")
    ]
    if num == None:
        return items
    else:
        return items[num]

#############################################################################################

def strip_item(item):
    item = str(item).replace("°C", "")
    return item

#############################################################################################

def check_weather_ico(temp):
    if int(temp) < 15:
        return False
    else:
        return True

#############################################################################################

def show_weather(num):
    messagebox.showinfo("Temperatur", f"Heute werden es {get_temp(0)} und {get_info(1)}.")

#############################################################################################

def return_x_days(self):
    days = get_day(None)
    temp = get_temp(None)
    info = get_info(None)

    items = []
    for i in range(0, 8):
        days1 = f"{days[i]} {temp[i]}, {info[i]}"
        days1 = str(days1)
        items.append(days1)

    items = [str(x) for x in items]
    msg = " \n".join(items)

    messagebox.showinfo("Voraussicht", msg)

#############################################################################################
 
menu_options = (("Wetter Heute", None, show_weather), ("Wetter 7 Tage", None, return_x_days))


pictures = [
    item.get_text(strip=True) for item in doc.find_all(class_="icons")
]

if check_weather_ico(strip_item(get_temp(1))) == True:
    systray = SysTrayIcon("sun.ico", "Scott's Wetter", menu_options)
else:
    systray = SysTrayIcon("rain.ico", "Wetter", menu_options)

systray.start()