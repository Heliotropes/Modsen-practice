from PyQt6.QtWidgets import  QLabel,QLineEdit, QToolButton, QSpinBox, QPushButton
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt, QSize


def create_label(text):
    """
    Creates a label with set text

    Args:
        text (string): text message 
    
    Returns:
        QLabel: finished label widget
            
    """
    label = QLabel()
    label.setAlignment(Qt.AlignmentFlag.AlignLeft)
    label.setText(text)
    return label

def create_line(MaxLength, PlaceholderText):
    """
    Creates a one-line text editor with set max length and holder text

    Args:
        MaxLength (int): maximum number of characters per line
        PlaceholderText(string): holder text 
    
    Returns:
        QLabel: finished line-edit widget
            
    """
    label = QLineEdit()
    label.setMaxLength(MaxLength)
    label.setPlaceholderText(PlaceholderText)
    return label

def create_button(text, icon_path, icon_size=QSize(20, 20)):
    """
    Creates a button with set text and icon

    Args:
        text (string): text message
        icon_path(string): button icon path 
    
    Returns:
        QLabel: finished button widget
            
    """
    button = QPushButton()
    button.setFixedSize(QSize(40, 20))
    button.setIconSize(icon_size)
    button.setIcon(QIcon(icon_path))
    button.setText(text)
    return button


def create_toolbar_buttons(layout, icon_path, tooltip_text, on_click=None):
    """
    Creates a button with set text, icon and related function and places it in selected layout

    Args:
        layout (string): selected layout, where the button will be placed
        icon_path(string): button icon path 
        tooltip_text(string): text tip for the button
        on_click (function): a function that will start executing after the button is pressed
            
    """
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
