from deepface import DeepFace
from format_image import FormatImage

class Process:

    def  __init__(self, image_path) -> None: 
        self.image_path = FormatImage(image_path).format()

        
    def  process(self) -> str:

        if self.image_path == "": raise Exception("No image found")
        try:
            objs = DeepFace.analyze(img_path = self.image_path, actions = ['emotion'])
        except:
            raise Exception("DeepFace's error")
        
        #single detected face
        return objs[0]['dominant_emotion']
    
        

