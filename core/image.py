from PIL import Image, ImageOps, ImageEnhance, UnidentifiedImageError

class SelectedImage():
    def __init__(self):
        """
        Initializes object of class SelectedImage
            
        """
        self.image_name = None
        self.image = None
        
    def set_image(self,image):
        """
        Sets nessesary attributes to the class 

        Args:
            image (string): image path
            
        """
        self.image_name = image
        self.image = Image.open(self.image_name)

    def scaling(self,coefficient):
        """
        Resizes image with set scaling and saves 

        Args:
            coefficient (string): scale coefficient
            
        """
        self.image = ImageOps.scale(self.image, float(coefficient), resample=Image.LANCZOS)
        self.image.save(self.image_name)  

    def crop(self,border): 
        """
        Crops the image from the border and saves 

        Args:
            border (string): crop size
            
        """
        self.image = ImageOps.crop(self.image, int(border)) 
        self.image.save(self.image_name) 

    def mirror(self):
        """
        Reflects the image horizonally and saves 
            
        """
        self.image = ImageOps.mirror(self.image)
        self.image.save(self.image_name) 

    def flip(self):
        """
        Reflects the image vertically and saves 
            
        """  
        self.image = ImageOps.flip(self.image)
        self.image.save(self.image_name)

    def rotate(self,angle,flag = Image.BICUBIC , expand = 1):
        """
        Rotates image for set angle and saves 

        Args:
            angle (string): the angle by which the image is rotated
            flag :resampling filter
            expand (bool): expansion flag
            
        """
        self.image = self.image.rotate(int(angle),flag,expand)
        self.image.save(self.image_name)  

    def color(self,factor):
        """
        Changes saturation to the image and saves 

        Args:
            factor (string): saturation change scale
            
        """
        self.image = ImageEnhance.Color(self.image).enhance(float(factor)) 
        self.image.save(self.image_name)

    def contrast(self,factor):
        """
        Changes contrast to the image and saves 

        Args:
            factor (string): contrast change scale
            
        """
        self.image = ImageEnhance.Contrast(self.image).enhance(float(factor)) 
        self.image.save(self.image_name)

    def brightness(self,factor):
        """
        Changes brightness to the image and saves 

        Args:
            factor (string): brightness change scale
            
        """
        self.image = ImageEnhance.Brightness(self.image).enhance(float(factor)) 
        self.image.save(self.image_name)
    
def valided_image(image_path):
    """
    Validates selected image

    Args:
        image_path (string): image path
        
    Returns:
        bool, string: result, does image pass validation and message with validation details
            
    """
    try:
        Image.open(image_path)
        return True, 'Валидация прошла успешно'
    except FileNotFoundError:
        return False, 'Изображение не найдено'
    except UnidentifiedImageError:
        return False, 'Это не изображение'
    except Exception as ex:
        return False, f'Неизвестная ошибка: {ex}'