# MouseClickServer-PyAutoGUI

This repository contains a simple Python-based web server that listens for HTTP POST requests and simulates a mouse click on the host computer using the PyAutoGUI library.

## Usage

1. Clone the repository to your local machine:

    git clone https://github.com/your-username/MouseClickServer-PyAutoGUI.git
    cd MouseClickServer-PyAutoGUI


2. Install the required libraries if you haven't already:

    pip install flask pyautogui


3. Run the server:

    python mouse_click_server.py


Upon the first run, the server will generate an API key and display it in the command-line interface. The API key will be saved to `key.txt`. Subsequent runs will load the API key from the file.

## Making a Mouse Click Request

To trigger a mouse click, send an HTTP POST request to the `/click` endpoint with the API key in the `Authorization` header. The server will respond with a success message if the mouse click is successful.

Example using curl:

    curl -X POST -H "Authorization: YOUR_API_KEY" http://localhost:5000/click
