# Kanye-Quote-application
This code gets Kanye West's quotes from the internet and displays
This code is a simple Python application using the Tkinter library for creating a graphical user interface (GUI). The purpose of the application is to display random Kanye West quotes when a button is clicked.

Here's a breakdown of what the code does:

Imports:

from tkinter import *: Imports the entire Tkinter module, allowing you to use its classes and functions without prefixing them with tkinter..
import requests: Imports the requests module, which is used to make HTTP requests to the Kanye Rest API to fetch quotes.
Function Definition:

get_quote(): This function is defined to fetch a random Kanye West quote from the Kanye Rest API. It sends an HTTP GET request to the API endpoint (https://api.kanye.rest) and retrieves the response. If the request is successful (status code 200), it extracts the quote from the JSON response and updates the text displayed on the canvas (quote_text) with the retrieved quote.
Tkinter Setup:

window: Creates a Tkinter window with the title "Kanye Says...".
window.config(): Sets padding for the window.
canvas: Creates a canvas widget for displaying images and text.
background_img: Loads an image file named "background.png" as the background of the canvas.
quote_text: Creates a text item on the canvas with initial text "Kanye Quote Goes HERE".
kanye_img: Loads an image file named "kanye.png" to be used as a button.
kanye_button: Creates a button with the Kanye image. When clicked, it will execute the get_quote() function.
Main Loop:

window.mainloop(): Starts the Tkinter event loop, which listens for events such as button clicks and redraws the GUI as necessary. This loop keeps the window open until the user closes it.
Overall, this code creates a simple GUI application that fetches random Kanye West quotes from an API and displays them on the screen when a button is clicked.
