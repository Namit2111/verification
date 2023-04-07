import face_checker as fc 
import face_extract as fe 
def result(id_img_path,selfie_img_path):
    extracted_facename = fe.extract(id_img_path)
    res = fc.check(extracted_facename,selfie_img_path)
    return res   # Will return True or false