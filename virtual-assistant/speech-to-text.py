#import section
import speech_recognition as sr
from gtts import gTTS
import os
from datetime import datetime
import playsound
import pyjokes
import wikipedia
import pyaudio
import webbrowser


#get mic audio
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        # wait for a second to let the recognizer adjust the
        # energy threshold based on the surrounding noise level
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio)
            print(said)
        except sr.UnknownValueError:
            speak("Sorry, I did not get that.")
        except sr.RequestError:
            speak("Sorry, the service is not available")
    return said.lower()

#speak converted audio to text
def speak(text):
    tts = gTTS(text=text, lang='en')
    filename = "voice.mp3"
    try:
        os.remove(filename)
    except OSError:
        pass
    tts.save(filename)
    playsound.playsound(filename)

#function to respond to commands
def respond(text):
    print("Text from get audio " + text)
    if 'youtube' in text:
        speak("What do you want to search for?")
        keyword = get_audio()
        if keyword!= '':
            url = f"https://www.youtube.com/results?search_query={keyword}"
            webbrowser.get().open(url)
            speak(f"Here is what I have found for {keyword} on youtube")
    elif 'search' in text:
        speak("What do you want to search for?")
        query = get_audio()
        if query !='':
            result = wikipedia.summary(query, sentences=3)
            speak("According to wikipedia")
            print(result)
            speak(result)
    elif 'joke' in text:
        speak(pyjokes.get_joke())
    elif 'what time' in text:
        strTime = datetime.today().strftime("%H:%M %p")
        print(strTime)
        speak(strTime)
    elif 'weather' in text:
        speak("What city do you want to search for?")
        keyword = get_audio()
        if keyword != '':
            url = f"https://www.google.com/search?q=weather {keyword}"
            webbrowser.get().open(url)
            speak(f"Here is what I have found for {keyword} on google")
    elif 'google' in text:
        speak("What do you want to search for on Google?")
        keyword = get_audio()
        if keyword != '':
            url = f"https://www.google.com/search?q={keyword}"
            webbrowser.get().open(url)
            speak(f"Here is what I have found for {keyword} on google")
    elif 'exit' in text:
        speak("Goodbye, till next time")
        exit()


while True:
    print("I am listening...")
    text = get_audio()
    respond(text)

