## Sample code to translate the speach from one language to another

from googletrans import Translator
import speech_recognition as spr
from gtts import gTTS
import os

def takeInput():
 languages = {"English": 'en', "French": 'fr',
                 "Spanish": 'es', "German": 'de', "Italian": 'it'}

 print("Select a target language")
 print("Language", "   ", "Code")
 
 for x in languages:
    print(x, "   ", languages[x])
 print("=================================")

 target = input();
 if (target in languages):
    target1 = languages[target]

 else:
    print("Input target language is not in the supported list of Languages shown above")
    exit()

 recogniser =spr.Recognizer()
 mic = spr.Microphone()

 print("Speak something to translate.....")
 with mic as src:
    phrase = recognise_speech(recogniser, src)

 return target1,phrase

def recognise_speech(recogniser, src):
   try:
      recogniser.adjust_for_ambient_noise(src)  # Adjust for background noise
      audio = recogniser.listen(src)  # Capture audio input
      recognized_text = recogniser.recognize_google(audio)  # Recognize using Google's recognizer
      return recognized_text
   except spr.UnknownValueError:
      print("Google Speech Recognition could not understand the audio.")
      return None
   except spr.RequestError as e:
      print(f"Could not request results from Google Speech Recognition service; {e}")
      return None

def googleTranslate(DestLanguage, phrase):
  
    try:
       translator = Translator()
       result = translator.translate(phrase, dest=DestLanguage)
       print(f"Translating the following text:\n{result.origin}\nDetected language code is {result.src}")
       print(f"Here's the result:\n{result.text}\nTarget language code is {result.dest}")

       # Convert translated text to speech
       speak = gTTS(text=result.text, lang=DestLanguage, slow=False)

       # Save the translated speech to a file
       speak.save("recorded_voice.mp3")

       # Play the speech
       os.system("start recorded_voice.mp3")
    except Exception as e:
       print(f"An error occurred: {e}") 
    
trg, phrase = takeInput()

googleTranslate(trg, phrase)



