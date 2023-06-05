# from tkinter import *
# from logic import *
# from PIL import *

# class Window():
#     # text_placeholder='Enter a name'
#     nice_message='Have a nice day!'
    
#     def __init__(self) -> None:
        
#         pass
#     @classmethod
#     def add_person(cls, name, city):
#         new_person = PersonInfo(name, city)
#         input_name = new_person.name
#         input_city=new_person.city #To check time
#         new_person.add_new_person()
#         return new_person
    
#     @classmethod
#     def check_click(cls):
#         # cls.text_placeholder = 'Enter a name'
#         name = 'Berta'
#         city = 'London'
#         city=PersonInfo.get_city(name)
#         time =PersonInfo.get_time(city)
        
#         nice_message = f'It\'s {time} in {city}. To late to call.'
#         print('check_click')
#         print(nice_message)
        
#     @classmethod
#     def add_click(cls):
#         # cls.text_placeholder='!!!!'

#         # if cls.text_placeholder=='Enter a name': 
#         #     cls.text_placeholder == 'Enter a city'
#         # else:
#         #     cls.text_placeholder=='Enter a name'
#         # add_person('Ron', 'Budapest')
#         print('add_click')
#         # return cls.text_placeholder
        
#     #placeholder
        
        
#     def draw_interface(self, nice_message='Have a nice day!'):
#         root = Tk()
#         root.geometry("350x300")
#         root.configure(bg = "#ffffff")
#         root.iconbitmap('CallGrandma/logo.ico')
#         root.title('Call Grandma')
#         canvas = Canvas(root, bg = "#ffffff", height = 300, width = 350, bd = 0, highlightthickness = 0, relief = "ridge")
#         canvas.place(x = 0, y = 0)

#         background_img = PhotoImage(file = "CallGrandma/background.png")
#         background = canvas.create_image(175.0, 150.0, image=background_img)
#         # user_input_img = PhotoImage(file = "CallGrandma/user_input_img.png")
        
#         #*****get info from user*****#
#         name_input = Entry(bd = 0, highlightthickness = 0, fg = 'gray')
#         name_input.insert(0, 'Enter a name')
#         # name_input.delete(0, 'end')
#         name_input.bind("<Button-1>", Window.add_click)
#         name_input.place(x = 65.0, y = 103, width = 100.0, height = 35)
#         name=name_input.get()
        
#         city_input = Entry(bd = 0, highlightthickness = 0, fg = 'gray')
#         city_input.insert(0, 'Enter a city')
#         # city_input.delete(0, 'end')
#         city_input.bind("<Button-1>", Window.add_click)
#         city_input.place(x = 184.0, y = 103, width = 100.0, height = 35)
#         city=name_input.get()
#         print(name, city)
#         timeInfo = Label(root, bg = 'white', text= Window.nice_message, fg='red',  font = 24)
#         timeInfo.place(x = 65.0, y = 211, width = 220.0, height = 35)

#         #*****button to add information*****#
#         button_img_add=PhotoImage(file="CallGrandma/button_img_add.png")
#         button_add = Button(root, image=button_img_add, bg="#FB2E91", border=0, highlightthickness = 0, activebackground="white", command = Window.add_click)
#         button_add.place(x=65, y=157)

#         #*****button to check time*****#
#         button_img_check=PhotoImage(file="CallGrandma/button_img_check.png")
#         button_check = Button(root, image=button_img_check, highlightthickness = 0, bg="#FB2E91", border=0, activebackground="white", command = Window.check_click)
#         button_check.place(x=185, y=157)

#         root.resizable(False, False)
#         root.mainloop()

# text_placeholder = 'Enter a city'
# nice_message = f'To late to call.'

# # draw_interface(text_placeholder, nice_message)

# # new_person = PersonInfo('Loran', 'Tel Aviv')
# # print(new_person.name)
# # print(new_person.city)
# # new_person.add_new_person()

# window1=Window()
# window1.draw_interface()