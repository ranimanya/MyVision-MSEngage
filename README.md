# MyVision-MS-Engage-Project 
* **Problem**: Develop a browser-based application or a native mobile application to demonstrate application of Face Recognition technology.
* **My idea**: In face-to-face social interactions, *blind and visually impaired persons* lack access to nonverbal cues like *facial expressions*, gestures and other general details such as *age*, *gender* and *race* which may lead to impaired interpersonal communication. 
* **Solution**: Here is the design and implementation of a face detection and recognition system for the visually impaired. 
Here, I attempted to build an application which gives *voice output to the user to facilitate interaction*
* **Technology used**: Python, Opencv, Deepface, gTTs(Google-Text-To-Speech), Kivy, Pycharm IDE
## How to run?
Go to requirements.txt for related dependencies.
Clone the project and open on your IDE, click and run **MyVision.py**
### If the saved image of the person is similar to captured image, the model gives output as true(this means the person is known). Since, the person is known to the user, we do not require to tell about their age, gender and race. But for better underatanding about the emotional state of the person, the model tells the dominant facial expression. 
<img width="960" alt="image" src="https://user-images.githubusercontent.com/81632252/170852115-3ee89dc3-5633-4a3b-8312-65475084bd5b.png">
<img width="960" alt="image" src="https://user-images.githubusercontent.com/81632252/170852190-c4237307-e185-4741-be91-5dfe317a500c.png">
<img width="616" alt="msengage22" src="https://user-images.githubusercontent.com/81632252/170880184-bfcf9d65-d77b-4550-b041-e0445c28b9aa.png">
<img width="531" alt="msengage223" src="https://user-images.githubusercontent.com/81632252/170880188-79a2556d-286c-478e-82b8-210dedaccf29.png">

### If the saved image is not same as captured image, the output is false(this means that the person is unknown). But for better underatanding about the person, the model tells about the age, gender, facial expression and race of the unknown person in the form of both voice output and terminal output.
<img width="613" alt="image" src="https://user-images.githubusercontent.com/81632252/170880489-cc128e19-2b0b-4bcb-96e0-2c86028f7a3b.png">
<img width="511" alt="image" src="https://user-images.githubusercontent.com/81632252/170880450-11ad98d4-df65-45fe-90f3-e1b912d8b0e4.png">



## References used
* https://pypi.org/project/deepface/
* https://kivy.org/doc/stable/examples/index.html

