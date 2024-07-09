import tkinter as tk
import requests
from PIL import Image,ImageTk #pip install

root=tk.Tk()

root.title("wearther App")
root.geometry("600x500")   # x not *


def format_response(weather):
    try:
        city=weather["name"]
        condition=weather["weather"][0]["description"]
        temp=weather["main"]["temp"]
        final_str="City:%s\nCondition:%s\nTemprature:%s"%(city,condition,temp)
    except:
        final_str="There was a problem retreiving that information"
    return final_str



def get_weather(city):  #key and API taken from - https://openweathermap.org/api
    weather_key="82c6d500e448d4db5f61928ee567d3b1"
    url="https://api.openweathermap.org/data/2.5/weather"
    params={"appid":weather_key , "q":city , "units":"imperial"} #If you do not use the units parameter, standard units will be applied by default.
    response=requests.get(url , params)
#    print(response.json()) #hsion use to send text data to network
    weather=response.json()
    #print(weather["name"])  #these 3 prints use to print value in vsc-output
    #print(weather["weather"][0]["description"])
    #print(weather["main"]["temp"])

    result["text"]=format_response(weather)

    icon_name=weather["weather"][0]["icon"]
    open_image(icon_name)

def open_image(icon):
    size=int(frame_two.winfo_height()*0.25)
    img=ImageTk.PhotoImage(Image.open("./img/"+icon+".png").resize((size,size)))
    weather_icon.delete("all")
    weather_icon.create_image(0,0,anchor="nw",image=img)
    weather_icon.image=img



img=Image.open("./img1.png")
img=img.resize((600,500),Image.LANCZOS) #LANC. covert high level images into low level
                                        #Remenber- ANTIALIAS is now replace by LANCZOS
img_photo=ImageTk.PhotoImage(img)

bg_label=tk.Label(root , image=img_photo)
bg_label.place(x=0 , y=0 , width=600 , height=500)

heading_title=tk.Label(bg_label , text="Earth including over 200000 cities" , fg="red",bg="skyblue", font=("Arial" , 18 , "bold"))
heading_title.place(x=80,y=18)

#frame on image-blue color
frame_one=tk.Frame(bg_label , bg="skyblue" , bd=5)
frame_one.place(x=80 , y=60 , width=450 , height=50)

#entry field - in white color
txt_box=tk.Entry(frame_one , font=("Arial" , 25) , width=17)
txt_box.grid(row=0,column=0,sticky="w")

#for button
btn=tk.Button(frame_one,text="Get",fg="green" ,font=("Arial",16,"bold"),command=lambda: get_weather(txt_box.get()))
btn.grid(row=0 , column=1,padx=30)

#second frame to show data 
frame_two=tk.Frame(bg_label , bg="skyblue" , bd=5)
frame_two.place(x=80 , y=130 , width=450 , height=300)

#label on frame 
result=tk.Label(frame_two,font=40,bg="white" , justify="left",anchor="nw") #nw=north-west
result.place(relwidth=1,relheight=1) #where rel of w and h is making relation with it's parent(frame_two) and adjust with-respective to frame2

weather_icon=tk.Canvas(result,bg="white",bd=0,highlightthickness=0)
weather_icon.place(relx=.75,rely=0,relwidth=1,relheight=0.5)

root.mainloop()