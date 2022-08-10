from unicodedata import category
import numpy as np
import cv2
import pickle

face_cascade = cv2.CascadeClassifier('./Utils/haarcascade_frontalface_alt2.xml')

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("./Utils/recognizers/face-trainner.yml")

labels = {"person_name": 1}
with open("Utils/pickles/face-labels.pickle", 'rb') as f:
	og_labels = pickle.load(f)
	labels = {v:k for k,v in og_labels.items()}

loop = True

'''

PARTIE III (se connecter à la caméra)

'''

def PrintFrames(faces, frame):
    '''
    
    PARTIE IV (afficher les rectangles)
    
    '''
    pass


def PrintNames(faces, gray, frame):
    '''
    
    PARTIE VI (entière)
    
    '''
    pass

while(loop == True):
    '''
    
    PARTIE III (lire l'image de la caméra)

    '''

    '''
    
    PARTIE IV (récupérer la liste des visages)
    
    '''

    # Enlevez ces commentaires après complétion de 'PARTIE IV (récupérer la liste des visages)'
    # PrintFrames(faces, frame)
    # PrintNames(faces, gray)

    '''

    PARTIE III (afficher l'image sur votre écran)

    '''
    if cv2.waitKey(20) == ord('q'):
        loop = False