from PyQt6.QtWidgets import QMessageBox

class ErrorWindow(QMessageBox):
    def __init__(self, message):
        """
        Initializes object of class ErrorWindow
            
        """
        super().__init__()
        self.setWindowTitle('Ошибка')
        self.setIcon(QMessageBox.Icon.Warning)
        self.setText(message)
        self.setStandardButtons(QMessageBox.StandardButton.Ok)