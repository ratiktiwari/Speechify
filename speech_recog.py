import speech_recognition as sr
import webbrowser as wb

r1=sr.Recognizer()
r2=sr.Recognizer()
r3=sr.Recognizer()

with sr.Microphone() as source:
    print("Search Amazon")
    print("\nSpeak Now!")
    audio=r1.listen(source)

if "Amazon" in r1.recognize_google(audio):
    url="https://www.amazon.in/s?k="
    with sr.Microphone() as source:
        print("Search Your Query")
        audio=r2.listen(source)

        try:
            get=r2.recognize_google(audio)
            print(get)
            wb.get().open_new(url+get)

        except sr.UnknownValueError:
            print("Error!")

        except sr.RequestError as e:
            print("failed".format(e))

