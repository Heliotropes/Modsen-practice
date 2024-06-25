from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QFileDialog, QLabel
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import Qt
from GUI.main_widgets import  create_button, creat_toolbar_buttons, create_label, create_spin_box, create_line
from core.image import SelectedImage


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.image_paths = []
        self.selected_image = SelectedImage()
        self.labelImage = QLabel()
        self.setWindowTitle('Image Augmentator')
        self.setWindowIcon(QIcon('icons/iconApp.png'))
        self.setFixedSize(360, 480)
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)
        self.layout = QVBoxLayout()
        self.viewer_window = None

        toolbar = QWidget(self)
        toolbar.setFixedHeight(40)
        toolbar_layout = QHBoxLayout(toolbar)
        toolbar_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)

        toolbar_layout.setSpacing(5)
        
        creat_toolbar_buttons(toolbar_layout, 'icons/iconFolder.png', 'Загрузить изображение',self.select_image)
        creat_toolbar_buttons(toolbar_layout, 'icons/iconSettings.png', 'Настройки')
        creat_toolbar_buttons(toolbar_layout, 'icons/iconSave.png', 'Сохранить изображение')

        toolbar.setLayout(toolbar_layout)
        self.layout.addWidget(toolbar)
        
        
        scaling_layout = QHBoxLayout()

        self.scaling_label = create_label("Масштабирование")
        scaling_layout.addWidget(self.scaling_label)
        
        self.scaling_line = create_line(10,'1.0')
        scaling_layout.addWidget(self.scaling_line)
        
        self.scaling_button = create_button("","icons/iconEnter.png")
        self.scaling_button.clicked.connect(lambda: self.selected_image.scaling((self.scaling_line.text())))
        self.scaling_button.clicked.connect(self.openImage)
        scaling_layout.addWidget(self.scaling_button)
        
        self.layout.addLayout(scaling_layout)
        
        
        crop_layout = QHBoxLayout()
        
        self.crop_label = create_label("Обрезка")
        crop_layout.addWidget(self.crop_label)
        
        self.crop_line = create_line(10,'30')
        crop_layout.addWidget(self.crop_line)
        
        self.crop_button = create_button("","icons/iconEnter.png")
        self.crop_button.clicked.connect(lambda: self.selected_image.crop((self.crop_line.text())))
        self.crop_button.clicked.connect(self.openImage)
        crop_layout.addWidget(self.crop_button)
        
        self.layout.addLayout(crop_layout)
        
        
        mirror_layout = QHBoxLayout()
        
        self.mirror_label = create_label("Отражение")
        mirror_layout.addWidget(self.mirror_label)
        
        self.mirror_button = create_button("","icons/iconMirror.png")
        self.mirror_button.clicked.connect(self.selected_image.mirror)
        self.mirror_button.clicked.connect(self.openImage)
        mirror_layout.addWidget(self.mirror_button)
        self.flip_button = create_button("","icons/iconFlip.png")
        self.flip_button.clicked.connect(self.selected_image.flip)
        self.flip_button.clicked.connect(self.openImage)
        mirror_layout.addWidget(self.flip_button)
        
        self.layout.addLayout(mirror_layout)
        
        
        rotate_layout = QHBoxLayout()
        
        self.rotate_label1 = create_label("Поворот на")
        rotate_layout.addWidget(self.rotate_label1)
        
        self.rotate_line = create_line(10,'90')
        rotate_layout.addWidget(self.rotate_line)
        
        self.rotate_label2 = create_label("градусов")
        rotate_layout.addWidget(self.rotate_label2)
        
        self.rotate_button = create_button("","icons/iconRotate.png")
        self.rotate_button.clicked.connect(lambda: self.selected_image.rotate((self.rotate_line.text())))
        self.rotate_button.clicked.connect(self.openImage)
        rotate_layout.addWidget(self.rotate_button)
        
        self.layout.addLayout(rotate_layout)
        
        
        color_layout = QHBoxLayout()
        
        self.color_label = create_label("Насыщенность")
        color_layout.addWidget(self.color_label)
        
        self.color_line = create_line(10,'1.0')
        color_layout.addWidget(self.color_line)
        
        self.color_button = create_button("","icons/iconColor.png")
        self.color_button.clicked.connect(lambda: self.selected_image.color((self.color_line.text())))
        self.color_button.clicked.connect(self.openImage)
        color_layout.addWidget(self.color_button)
        
        self.layout.addLayout(color_layout)
        
        
        contrast_layout = QHBoxLayout()
        
        self.contrast_label = create_label("Контраст")
        contrast_layout.addWidget(self.contrast_label)
        
        self.contrast_line = create_line(10,'1.0')
        contrast_layout.addWidget(self.contrast_line)
        
        self.contrast_button = create_button("","icons/iconContrast.png")
        self.contrast_button.clicked.connect(lambda: self.selected_image.contrast((self.contrast_line.text())))
        self.contrast_button.clicked.connect(self.openImage)
        contrast_layout.addWidget(self.contrast_button)
        
        self.layout.addLayout(contrast_layout)
        
        
        brightness_layout = QHBoxLayout()
        
        self.brightness_label = create_label("Яркость")
        brightness_layout.addWidget(self.brightness_label)
        
        self.brightness_line = create_line(10,'1.0')
        brightness_layout.addWidget(self.brightness_line)
        
        self.brightness_button = create_button("","icons/iconBrightness.png")
        self.brightness_button.clicked.connect(lambda: self.selected_image.brightness((self.brightness_line.text())))
        self.brightness_button.clicked.connect(self.openImage)
        brightness_layout.addWidget(self.brightness_button)
        
        self.layout.addLayout(brightness_layout)
        
        final_layout = QHBoxLayout()
        self.final_button = create_button("","icons/iconAll.png")
        self.final_button.clicked.connect(lambda: self.selected_image.scaling((self.scaling_line.text())))
        self.final_button.clicked.connect(lambda: self.selected_image.crop((self.crop_line.text())))
        self.final_button.clicked.connect(self.selected_image.mirror)
        self.final_button.clicked.connect(self.selected_image.flip)
        self.final_button.clicked.connect(lambda: self.selected_image.rotate((self.rotate_line.text())))
        self.final_button.clicked.connect(lambda: self.selected_image.color((self.color_line.text())))
        self.final_button.clicked.connect(lambda: self.selected_image.contrast((self.contrast_line.text())))
        self.final_button.clicked.connect(lambda: self.selected_image.brightness((self.brightness_line.text())))
        self.final_button.clicked.connect(self.openImage)
        final_layout.addWidget(self.final_button)
        
        self.layout.addLayout(final_layout)
        
        content_strip = QWidget()
        self.layout.addWidget(content_strip)

        self.main_widget.setLayout(self.layout)

    def select_image(self):
        image = QFileDialog.getOpenFileName(self,"Select Reference Image", "","Image Files (*.png *.jpg *.gif *.bmp)")
        if image:
            self.image_paths.append(image[0])
            self.selected_image.set_image(image[0])
            print(self.image_paths)
            self.openImage()
     
    def openImage(self):
        pixmapImage = QPixmap(self.selected_image.image_name)
        (width, height) = self.selected_image.image.size
        pixmapImage = pixmapImage.scaled(
            width, height,
            Qt.AspectRatioMode.KeepAspectRatioByExpanding,
            Qt.TransformationMode.SmoothTransformation
        )
        self.labelImage.setPixmap(pixmapImage)
        self.labelImage.setMaximumSize(width,height)
        self.labelImage.resize(width,height)
        self.labelImage.show()
        self.labelImage.activateWindow()

