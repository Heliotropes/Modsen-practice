import unittest
import os
from PIL import Image, ImageOps, ImageChops, ImageEnhance, UnidentifiedImageError
import sys
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)
from core.image import SelectedImage, valided_image


class TestSelectedImage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
        Set up the test environment, create a sample image for testing
        """
        cls.test_image_path = 'test_image.jpg'
        cls.test_image_path_invalid = 'invalid_image.jpg'
        # Create a sample image
        image = Image.new('RGB', (100, 100), color = 'red')
        image.save(cls.test_image_path)
        # Create an invalid image file
        with open(cls.test_image_path_invalid, 'w') as f:
            f.write('This is not a valid image file')

    @classmethod
    def tearDownClass(cls):
        """
        Clean up the test environment, remove the sample image after tests
        """
        if os.path.exists(cls.test_image_path):
            os.remove(cls.test_image_path)
        if os.path.exists(cls.test_image_path_invalid):
            os.remove(cls.test_image_path_invalid)

    def setUp(self):
        """
        Set up before each test
        """
        self.image_obj = SelectedImage()

    def test_valided_image_valid(self):
        result, message = valided_image(self.test_image_path)
        self.assertTrue(result)
        self.assertEqual(message, 'Валидация прошла успешно')

    def test_valided_image_not_found(self):
        result, message = valided_image('non_existent_image.jpg')
        self.assertFalse(result)
        self.assertEqual(message, 'Изображение не найдено')

    def test_valided_image_invalid(self):
        result, message = valided_image(self.test_image_path_invalid)
        self.assertFalse(result)
        self.assertEqual(message, 'Это не изображение')

    def test_set_image(self):
        self.image_obj.set_image(self.test_image_path)
        self.assertEqual(self.image_obj.image_name, self.test_image_path)
        self.assertIsInstance(self.image_obj.image, Image.Image)

    def test_scaling(self):
        self.image_obj.set_image(self.test_image_path)
        original_size = self.image_obj.image.size
        self.image_obj.scaling(0.5)
        self.assertEqual(self.image_obj.image.size, (original_size[0] // 2, original_size[1] // 2))

    def test_crop(self):
        self.image_obj.set_image(self.test_image_path)
        original_size = self.image_obj.image.size
        self.image_obj.crop(10)
        self.assertEqual(self.image_obj.image.size, (original_size[0] - 20, original_size[1] - 20))

    def test_mirror(self):
        self.image_obj.set_image(self.test_image_path)
        mirrored_image = ImageOps.mirror(self.image_obj.image)
        self.image_obj.mirror()
        self.assertTrue(ImageChops.difference(self.image_obj.image, mirrored_image).getbbox() is None)

    def test_flip(self):
        self.image_obj.set_image(self.test_image_path)
        flipped_image = ImageOps.flip(self.image_obj.image)
        self.image_obj.flip()
        self.assertTrue(ImageChops.difference(self.image_obj.image, flipped_image).getbbox() is None)

    def test_rotate(self):
        self.image_obj.set_image(self.test_image_path)
        rotated_image = self.image_obj.image.rotate(45, Image.BICUBIC, expand=1)
        self.image_obj.rotate(45)
        self.assertTrue(ImageChops.difference(self.image_obj.image, rotated_image).getbbox() is None)

    def test_color(self):
        self.image_obj.set_image(self.test_image_path)
        enhanced_image = ImageEnhance.Color(self.image_obj.image).enhance(2.0)
        self.image_obj.color(2.0)
        self.assertTrue(ImageChops.difference(self.image_obj.image, enhanced_image).getbbox() is None)

    def test_contrast(self):
        self.image_obj.set_image(self.test_image_path)
        enhanced_image = ImageEnhance.Contrast(self.image_obj.image).enhance(2.0)
        self.image_obj.contrast(2.0)
        self.assertTrue(ImageChops.difference(self.image_obj.image, enhanced_image).getbbox() is None)

    def test_brightness(self):
        self.image_obj.set_image(self.test_image_path)
        enhanced_image = ImageEnhance.Brightness(self.image_obj.image).enhance(2.0)
        self.image_obj.brightness(2.0)
        self.assertTrue(ImageChops.difference(self.image_obj.image, enhanced_image).getbbox() is None)

if __name__ == '__main__':
    unittest.main()
