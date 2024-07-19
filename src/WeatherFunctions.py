from requests import get as RqGet
from bs4 import BeautifulSoup
from tkinter import messagebox

def getItem(item):
    r = RqGet("https://forecast7.com/de/50d9811d03/erfurt/")

    if r.status_code == 200:
        doc = BeautifulSoup(r.content, 'html.parser')

        items = [
            item.get_text(strip=True) for item in doc.find(class_="current-conditions")
        ]

        def getExtraInfo(value, num):
            items = [item.get_text(strip=True) for item in doc.find_all(class_=value)]
            if num == None:
                return items
            else:
                return items[num]

        match item:
            case "allInfos":
                currentWeather = items[1]
                currentCond = items[3]

                messagebox.showinfo("Temperatur", f"Aktuell sind es {currentWeather} und {currentCond}.")

            case "weatherSevenDays":
                days = getExtraInfo("time", None)
                temp = getExtraInfo("hiTemp", None) 
                info = getExtraInfo("summary", None)

                items = []
                for i in range(0, 8):
                    
                    days1 = f"{days[i]}:\n{temp[i]}, {info[i+1]}\n"

                    days1 = str(days1)
                    items.append(days1)

                items = [str(x) for x in items]
                msg = " \n".join(items)
                
                messagebox.showinfo("Vorraussicht", msg)
    else:
        messagebox.showerror("Fehler", "Es gab einen Fehler bei der Wetterapp. Versuchen Sie es später erneut.")