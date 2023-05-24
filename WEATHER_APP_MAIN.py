import tkinter as tk
import requests
from PIL import ImageTk, Image
import weather_icons

app = tk.Tk()
app.iconbitmap(True,"window_icon.ico")
app.title("Weather")

HEIGHT = 500
WIDTH = 600

def format_response(weather_json):

    try:

        city = weather_json['name']
        conditions = weather_json['weather'][0]['description']
        temp = weather_json['main']['temp']
        feels_like = weather_json['main']['feels_like']
        humidity = weather_json['main']['humidity']
        final_str = 'City: %s \nConditions: %s \nTemperature (°C): %s \nFeels Like: %s \nHumidity: %s' % (city, conditions, temp, feels_like, humidity)
    
    except:
        final_str = 'There was a problem retrieving that information'
    
    return final_str

#api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}

def get_weather(city):

    weather_key = 'cf160e479cbea7bff8c1d6e072c8263a'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units':'metric'}
    response = requests.get(url, params=params)
    weather_json = response.json()

    results['text'] = format_response(weather_json)

    icon_name = weather_json['weather'][0]['icon']
    open_image(icon_name)

def open_image(icon):
    size = int(lower_frame.winfo_height()*0.25)
    img = ImageTk.PhotoImage(Image.open('./img/'+icon+'.png').resize((size, size)))
    weather_icon.delete("all")
    weather_icon.create_image(0,0, anchor='nw', image=img)
    weather_icon.image = img

C = tk.Canvas(app, height=HEIGHT, width=WIDTH)
C.pack()

background_image = ImageTk.PhotoImage(Image.open("C:\\Users\\SHINJINI\\weather_app\\los_angeles.png"))
bgl=tk.Label(app,image=background_image)
bgl.place(x=0,y=0,relwidth=1,relheight=1)


frame = tk.Frame(app,bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

textbox = tk.Entry(frame, font=40,bg='#ffe6f9')
textbox.place(relwidth=0.65, relheight=1)

submit = tk.Button(frame, text='Get Weather', font=('Courier',12,'bold'),command=lambda: get_weather(textbox.get()))
submit.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(app, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

bg_color='#ffe6ff'
results = tk.Label(lower_frame, anchor='nw', justify='left', bd=4)
results.config(font=40, bg=bg_color)
results.place(relwidth=1, relheight=1)

weather_icon = tk.Canvas(results, bg=bg_color, bd=0, highlightthickness=0)
weather_icon.place(relx=.75, rely=0, relwidth=1, relheight=0.5)

app.mainloop()