# Speech-To-text
This project is a simple Speech-to-Text converter that captures speech input from the microphone and converts it to text using Python's SpeechRecognition library. The project also provides a simple web interface using Flask where users can click a button to start speech recognition and see the text results on the page.

## Table of Contents
  1. [ Technologies Used ](#Technologies-Used)
  2. [ Prerequisites ](#Prerequisites)
  3. [ Installation ](#Installation)
  4. [ Usage ](#Usage)
  5. [ API Endpoint ](#API-Endpoint)
  
## Technologies Used
- Python
- Flask (for creating the API)
- SpeechRecognition (for speech-to-text conversion)
- HTML, CSS, and JavaScript (for the frontend)

## Prerequisites
Before you begin, ensure you have met the following requirements:
- Python 3.7 or higher
- pip package manager

## Installation
  1. Clone the Repository:
  ```
  git clone https://github.com/your-username/speech-to-text.git
  cd speech-to-text

  ```
  2. Install the Python Dependencies:
  ```

  pip install -r requirements.txt

  ```
  3. Run the Flask Server:
  ```
  python app.py

  ```

## Usage
  ### Running the Project Locally
   1. Navigate to http://127.0.0.1:5000/ in your browser.
   2. You'll see a web page with a "Click to Speak" button.
   3. Click the button, and the microphone will start recording your voice.
   4. After a few seconds of recording, the spoken words will be converted to text and displayed on the page.

## API Endpoint
You can also use the API directly by sending a POST request to:
  ```
  POST /speech-to-text
  
  ```
  



  
