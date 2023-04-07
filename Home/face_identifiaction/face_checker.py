import face_recognition as fr
import cv2
import numpy as np
import ImageEncoder as ie

#load encoded images 
# with open("Resource\\data.pickle",'rb')as f:
#     face_known,face_enco_done = pickle.load(f)


def check(face,test_face):
    face_known,face_enco_done=ie.img_enc(face)        
    face_loca = []
    face_enco = []
    face_name =[]

    #to read  video and capture attendance

    img = cv2.imread(test_face)
    #small_frame = cv2.resize(frame,(0,0),fx = 0.25,fy = 0.25)
    rgb_frame = img#small_frame#[:,:,::-1]
    if True:
        face_loca = fr.face_locations(rgb_frame)
        face_enco = fr.face_encodings(rgb_frame,face_loca)
        face_name = []
        for face_enc in face_enco:
            matches = fr.compare_faces(face_enco_done,face_enc)
            name = "Unknown_Unknown"
            face_distance = fr.face_distance(face_enco_done,face_enc)
            best_match = np.argmin(face_distance)
            
            if matches[best_match]:
                return True
            else:
                return False
     
# to add a box on the detected face        
##        for (top, right, bottom, left), name in zip(face_loca, face_name):
##            # Draw a box around the face
##            cv2.rectangle(frame, (left-20, top-20), (right+20, bottom+20), (255, 0, 0), 2)
##
##            # Draw a label with a name below the face
##            cv2.rectangle(frame, (left-20, bottom -15), (right+20, bottom+20), (255, 0, 0), cv2.FILLED)
##            font = cv2.FONT_HERSHEY_DUPLEX
##            cv2.putText(frame, name, (left -20, bottom + 15), font, 1.0, (255, 255, 255), 2)
    

                
