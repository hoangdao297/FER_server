import pillow_avif
from PIL import Image
from pillow_heif import register_heif_opener
from os.path import exists
import random

class FormatImage:

    def __init__(self, img_path) -> None:
        register_heif_opener()
        self.img = False
        self.img_path = self.check_exist(img_path)
        # self.img_path = img_path
        if self.img_path != "":
            self.img  = Image.open(img_path)

    def check_exist(self, img_path) ->str:
        path=""
        if exists(img_path):
            path = img_path
        return path
    
    def check_format(self) -> bool:
        """Verify if the image has the right format."""
        if not self.img: return self.img
        return self.img.format.lower() in ["jpg", "jpeg", "png"]
    
    def format(self) -> str:
        """Returns the path of correctly formatted image file."""

        out_path = self.img_path
        if  not self.check_format():
            out_path = "../images/output"+str(random.randint(0, 100))+".jpg"
            self.img.convert('RGB').save(out_path, "JPEG")
        return out_path
