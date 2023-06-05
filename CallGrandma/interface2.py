from tkinter import *
from logic import *
from datetime import datetime
from PIL import *
import pytz

def add_person(name, city):
    new_person = PersonInfo(name, city)
    name_to_list = new_person.name
    new_person.add_new_person()
    return new_person

def save_contact():
    name = name_entry.get()
    city = city_entry.get()

    if name !='' and city !='':
        add_person(name, city)
        timeInfo.config(text="Contact saved!")
    else:
        timeInfo.config(text="Something wrong")
    # else:
    #     timeInfo.config(text="Name already exists!")
    
def find_contact():
    name = name_entry
    city = PersonInfo.get_city(name)
    message = PersonInfo.get_time(name) # Works in logic file
    return message
nice_message = find_contact()
# nice_message = 'Time to call'

root = Tk()
root.geometry("350x300")
root.configure(bg = "#ffffff")
root.iconbitmap('CallGrandma/logo.ico')
root.title('Call Grandma')
canvas = Canvas(root, bg = "#ffffff", height = 300, width = 350, bd = 0, highlightthickness = 0, relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = "CallGrandma/background.png")
background = canvas.create_image(175.0, 150.0, image=background_img)
        
    #*****get info from user*****#
global name_entry
name_entry = Entry(bd = 0, highlightthickness = 0, fg = 'gray')
name_entry.bind("<Button-1>", save_contact)
name_entry.place(x = 65.0, y = 103, width = 100.0, height = 35)       
city_entry = Entry(bd = 0, highlightthickness = 0, fg = 'gray')

city_entry.bind("<Button-1>", save_contact)
city_entry.place(x = 185.0, y = 103, width = 100.0, height = 35)
timeInfo = Label(root, bg = 'white', text= nice_message, fg="#FC1BAD",  font = 14)
timeInfo.place(x = 65.0, y = 211, width = 220.0, height = 35)

#*****button to add information*****#
button_img_add=PhotoImage(file="CallGrandma/button_img_add.png")
button_add = Button(root, image=button_img_add, border=0, highlightthickness = 0, activebackground="white", command = save_contact)
button_add.place(x=65, y=157)

#*****button to check time*****#
button_img_check=PhotoImage(file="CallGrandma/button_img_check.png")
button_check = Button(root, image=button_img_check, highlightthickness = 0, border=0, activebackground="white", command = find_contact)
button_check.place(x=185, y=157)

root.resizable(False, False)
root.mainloop()