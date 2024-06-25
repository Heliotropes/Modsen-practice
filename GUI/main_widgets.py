from PyQt6.QtWidgets import  QLabel,QLineEdit, QWidget, QHBoxLayout, QToolButton, QFileDialog, QCheckBox, QSlider, QSpinBox, QPushButton
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt, QSize


def create_label(text):
    label = QLabel()
    label.setAlignment(Qt.AlignmentFlag.AlignLeft)
    label.setText(text)
    return label

def create_line(MaxLength, PlaceholderText):
    label = QLineEdit()
    label.setMaxLength(MaxLength)
    label.setPlaceholderText(PlaceholderText)
    return label

def create_button(text, icon_path, icon_size=QSize(20, 20)):
    button = QPushButton()
    button.setFixedSize(QSize(40, 20))
    button.setIconSize(icon_size)
    button.setIcon(QIcon(icon_path))
    button.setText(text)
    return button

def create_spin_box(min_board, max_board, setting_key, step):
    spin_box = QSpinBox()
    spin_box.setRange(min_board, max_board)
    spin_box.setValue(setting_key)
    spin_box.setSingleStep(step)
    return spin_box

def creat_toolbar_buttons(layout, icon_path, tooltip_text, on_click=None):
    icon_size = QSize(500, 500)

    icon_button = QToolButton()
    icon_button.setIcon(QIcon(icon_path))
    icon_button.setIconSize(icon_size)
    icon_button.setFixedHeight(20)
    icon_button.setFixedWidth(20)
    icon_button.setToolTip(tooltip_text)
    if on_click:
        icon_button.clicked.connect(on_click)

    layout.addWidget(icon_button)
