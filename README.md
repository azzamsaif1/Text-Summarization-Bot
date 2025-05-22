
# Text Summarization Bot (HTTP via Python Socket)

A lightweight HTTP server built with raw Python socket that receives a text input from a web form and returns a summarized version of that text.

---

## Features

- Accepts HTTP POST requests via browser
- Parses text= from the request body
- Automatically decodes URL-encoded characters (e.g., %20, +)
- Performs simple text summarization:
  - Returns first sentence if available
  - Otherwise, returns the first 50 characters followed by ...
- Displays both original and summarized text in the browser

---

## How It Works

1. The user enters/pastes a long text in the form.
2. The browser sends it as:

POST / HTTP/1.1 Content-Type: application/x-www-form-urlencoded

text=This+is+a+long+text+to+summarize...

3. The server:
- Parses the body
- Applies unquote_plus to decode
- Extracts text and summarizes it
4. The summarized text is sent back inside a dynamically generated HTML page.

---

## Technologies Used

- Python 3
- socket module
- urllib.parse (for decoding)

---

## Usage

bash
python text_summarization_bot.py

Then open your browser and visit:
http://127.0.0.1:9090

