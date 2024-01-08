# The python will convert the user's input in to the preferred output in realtime

from flask import Flask, render_template, request
import speech_recognition as sr
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

# Language options (10 most common languages)
languages = {
    'Spanish': 'es',
    'French': 'fr',
    'German': 'de',
    'Chinese': 'zh-cn',
    'Japanese': 'ja',
    'Korean': 'ko',
    'Arabic': 'ar',
    'Russian': 'ru',
    'Portuguese': 'pt',
    'Italian': 'it'
}

@app.route('/')
def index():
    return render_template('index.html', languages=languages)

@app.route('/translate', methods=['POST'])
def translate():
    if request.method == 'POST':
        selected_language = request.form.get('language')  # Get selected language from frontend
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio)
                print("You said:", text)
                translated = translator.translate(text, dest=selected_language).text
                print(f"Translated to {selected_language}: {translated}")
                return translated
            except Exception as e:
                print("Error:", str(e))
                return "Error"

if __name__ == '__main__':
    app.run(debug=True)
