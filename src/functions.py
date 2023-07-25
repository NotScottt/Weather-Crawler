import requests
from bs4 import BeautifulSoup
import threading
from tkinter import messagebox
import re

r = requests.get("https://forecast7.com/de/50d9811d03/erfurt/")
doc = BeautifulSoup(r.content, 'html.parser')
   
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

def get_current_temp():
    threading.Timer(30.0, get_current_temp).start()
    items = [
        item.get_text(strip=True) for item in doc.find_all(class_="hiTemp")
    ]
    return items[0]

#############################################################################################

def get_current_inf():
    threading.Timer(30.0, get_current_inf).start()
    items = [
        item.get_text(strip=True) for item in doc.find_all(class_="summary")
    ]
    return items[1]

#############################################################################################

def show_weather(document):
    messagebox.showinfo("Temperatur", f"Aktuell sind es {getWeatherNow()} und {getConditionNow()}.")


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

def check_weather_ico():
    threading.Timer(30.0, check_weather_ico).start()
    weather = str(getConditionNow())
    if re.search("Regen", weather):
        return True

#############################################################################################

def return_days():

    days = get_day(None)
    temp = get_temp(None) 
    info = get_info(None)
 

    items = []
    for i in range(0, 8):
        days1 = f"{days[i]}:\n{temp[i]}, {info[i]}\n"

        days1 = str(days1)
        items.append(days1)

    items = [str(x) for x in items]
    msg = " \n".join(items)
    return msg

#############################################################################################

def return_x_days(self):
    msg = return_days()
    messagebox.showinfo("Voraussicht", msg)

#############################################################################################

def getWeatherNow():
    items = [
        item.get_text(strip=True) for item in doc.find(class_="current-conditions")
    ]
    return items[1]

#############################################################################################

def getConditionNow():
    items = [
        item.get_text(strip=True) for item in doc.find(class_="current-conditions")
    ]
    return items[3]