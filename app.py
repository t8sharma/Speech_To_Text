from flask import Flask, jsonify, request, render_template
import speech_recognition as sr

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/speech-to-text', methods=['POST'])
def speech_to_text():
    recognizer = sr.Recognizer()
    
    # Use Microphone to capture the speech
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Listening...")
        audio = recognizer.listen(source)

        try:
            # Convert speech to text
            text = recognizer.recognize_google(audio)
            return jsonify({"success": True, "transcript": text})
        except sr.UnknownValueError:
            return jsonify({"success": False, "error": "Could not understand the audio"})
        except sr.RequestError as e:
            return jsonify({"success": False, "error": f"API request failed: {e}"})

if __name__ == '__main__':
    app.run(debug=True)
