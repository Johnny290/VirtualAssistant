import cv2
from deepface import DeepFace
import Sofia as S
import random

# Very simple emotion detection, and little "resposivity" for it

def getE(): 
    S.wish_me()
    cam = cv2.VideoCapture(0) 
    for i in range(3):
        ret, frame = cam.read()
        result = DeepFace.analyze(frame, enforce_detection=False, actions=["emotion"])   
    cam.release()

    if result["dominant_emotion"] == "sad":
        S.talk("Dont be so sad..let me tell you a joke.")
        S.talk(S.pyjokes.get_joke())
        S.talk("Is it better?")
        cmmd = S.take_command()

        if "no" in cmmd:
            S.talk("So let me just play some music")
            songS = random.choice(["lofi for better mood", "relaxing epic music", "whiskey blues"])
            S.pywhatkit.playonyt(songS)

        else:
            S.talk("So how can i help?")

    elif result["dominant_emotion"] == "angry":
        S.talk("Calm down a little, lets listen to some music")
        songA = random.choice(["lofi to relax", "relaxing epic music", "sad piano"])
        S.pywhatkit.playonyt(songA)

    elif result["dominant_emotion"] == "fear":
        S.talk("Don't be scared..")
        songF = random.choice(["bob marley dont worry be happy", "save me edguy", "Fear of the dark"])
        S.pywhatkit.playonyt(songF)
        

    elif result["dominant_emotion"] == "neutral":
        S.talk("how can i help")

   
    