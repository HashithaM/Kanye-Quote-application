# import requests

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# print(response)
# response.raise_for_status()

# data = response.json()

# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
# iss_position = (longitude, latitude)

# print(iss_position)

from tkinter import *
import requests


def get_quote():
    response = requests.get(url="https://api.kanye.rest")
    response.raise_for_status()
    data = response.json()
    quote = data["quote"]
    canvas.itemconfig(quote_text, text=quote)


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

window.mainloop()

# import requests
# from datetime import datetime

# MY_LAT = 6.927079
# MY_LONG = 79.861244

# parameters = {
#     "lat": MY_LAT,
#     "lng": MY_LONG,
#     "formatted": 0
# }

# response = requests.get(" https://api.sunrise-sunset.org/json", params=parameters)
# response.raise_for_status()
# data = response.json()
# sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
# sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
# print(sunrise)
# print(sunset)

# time_now = datetime.now()
# print(time_now.hour)
