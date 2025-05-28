import sys

from PySide6.QtWidgets import QMainWindow, QApplication
from ui_main_app_code import Ui_Form

class Program(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.stackedWidget.setCurrentIndex(2)












if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Program()
    window.show()
    sys.exit(app.exec())
