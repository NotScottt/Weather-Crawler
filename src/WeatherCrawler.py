## Imports
from infi.systray import SysTrayIcon
import functions

menu_options = (("Wetter Heute", None, functions.show_weather), ("Wetter 7 Tage", None, functions.return_x_days))

if functions.check_weather_ico(functions.strip_item(functions.get_temp(1))) == True:
    systray = SysTrayIcon("sun.ico", "Scott's Wetter", menu_options)
else:
    systray = SysTrayIcon("rain.ico", "Scott's Wetter", menu_options)

systray.start()