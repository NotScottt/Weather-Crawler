## Imports
from infi.systray import SysTrayIcon 
import requests
from bs4 import BeautifulSoup
from tkinter import messagebox
import os
import functions

## Static Link
r = requests.get("https://forecast7.com/de/50d9811d03/erfurt/")
doc = BeautifulSoup(r.content, 'html.parser')


menu_options = (("Wetter Heute", None, functions.show_weather(doc)),)
# menu_options = (("Wetter Heute", None, None), ("Wetter 7 Tage", None, None))


if functions.check_weather_ico(functions.strip_item(functions.get_temp(1,))) == True:
    systray = SysTrayIcon("sun.ico", "Scott's Wetter", menu_options)
else:
    systray = SysTrayIcon("rain.ico", "Scott's Wetter", menu_options)

systray.start()