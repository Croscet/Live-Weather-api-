from tkinter import *
from tkinter import messagebox
import requests
from timezonefinder import TimezoneFinder
from datetime import datetime
import pytz

def search():
    city=text_name.get('1.0',END)
    API_KEY =
    #insert  api key
    URL = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(URL)

    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']

        temp_label2.config(text=temp)
        feels_lik=data['main']['feels_like']
        feels_like2.config(text=feels_lik)

        data = response.json()
        weather = data['weather'][0]['description']

        weather_label2.config(text= weather)


        City_label.config(text='Location Name : -----         '+city.capitalize()+'                        ')

        pressure = data['main']['pressure']
        pressure_label2.config(text=pressure)

        lat=data['coord']['lat']
        longitude =data['coord']['lon']
        tf=TimezoneFinder()
        timezone_str = tf.timezone_at(lat=lat, lng=longitude)


        timezone = pytz.timezone(timezone_str)
        local_time = datetime.now(timezone)

        time_label.config(text=local_time.strftime(' %I:%M:%S %p %Z'))

    else:
        messagebox.showerror(message='Error,Could not find any location!!!',title='ERROR!!!!')

win=Tk()

ima1=PhotoImage(file='Capture.png')

win.geometry('800x1500')
win.title('Weather app ')
win.config(bg='#78c0c9')
label1=Label(win,text='     Weather    Information    ',font=('Times',30,'italic'),bg='light green')
label1.pack()

frame=Frame(win,bg='light green')
frame.place(x=250,y=100)

label2=Label(frame,text='Enter Location -------',font=('Times',25),bg='light green')
label2.grid(row=0,column=0,padx=40)

text_name=Text(frame,font=('Arial,20'),width=40,height=1.25)
text_name.grid(row=0,column=1,padx=10)
text_name.focus()

button=Button(frame,image=ima1,width=35,height=30,command=search)
button.grid(row=0,column=2)
excess=Label(frame,text='     ',bg='light green').grid(row=0,column=3)
display=Label(win,height=21,bg='#78c0c9' ,width=90)
display.place(x=400,y=400)

display1=Label(win,height=20,width=100,bg='#78c0c9')
display1.place(x=450,y=300)


City_label=Label(display1,text='',font=('Times',15,'italic','bold'),fg='purple',bg='#78c0c9')
City_label.grid(row=0,column=1)

time_label=Label(display1,text='',font=('Times',15,'italic','bold'),fg='navy blue',bg='#78c0c9')
time_label.grid(row=1,column=1)

temp_label=Label(display,text='Temperature :',font=('Times',15),bg='#78c0c9')
temp_label.grid(row=2,column=0,padx=40)

temp_label2=Label(display,font=('Arial,20'),width=15,height=1)
temp_label2.grid(row=2,column=1,padx=10)

cent_text1=Label(display,text=' °C ',font=('Times',15),bg='#78c0c9')
cent_text1.grid(row=2,column=2,padx=5)

weather_label=Label(display,text='Weather :',font=('Times',15),bg='#78c0c9')
weather_label.grid(row=1,column=0,padx=40,pady=10)

weather_label2=Label(display,font=('Arial,20'),width=25,height=1)
weather_label2.grid(row=1,column=1,padx=10)

pressure_label=Label(display,text='Pressure  : ',font=('Times',15),bg='#78c0c9')
pressure_label.grid(row=4,column=0,padx=40,pady=10)

pressure_label2=Label(display,font=('Arial,20'),width=15,height=1)
pressure_label2.grid(row=4,column=1,padx=10)

feels_like=Label(display,text='Feels like  : ',font=('Times',15),bg='#78c0c9')
feels_like.grid(row=3,column=0,padx=40,pady=10)

feels_like2=Label(display,font=('Arial,20'),width=15,height=1)
feels_like2.grid(row=3,column=1,padx=10)

cent_text2=Label(display,text=' °C ',font=('Times',15),bg='#78c0c9')
cent_text2.grid(row=3,column=2,padx=5)

win.mainloop()
