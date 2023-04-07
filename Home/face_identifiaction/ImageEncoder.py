import face_recognition as fr

def img_enc(face):
    encoded={}
    
    faces = fr.load_image_file(face)
    face_enc = fr.face_encodings(faces)[0]
    encoded[face.split(".")[0]] = face_enc
    return list(encoded.keys()),list(encoded.values())


# face_known,face_enco_done= img_enc()
# with open("data.pickle","wb")as f:
#     pickle.dump((face_known,face_enco_done),f)
    

