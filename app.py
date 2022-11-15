import requests
from googletrans import Translator, constants
from pprint import pprint
from bs4 import BeautifulSoup
from tkinter import *

trs = Translator()
root = Tk()
root.geometry('500x400')
root.title("Weather App With Python")
cityName = Label(
    root,
    text = "شهر مورد نظر را وارد کنید"
).pack()

cityNameEntry = Entry(root)
cityNameEntry.pack()

choosed = StringVar()

choosed.set('یک گزینه را انتخاب کنید')


def dataSave():
    global url
    city = cityNameEntry.get()
    degree = choosed.get()
    url = '''
    https://www.google.com/search?q=weather+{}+{}&rlz=1C1GGRV_enIR901IR901&oq=weather+{}+{}&aqs=chrome..69i57j0i512j0i22i30j0i10i22i30j0i22i30j0i15i22i30j0i22i30l2.5026j0j7&sourceid=chrome&ie=UTF-8
    '''.format(city, degree, city, degree)
    UrlProcess()


degreeMenu = OptionMenu(
    root,
    choosed,
    "Celsius",
    "FarenHeit"
)
degreeMenu.pack()


def UrlProcess():
    global weatherStats
    mainSource = requests.get(url)

    content = BeautifulSoup(mainSource.content, 'html.parser')

    cityName = content.find('span', class_= 'BNeawe tAd8D AP7Wnd')
    dateWithWeatherStatus = content.find('div', class_= 'BNeawe tAd8D AP7Wnd')
    degree = content.find('div', class_= 'BNeawe iBp4i AP7Wnd')
    
    trs_city = trs.translate(cityName.text, "fa")
    trs_date = trs.translate(dateWithWeatherStatus.text, "fa")

    weatherStats = Label(
        root,
        text = "شهر : {}\n\nوضعیت / تاریخ : {}\n\nدرجه هوا : {}".format(
            trs_city.text, 
            trs_date.text,
            degree.text
        )
    )
    weatherStats.pack()

    getWeatherButton['state'] = DISABLED
    deleteButton['state'] = NORMAL


def statsDelete():
    weatherStats.destroy()
    getWeatherButton['state'] = NORMAL
    deleteButton['state'] = DISABLED


getWeatherButton = Button(
    root,
    text = "مشاهده نتیجه",
    bg = 'green',
    fg = 'white',
    command = dataSave
)
getWeatherButton.pack()

deleteButton = Button(
    root,
    text = "حذف نتایج قبلی",
    bg = 'red',
    fg = 'white',
    command = statsDelete
)
deleteButton.pack()

root.mainloop()