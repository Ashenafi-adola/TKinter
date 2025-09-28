import requests
from tkinter import *
import json

app = Tk()
app.config(background="#131a24")
app.geometry("1200x650")

apiKey = "a94b5ab426afd7bceddf051bde36cd48"

main = Frame(
    app,
    width=1200,
    height=650,
    bg="#131a24"
) 
main.pack()

def theRegion():
    return Label(
                main,
                width=105,
                height=12,
                bg="#262f3e"
            )

region3 = theRegion()
region3.place(x=20,y=250)

region4 =  theRegion()

region4.place(x=20,y=450)

region5 = Label(
    main,
    width=47,
    height=38,
    bg="#262f3e"
)

region5.place(x=825,y=60)

def master():
    city = search.get()
    if city != '':
        city = city
    else:
        city = "Adama"

    currenturl = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}&units=metric"
    baseUrl = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={apiKey}&units=metric"
    response = requests.get(baseUrl)
    currentResponse = requests.get(currenturl)
    currentWeather = currentResponse.json()
    weather = response.json()

    region2 = Label(
        main,
        width=95,
        height=13,
        bg="#131a24"
    )
    city = Label(
        region2,
        fg='#d8dce5',
        bg="#131a24",
        text=f"{currentWeather['name']}",
        font=("Arial",35,"bold"),
        
    )
    city.place(x=5,y=5)
    cond = Label(
        region2,
        fg="#aeaeae",
        bg="#131a24",
        text=f"{currentWeather["weather"][0]["description"]}",
        font=("Arial",15)
    )
    cond.place(x=5,y=60)

    temp = Label(
        region2,
        text=f'{currentWeather['main']['temp']}°C',
        fg='#d8dce5',
        bg="#131a24",
        font=("Arial",40,"bold"),
        )
    mainIcon = PhotoImage(file=f"{currentWeather["weather"][0]["icon"]}.png")
    icon = Label(
        region2,
        image=mainIcon,
        bg="#131a24",
    )
    icon.place(x=460,y=20)
    temp.place(x=5,y=120)
    region2.place(y=50,x=20)

    def theLabel(temp):
        return Label(
                region3,
                text=temp,
                font=("Arial",12,"bold"),
                height=1,
                width=8,
                padx=1,
                pady=5,
            )

    def info(icon,text):
        return Label(
            region3,
            width=80,
            height=100,
            font=("Arial",12,"bold"),
            text=text,
            image=icon,
            compound="bottom"  
        )
    #=======================================

    Icon1 = PhotoImage(file=f"{weather['list'][0]["weather"][0]['icon']}.png")
    text = f"{weather['list'][0]['dt_txt']}"[-9:-3]
    hour1 = info(Icon1,text)
    hour1.place(x=5,y=40)
    tempratur1 = theLabel(f"{weather['list'][0]['main']['temp']}°C")
    tempratur1.place(x=5,y=145)
    #=======================================

    Icon2 = PhotoImage(file=f"{weather['list'][1]["weather"][0]['icon']}.png")
    text = f"{weather['list'][1]['dt_txt']}"[-9:-3]
    hour2 = info(Icon2,text)
    hour2.place(x=95,y=40)
    tempratur2 = theLabel(f"{weather['list'][1]['main']['temp']}°C")
    tempratur2.place(x=95,y=145)

    #=======================================

    text = f"{weather['list'][2]['dt_txt']}"[-9:-3]
    Icon3 = PhotoImage(file=f"{weather['list'][2]["weather"][0]['icon']}.png")
    hour3 = info(Icon3,text)
    hour3.place(x=185,y=40)
    tempratur3 = theLabel(f"{weather['list'][2]['main']['temp']}°C")
    tempratur3.place(x=185,y=145)

    #=======================================

    text = f"{weather['list'][3]['dt_txt']}"[-9:-3]
    Icon4 = PhotoImage(file=f"{weather['list'][3]["weather"][0]['icon']}.png")
    hour4 = info(Icon4,text)
    hour4.place(x=275,y=40)
    tempratur4 = theLabel(f"{weather['list'][3]['main']['temp']}°C")
    tempratur4.place(x=275,y=145)

    #=======================================

    text = f"{weather['list'][4]['dt_txt']}"[-9:-3]
    Icon5 = PhotoImage(file=f"{weather['list'][4]["weather"][0]['icon']}.png")
    hour5 = info(Icon5,text)
    hour5.place(x=365,y=40)
    tempratur5 = theLabel(f"{weather['list'][4]['main']['temp']}°C")
    tempratur5.place(x=365,y=145)

    #=======================================
    text = f"{weather['list'][5]['dt_txt']}"[-9:-3]
    Icon6 = PhotoImage(file=f"{weather['list'][5]["weather"][0]['icon']}.png")
    hour6 = info(Icon6,text)
    hour6.place(x=455,y=40)
    tempratur6 = theLabel(f"{weather['list'][5]['main']['temp']}°C")
    tempratur6.place(x=455,y=145)

    #=======================================

    text = f"{weather['list'][6]['dt_txt']}"[-9:-3]
    Icon7 = PhotoImage(file=f"{weather['list'][6]["weather"][0]['icon']}.png")
    hour7 = info(Icon7,text)
    hour7.place(x=545,y=40)
    tempratur7 = theLabel(f"{weather['list'][6]['main']['temp']}°C")
    tempratur7.place(x=545,y=145)

    #=======================================
    text = f"{weather['list'][7]['dt_txt']}"[-9:-3]
    Icon8 = PhotoImage(file=f"{weather['list'][7]["weather"][0]['icon']}.png")
    hour8 = info(Icon8,text)
    hour8.place(x=635,y=40)
    tempratur8 = theLabel(f"{weather['list'][7]['main']['temp']}°C")
    tempratur8.place(x=635,y=145)

    #=======================================

region1 = Label(
    main,
    width=900,
    height=2,
    bg="#333a46",
)

search = Entry(
    region1,
    width=110,
    bg="#333a46",
    fg="#FFFFFF",
)
searchButton = Button(
    region1,
    text="Search",
    command=master
)
searchButton.grid(row=0,column=1)
search.grid(column=0,row=0)
region1.place(x=20,y=15)

app.mainloop()