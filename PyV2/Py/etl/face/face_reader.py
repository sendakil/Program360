"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

    Author: Rajagopal Senthil Kumar
    Created Date:  07-Sep-2017
    Modified Date: 07-Sep-2017
    Purpose: Python Program to recognize human faces from picture (png)

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

import cv2
from internal import Internal


class HumanFaceDetector(Internal):
   
    no_of_objects=0
 
    def __init__(self,image_path="",cascade_path="",detect=0):
       HumanFaceDetector.no_of_objects+=1 
       self.image_path = image_path 
       self.cascade_path = cascade_path 
       if detect==1:
           self.detectAndShowFaces(detect)

    def setImagePath(self,image_path):
        self.image_path=image_path

    def setImagePath(self,cascade_path):
        self.cascade_path=cascade_path

    def detectFaces(self):
        face_cascade = cv2.CascadeClassifier(self.cascade_path)
        self.image = cv2.imread(self.image_path)
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.faces_detected = face_cascade.detectMultiScale( gray,
                        scaleFactor=1.1,
                        minNeighbors=5,
                        minSize=(30, 30),
                        flags = cv2.CASCADE_SCALE_IMAGE)

    def detectAndShowFaces(self,detect=0):
        if detect==1:
            self.detectFaces()

        print ("Found {0} faces!".format(len( self.faces_detected )))
        for (x, y, w, h) in self.faces_detected:
                cv2.rectangle(self.image, (x, y), (x+w, y+h), (0, 255, 0), 2)

        cv2.imshow("Faces found" ,self.image)
        cv2.waitKey(0)


#End of this Program#########################################################################################################



