# import packages
from deepface import DeepFace
import cv2
from gtts import gTTS
from playsound import playsound
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.logger import Logger
import logging
Logger.setLevel(logging.TRACE)

# specify window size

Window.size = (300, 500)


# kivy code

Builder.load_string('''
<CameraClick>:
    orientation: 'vertical'
    padding: "15sp"
    Camera:
        id: camera
        resolution: (800, 960)
        play: False
    ToggleButton:
        text: 'Play'
        background_normal: 'images/blue2.png'
        background_down: 'images/blue2.png'
        on_press: camera.play = not camera.play
        size_hint_y: None
        height: '48dp'
    Button:
        text: 'Capture'
        background_normal: 'images/orange-pink.png'
        background_down: 'images/orange-pink.png'
        size_hint_y: None
        height: '48dp'
        on_press: root.capture()   
''')

# Camera Class


class CameraClick(BoxLayout):
    def capture(self):
        camera = self.ids['camera']
        camera.export_to_png("files/IMG.png")
        print("Captured")


# TestCamera().run()


def MyFun():
    # Camera calling
    TestCamera().run()

    # saving the captured image
    img_path = 'files/IMG.png'
    img = cv2.imread(img_path)

    # Specify the image to be recognized
    img1_path = 'Dwayne Johnson.jpg'
    img2_path = img_path
    img1 = cv2.imread(img1_path)
    img2 = cv2.imread(img2_path)

    model_name = "Facenet"

    # Deepface face verification
    resp = DeepFace.verify(img1_path=img1_path, img2_path=img2_path, model_name=model_name)

    # converting the result into a list
    all_resp = list(resp.items())

    # Deepface facial attribute analysis
    result = DeepFace.analyze(img, actions=('emotion', 'age', 'gender', 'race'))

    # converting the result into a list
    all_pairs = list(result.items())

    # storing required values
    emotion = all_pairs[1][1]
    age = all_pairs[3][1]
    gender = all_pairs[4][1]
    race = all_pairs[6][1]

    var1 = all_resp[0][1]
    print(var1)

    # Code for voice output
    if var1==True:

        # If the person is known this code runs
        # Verifying face
        var = gTTS('the person is known', lang='en')
        var.save("files/MyName.mp3")
        playsound("files/MyName.mp3")

        # output for emotion
        tts_emotion1 = gTTS(emotion, lang='en')
        tts_emotion2 = gTTS('dominant emotion is', lang='en')
        tts_emotion2.save("files/hello1.mp3")
        tts_emotion1.save("files/hello.mp3")
        playsound("files/hello1.mp3")
        playsound("files/hello.mp3")
    else:

        # If the person is unknown, certain features are given
        # as output to give some idea about the person
        var = gTTS('the person is unknown', lang='en')
        var.save("files/MyName1.mp3")
        playsound("files/MyName1.mp3")

        # output for gender
        tts_gender1 = gTTS(gender, lang='en')
        tts_gender2 = gTTS('the person is', lang='en')
        tts_gender1.save("files/hello4.mp3")
        tts_gender2.save("files/hello5.mp3")
        playsound("files/hello5.mp3")
        playsound("files/hello4.mp3")

        # output for age
        AgeNum = str(age)
        tts_age1 = gTTS(AgeNum, lang='en')
        tts_age2 = gTTS('their age is', lang='en')
        tts_age1.save("files/hello2.mp3")
        tts_age2.save("files/hello3.mp3")
        playsound("files/hello3.mp3")
        playsound("files/hello2.mp3")

        # output for emotion
        tts_emotion1 = gTTS(emotion, lang='en')
        tts_emotion2 = gTTS('dominant emotion is', lang='en')
        tts_emotion2.save("files/hello1.mp3")
        tts_emotion1.save("files/hello.mp3")
        playsound("files/hello1.mp3")
        playsound("files/hello.mp3")

        # output for race
        tts_race1 = gTTS(race, lang='en')
        tts_race2 = gTTS('dominant race is', lang='en')
        tts_race1.save("files/hello6.mp3")
        tts_race2.save("files/hello7.mp3")
        playsound("files/hello7.mp3")
        playsound("files/hello6.mp3")

        # printing values
        print(all_pairs[1])
        print(all_pairs[3])
        print(all_pairs[4])
        print(all_pairs[6])


class TestCamera(App):
    def build(self):
        return CameraClick()


class MyDetection(Screen):
    Window.size = (300, 500)
    MyFun()


class TestEmotion(App):
    def build(self):
        return MyDetection()


# TestEmotion().run()
