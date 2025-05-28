import sys

from PySide6.QtWidgets import QMainWindow, QApplication, QWidget
from ui_main_app_code import Ui_Form

class Program(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.erreur_sign_nom.hide()
        self.ui.erruer_sign_password2.hide()
        self.ui.erreur_sign_password1.hide()

        self.ui.bout_sign_up.clicked.connect(self.sign_up)
        self.ui.bout_log_in.clicked.connect(self.log_in)

    def sign_up(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def log_in(self):
        self.ui.stackedWidget.setCurrentIndex(2)








if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Program()
    window.show()
    sys.exit(app.exec())
