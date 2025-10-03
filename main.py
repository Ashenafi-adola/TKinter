import requests
from tkinter import *
from datetime import datetime

app = Tk()
app.config(background="#131a24")
app.geometry("1200x650")
app.title("Weather")
apiKey = "a94b5ab426afd7bceddf051bde36cd48"
main = Frame(
    app,
    width=1200,
    height=650,
    bg="#131a24"
) 
main.pack()
def Region():
    return Label(
                main,
                width=105,
                height=12,
                bg="#262f3e"
            )

def theLabel(temp):
    return Label(
            region3,
            text=temp,
            font=("Arial",12,"bold"),
            height=1,
            width=8,
            fg='#d8dce5',
            bg="#151d2c",
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
        compound="bottom",
        fg='#d8dce5',
        bg="#151d2c"
    )

def dailyCondition(icon,text):
    return Label(
        region5,
        width=140,
        height=88,
        image=icon,
        text=text,
        compound="right",
        fg='#d8dce5',
        bg="#151d2c",
        font=("Arial",12,"bold"),
        padx=10
    )

def dailyWeather(condition,temp_max,temp_min):
    return Label(
        region5,
        width=23,
        height=6,
        text=f" {condition}         {temp_max} / {temp_min}",
        font=("Arial",9),
        fg='#d8dce5',
        bg="#151d2c",
        padx=0,
        pady=0,
    )

hourly_icons = [0,0,0,0,0,0,0,0]
daily_icons = [0,0,0,0,0]
daily_text = []
hourly_text = []

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
    heading = Label(
        region3,
        text="TODAY'S FORECAST",
        fg='#d8dce5',
        bg="#262f3e"
    )
    heading.place(x=2,y=4)

    heading = Label(
        region4,
        text="AIR CONDITION",
        fg='#d8dce5',
        bg="#262f3e"
    ) 
    heading.place(x=2,y=4)

    for i in range(8):
        icon = PhotoImage(file=f"{weather['list'][i]["weather"][0]['icon']}.png")
        text = f"{weather['list'][i]['dt_txt']}"[-9:-3]
        hourly_icons[i] = icon
        hourly_text.append(text)
        hour = info(hourly_icons[i],hourly_text[i])
        hour.place(x=5 + i*90,y=40)
        tempratur1 = theLabel(f"{weather['list'][i]['main']['temp']}°C")
        tempratur1.place(x=5 + i*90,y=145)

    mainIcon = PhotoImage(file=f"{currentWeather["weather"][0]["icon"]}.png")
    hourly_icons.append(mainIcon)
    icon = Label(
        region2,
        image=hourly_icons[8],
        bg="#131a24",
    )
    icon.place(x=460,y=20)
    temp.place(x=5,y=120)
    region2.place(y=50,x=20)

    for i in range(5):
        icon = PhotoImage(file=f"{weather['list'][i*8]["weather"][0]['icon']}.png")
        text = f"{weather['list'][i*8]['dt_txt']}"[:10]
        date = datetime.strptime(text, "%Y-%m-%d").strftime("%A")
        daily_icons[i] = icon
        daily_text.append(date)
        day = dailyCondition(hourly_icons[i],daily_text[i])
        condtions = dailyWeather(weather['list'][i*8]['weather'][0]['description'],str(weather['list'][i*8]['main']['temp_max'])[:2],str(weather['list'][i*8]['main']['temp_min'])[:2])
        condtions.place(x=170,y=5 + i*115)
        day.place(x=10,y=5 + i*115)

    temp = PhotoImage(file="temp.png")
    daily_icons.append(temp)
    temp_feel = Label(
        region4,
        image=daily_icons[5],
        bg="#262f3e",
        text="Real feel",
        fg="#B1B1B1",
        compound="left",
        font=("Arial",12,"bold")
    )
    temp_feel.place(x=10,y=30)

    realFeel = Label(
        region4,
        text=f"{weather['list'][i*8]['main']['feels_like']}°C",
        bg="#262f3e",
        fg="#acaaaa",
        font=("Arial",24,"bold")
    )

    realFeel.place(x=10,y=70)
    windSpeed = Label(
        region4,
        text=f"{weather['list'][i*8]['wind']['speed']} Km/h",
        bg="#262f3e",
        fg="#acaaaa",
        font=("Arial",24,"bold")
    )
    windSpeed.place(x=400,y=70)
#-------------------end of function------------
region3 = Region()

region3.place(x=20,y=250)
region4 =  Region()

temp = PhotoImage(file="temp.png")
temp_feel = Label(
    region4,
    image=temp,
    bg="#262f3e",
    text="Real feel",
    fg="#B1B1B1",
    compound="left",
    font=("Arial",12,"bold")
)
temp_feel.place(x=10,y=30)

wind = PhotoImage(file="wind.png")
wind_speed = Label(
    region4,
    image=wind,
    bg="#262f3e",
    text="wind speed",
    fg="#acaaaa",
    compound="left",
    font=("Arial",12,"bold")
)
wind_speed.place(x=400,y=30)
region4.place(x=20,y=450)

region5 = Label(
    main,
    height=38,
    width=53,
    bg="#262f3e",
)

region5.place(x=790,y=60)

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