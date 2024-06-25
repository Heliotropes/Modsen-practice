from PIL import Image, ImageOps, ImageEnhance

class SelectedImage():
    def __init__(self):
        self.image_name = None
        self.image = None
        
    def set_image(self,image):
        self.image_name = image
        self.image = Image.open(self.image_name)

    def scaling(self,coefficient):
        self.image = ImageOps.scale(self.image, float(coefficient), resample=Image.LANCZOS)
        self.image.save(self.image_name)  

    def crop(self,border): 
        self.image = ImageOps.crop(self.image, int(border)) 
        self.image.save(self.image_name) 

    def mirror(self):
        self.image = ImageOps.mirror(self.image)
        self.image.save(self.image_name) 

    def flip(self):  
        self.image = ImageOps.flip(self.image)
        self.image.save(self.image_name)

    def rotate(self,angle,flag = Image.BICUBIC , expand = 1):
        self.image = self.image.rotate(int(angle),flag,expand)
        self.image.save(self.image_name)  

    def color(self,factor):
        self.image = ImageEnhance.Color(self.image).enhance(float(factor)) 
        self.image.save(self.image_name)

    def contrast(self,factor):
        self.image = ImageEnhance.Contrast(self.image).enhance(float(factor)) 
        self.image.save(self.image_name)

    def brightness(self,factor):
        self.image = ImageEnhance.Brightness(self.image).enhance(float(factor)) 
        self.image.save(self.image_name)
    
