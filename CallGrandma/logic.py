from tkinter import *
from contacts_database import Contacts
import pytz
from datetime import datetime
# import datetime
import time
class PersonInfo():
    def __init__(self, name, city):
        self.name = name
        self.city = city
    #add a new person to the list
    def add_new_person(self):
        new_person = Contacts(self.name, self.city)
        new_person.save()
        return new_person
    @classmethod
    def get_city(cls, name):
        city=Contacts.get_by_name(name)
        return city
    @classmethod
    def get_time(cls, name):
        city = PersonInfo.get_city(name)
        timezone = pytz.timezone(f"Europe/{city}")
        current_time =f"{datetime.now(timezone):%H:%M}" 
        message = f"It is {current_time} in {city}."
        return message
    
    
# new_person = PersonInfo('Lila', 'Paris')
# print(new_person.name)
# print(new_person.city)
# new_person.add_new_person()
# get_time()
# print(PersonInfo.get_city('Sara'))
# PersonInfo.get_time('London')
# print(PersonInfo.get_time('Lola')) # works show time

