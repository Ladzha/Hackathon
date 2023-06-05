import tkinter as tk
import sqlite3
from datetime import datetime

# Connect to the SQLite database
conn = sqlite3.connect("contacts.db")
cursor = conn.cursor()

# Create a table to store contacts if it doesn't exist
cursor.execute("CREATE TABLE IF NOT EXISTS contacts (name TEXT PRIMARY KEY, city TEXT)")

def save_contact():
    name = name_entry.get()
    city = city_entry.get()

    cursor.execute("SELECT * FROM contacts WHERE name=?", (name,))
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO contacts VALUES (?, ?)", (name, city))
        conn.commit()
        status_label.config(text="Contact saved successfully!")
    else:
        status_label.config(text="Name already exists! Enter a different name.")

def find_contact():
    name = name_entry.get()

    cursor.execute("SELECT city FROM contacts WHERE name=?", (name,))
    result = cursor.fetchone()

    if result is not None:
        city = result[0]
        try:
            current_time = datetime.now().strftime("%H:%M:%S")
            message = f"{name} lives in {city}. Current time in {city} is {current_time}."
            status_label.config(text=message)
        except pytz.UnknownTimeZoneError:
            status_label.config(text=f"Timezone for {city} is unknown.")
    else:
        status_label.config(text="Contact not found in the database.")

# Create a tkinter window
window = tk.Tk()
window.title("Contact Database")

# Create the name entry field with placeholder text
name_entry = tk.Entry(window)
name_entry.insert(0, "Enter the name")
name_entry.pack()

# Create the city entry field with placeholder text
city_entry = tk.Entry(window)
city_entry.insert(0, "Enter the city")
city_entry.pack()

# Create the save button
save_button = tk.Button(window, text="Save Contact", command=save_contact)
save_button.pack()

# Create the find button
find_button = tk.Button(window, text="Find Contact", command=find_contact)
find_button.pack()

# Create a label to display status messages
status_label = tk.Label(window, text="")
status_label.pack()

# Remove the placeholder text when the entry field is clicked
def remove_placeholder(event):
    if name_entry.get() == "Enter the name":
        name_entry.delete(0, tk.END)
    if city_entry.get() == "Enter the city":
        city_entry.delete(0, tk.END)

name_entry.bind("<Button-1>", remove_placeholder)
city_entry.bind("<Button-1>", remove_placeholder)

# Run the tkinter event loop
window.mainloop()

# Close the database connection
conn.close()
