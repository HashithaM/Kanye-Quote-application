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

The commented geolocation example uses neutral `0.0` coordinates. Supply any real location through private runtime configuration rather than committing it.
