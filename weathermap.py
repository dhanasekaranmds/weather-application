from tkinter import *
from tkinter import messagebox
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

api = "http://api.openweathermap.org/data/2.5/weather?q={}&appid=f8a835bb6a974f36d40afd2c9332ed7b"
json_data=requests.get(api).json()


def getweather(city):
    result = requests.get(api.format(city))

    if result:
        json = result.json()
        city = json['name']
        country = json['sys']
        temp_kelvin = json['main']['temp']
        temp_celsius = temp_kelvin - 273.15
        weather1 = json['weather'][0]['main']
        pressure=json['main']['pressure']
        humidity=json['main']['humidity']
        final = [city, country, temp_kelvin,
                 temp_celsius, weather1,humidity,pressure]
        return final
    else:
        print("NO Content Found")

def search():
    city = city_text.get()
    weather = getweather(city)
    geolocator = Nominatim(user_agent="geoapiExcercises")
    location = geolocator.geocode(city)
    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
    print(result)
    if weather:
        location_lbl['text'] = '{} ,{}'.format(weather[0], weather[1])
        temperature_label['text'] = str(weather[3]) + " Degree Celsius"
        weather_l['text'] = weather[4]
    else:
        messagebox.showerror('Error', "Cannot find {}".format(city))

app = Tk()
app.title("Weather App")
app.geometry("700x500")
city_text = StringVar()
city_entry = Entry(app, textvariable=city_text)
city_entry.place(x=200,y=30)
Search_btn = Button(app, text="Search Weather",
                    width=12, command=search)
Search_btn.place(x=200,y=60)
location_lbl = Label(app, text="Location", font={'bold', 20})
location_lbl.place(x=100,y=90)
temperature_label = Label(app, text="")
temperature_label.place(x=100,y=120)
weather_l = Label(app, text="")
weather_l.place(x=100,y=150)
app.mainloop()