from deepface import DeepFace
from format_image import FormatImage
import os

class Process:

    def  __init__(self, image_path) -> None: 
        self.image_path = FormatImage(image_path).format()
        self.img_org = image_path


    def  process(self) -> str:

        if self.image_path == "": raise Exception("No image found")
        try:
            objs = DeepFace.analyze(img_path = self.image_path, actions = ['emotion'])
            if os.path.exists(self.image_path):
                os.remove(self.image_path)
            if os.path.exists(self.img_org) and self.img_org != self.image_path:
                os.remove(self.img_org)
        except:
            raise Exception("DeepFace's error")
        
        #single detected face
        return objs[0]['dominant_emotion']
    
        

