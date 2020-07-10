import face_recognition
from PIL import Image, ImageDraw

import xlwt 
from xlwt import Workbook 

import cv2
import numpy as np 
import os

import datetime

class_images_encod=[]
dataset_path='./class/'
known_face_names = []
atttendence = []

class_id = 0 
names = {}
# load and learn images from a folder
for fx in os.listdir(dataset_path):
	if fx.endswith('.jpg'):
		names[class_id] = fx[:-4]
		print("Loaded "+fx)
		class_images = face_recognition.load_image_file(dataset_path+fx)
		t = face_recognition.face_encodings(class_images)[0]
		class_images_encod.append(t)

		# #create labels for the class
		# target = class_id*np.ones((data_item.shape[0],))
		class_id+=1
		known_face_names.append(fx[:-4])

unknown_image = face_recognition.load_image_file("Z53A0529.jpeg")
# Find all the faces and face encodings in the unknown image
face_locations = face_recognition.face_locations(unknown_image)
face_encodings = face_recognition.face_encodings(unknown_image, face_locations)

# Convert the image to a PIL-format image so that we can draw on top of it with the Pillow library
# See http://pillow.readthedocs.io/ for more about PIL/Pillow
pil_image = Image.fromarray(unknown_image)
# Create a Pillow ImageDraw Draw instance to draw with
draw = ImageDraw.Draw(pil_image)

# Loop through each face found in the unknown image
for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
    # See if the face is a match for the known face(s)
    matches = face_recognition.compare_faces(class_images_encod, face_encoding)

    name = "Unknown"

    # If a match was found in known_face_encodings, just use the first one.
    if True in matches:
        first_match_index = matches.index(True)
        name = known_face_names[first_match_index]
        # file = open('name.txt','w') 
        # file.write(name) 
        # file.close()
        atttendence.append(name)
        wb = Workbook() 
        sheet1 = wb.add_sheet('Sheet 1') 
        time = datetime.datetime.now()
        for i in range(len(atttendence)):
            sheet1.write(i, 0, atttendence[i])
            sheet1.write(i,1, str(time))
            sheet1.write(i,2,'Present')


        wb.save('attendace.xls') 


    # Draw a box around the face using the Pillow module
    draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 255))

    # Draw a label with a name below the face
    text_width, text_height = draw.textsize(name)
    draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0, 0, 255), outline=(0, 0, 255))
    draw.text((left + 6, bottom - text_height - 5), name, fill=(255, 255, 255, 255))


# Remove the drawing library from memory as per the Pillow docs
del draw

# Display the resulting image
# pil_image = pil_image.resize((2000,1000),resample = 0)
pil_image.show()
