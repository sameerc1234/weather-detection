from tkinter import *
from tkinter import ttk #to create combo box
import requests #this module gets the info as reqested by user
def data_get():
  city = city_name.get() #assign city_name variable value to city
  data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=267a7df352e04bc0c38c86a102e057c8").json()
  w_label1.config(text=data["weather"][0]["main"]) #though the help of config we can change the value of any variable
  wb_label1.config(text=data["weather"][0]["description"])
  temp_label1.config(text=str(int(data["main"]["temp"]-273.15))) #convert the data into string and add -273.15 so that it will convert thetemp to celcius
  per_label1.config(text=data["main"]["pressure"])
win = Tk() #defining a variable for creating window,till here we will get only plain window
#assigning title for the window
win.title("The Weather Forcaster")
win.config(bg = "blue") #colour for background
win.geometry("500x570")
name_label=Label(win,text="The Weather Forcaster", font=("Time New Roman",30,"bold"))
name_label.place(x=25,y=50,height=50,width=450) #defining a space 
city_name = StringVar() #assigning a city name variable as string
#creating combo box
list_name=["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","Delhi","Puducherry"]
com=ttk.Combobox(win,text = "The Weather Forcaster",values=list_name,font=("Time New Roman",20,"bold"),textvariable=city_name) #designing the combo box and defining a variable for viewing particular city
com.place(x=25,y=120,height=50,width=450) #assigning the length,width and height of combo box
w_label = Label(win,text="Weather Climate", font=("Time New Roman",20)) #defining weather 
w_label.place(x=25,y=260,height=50,width=210)
w_label1 = Label(win,text="", font=("Time New Roman",20)) #to assign a value to weather
w_label1.place(x=250,y=260,height=50,width=210)
wb_label = Label(win,text="Weather Description", font=("Time New Roman",16)) #defining weather  description
wb_label.place(x=25,y=330,height=50,width=210)
wb_label1= Label(win,text="", font=("Time New Roman",17)) #to assign value to weather  description
wb_label1.place(x=250,y=330,height=50,width=210)
temp_label = Label(win,text="Temperature", font=("Time New Roman",20)) #defining temperature 
temp_label.place(x=25,y=400,height=50,width=210)
temp_label1 = Label(win,text="", font=("Time New Roman",20)) #to assign value to  temperature 
temp_label1.place(x=250,y=400,height=50,width=210)
per_label = Label(win,text="Pressure", font=("Time New Roman",20)) #defining pressure
per_label.place(x=25,y=470,height=50,width=210)
per_label1 = Label(win,text="", font=("Time New Roman",20)) #to assign a value to  pressure
per_label1.place(x=250,y=470,height=50,width=210)
done_button=Button(win, text="Done" , font=("Time New Roman",20,"bold"),command=data_get) #creating a done button andcalling declared function
done_button.place(y=190,height=50,width=100,x=200)
win.mainloop()