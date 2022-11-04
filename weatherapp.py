from tkinter import*
import tkinter as tk
import time
import requests
def getweather():
    city=textfield.get()
    data="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=d73567c89c1811de1330d178a3b1cd94"
    jdt=requests.get(data).json()
    condition=jdt['weather'][0]['main']
    temp=int(jdt['main']['temp']-273.15)
    max_temp=int(jdt['main']['temp_max']-273.15)
    min_temp=int(jdt['main']['temp_min']-273.15)
    pressure=jdt['main']['pressure']
    humidity=jdt['main']['humidity']
    wind=jdt['wind']['speed']
    sunrise=time.strftime("%I:%M:%S",time.gmtime(jdt['sys']['sunrise']-19800))
    sunset=time.strftime("%I:%M:%S",time.gmtime(jdt['sys']['sunset']-19800))

    info=condition+"\n"+str(temp)+"°C"
    rest="\n"+"Max Temp:"+str(max_temp)+"°C"+"\n"+"Min Temp:"+str(min_temp)+"°C"+"\n"+"Pressure:"+ str(pressure) + "\n"+"Humidity: " + str(humidity) + "\n" +"Wind Speed: " + str(wind) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset
    l1.config(text=info)
    l2.config(text=rest)
w=Tk()
w.title("WEATHER APP")
w.config(bg="aqua")
w.geometry("600x500")
textfield=tk.Entry(w,font=("New Roman",20,"italic"))
textfield.place(y=20,x=150)
textfield.focus()
b1=tk.Button(w,text="FETCH",bg='yellow',foreground='blue',command=getweather)
b1.place(x=280,y=70)
photo=PhotoImage(file="weather.png")
label=Label(w,bg='aqua',image=photo)
label.place(x=230,y=100)
l1=tk.Label(w,fg='red',bg='aqua',font=("poppins",20,"bold"))
l1.place(y=215,x=260 )
l2=tk.Label(w,bg='aqua',font=("poppins",15))
l2.place(y=282,x=215)
w.mainloop()