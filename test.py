'''import requests
import json

apiKey = "a94b5ab426afd7bceddf051bde36cd48"

city = 'adama'

baseUrl = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={apiKey}&units=metric"
response = requests.get(baseUrl)

print(response)
weather = response.json()
file = open("json.json" ,'w')
json.dump(weather,file,indent=4)

print(weather['list'])'''

import tkinter as tk

def check_entry_value():
    value = entry.get()
    if value == "secret":
        print("Access Granted!")
        result_label.config(text="Access Granted!")
    elif value == "exit":
        window.quit()
    else:
        print(f"Incorrect input: {value}")
        result_label.config(text=f"Incorrect input: {value}")

# Create the Tkinter window
window = tk.Tk()
window.title("Conditional Entry Example")

# Create an Entry widget
entry = tk.Entry(window)
entry.pack(pady=10)

# Create a Button to trigger the check
button = tk.Button(window, text="Submit", command=check_entry_value)
button.pack(pady=5)

# Create a Label to display results (optional)
result_label = tk.Label(window, text="")
result_label.pack(pady=5)

# Start the Tkinter event loop
window.mainloop()