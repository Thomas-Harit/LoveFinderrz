import cv2
import os
import numpy as np
from PIL import Image
import pickle
from typing import List, Any

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

face_cascade = cv2.CascadeClassifier('./Utils/haarcascade_frontalface_alt2.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()

labels_ids = {}
last_id = 0

def AddFaces(face_list, label_list, image_array, current_id):
    '''
    
    PARTIE V (récupérer et ajouter les visages)
    
    '''
    pass

def get_file(folder_name):
    global labels_ids
    global last_id
    face_list = []
    label_list = []
    full_path = os.path.join(BASE_DIR, folder_name)
    for root, dirs, files in os.walk(full_path):
        for file in files:
            if file.endswith("png") or file.endswith("jpg"):
                path = os.path.join(root, file)
                label = os.path.basename(root).replace(" ", "-").lower()
                #print(label, path)
                if not label in labels_ids:
                    labels_ids[label] = last_id
                    last_id += 1
                current_id = labels_ids[label]
                unicolor_image = Image.open(path).convert("L")
                size = (500, 500)
                resized_unicolor_image = unicolor_image.resize(size, Image.ANTIALIAS)
                image_array = np.array(resized_unicolor_image, "uint8")
                AddFaces(face_list, label_list, image_array, current_id)
    return face_list, label_list

faces_images = []
images_labels = []


faces_images, images_labels = get_file("Images")

with open("Utils/pickles/face-labels.pickle", 'wb') as f:
    pickle.dump(labels_ids, f)

'''

PARTIE V (entraîner et sauvegarder l'IA)

'''