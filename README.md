# Kanye Quote Desktop App

A small Tkinter application that retrieves a random quote from the public Kanye REST API and displays it in a styled desktop interface.

## Features

- One-click quote retrieval
- HTTP request and JSON parsing with `requests`
- Image-backed Tkinter interface
- Basic API error propagation with `raise_for_status()`

## Requirements

```bash
pip install requests
```

## Run

```bash
python main.py
```

Keep `background.png` and `kanye.png` beside `main.py`. An internet connection is required to load quotes.

## Privacy note

The file also contains commented geolocation examples. Replace precise coordinates with obvious sample values before publishing or adapting those examples.
