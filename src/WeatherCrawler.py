## Imports
from infi.systray import SysTrayIcon
from WeatherFunctions import getItem

menu_options = (("Wetter Heute", None, lambda e: getItem("allInfos")), ("Wetter 7 Tage", None, lambda e: getItem("weatherSevenDays")))

systray = SysTrayIcon("sun.ico", "Scott's Wetter", menu_options)
systray.start()