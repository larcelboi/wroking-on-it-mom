import sys

from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QMessageBox

from classes import Personne
from ui_main_app_code import Ui_Form



class Program(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.date = self.ui.dateEdit.date()

        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.erreur_sign_nom.hide()
        self.ui.erruer_sign_password2.hide()
        self.ui.erreur_sign_password1.hide()
        self.ui.g_back_log_in.setText("Go Back")
        self.ui.go_back_sign_up.setText("Go Back")


        self.ui.bout_sign_up.clicked.connect(self.sign_up)
        self.ui.bout_log_in.clicked.connect(self.log_in)
        self.ui.go_back_sign_up.clicked.connect(self.enelver_information)
        self.ui.g_back_log_in.clicked.connect(self.enelver_information)
        self.ui.sign_up_fini_boutton.clicked.connect(self.sign_up_information)

    def welcome_page(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def sign_up(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def log_in(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def client_page(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def enelver_information(self):
        self.ui.sign_nom_enter.clear()
        self.ui.sign_password_enter1.clear()
        self.ui.signpassword2.clear()
        self.ui.dateEdit.setDate(self.date)

        self.ui.log_in_nom_enter.clear()
        self.ui.log_in_password.clear()
        self.ui.stackedWidget.setCurrentIndex(0)

    def sign_up_information(self):
        nom = self.ui.sign_nom_enter.text()
        date_naissance = self.ui.dateEdit.date()
        password1 = self.ui.sign_password_enter1.text()
        password2 = self.ui.signpassword2.text()


        verification_personne = Personne(nom, date_naissance, password1, password2)
        format_erreur = ""
        if len(verification_personne.liste_erreur) >= 1:
            for erreur in verification_personne.liste_erreur:
                format_erreur += f"{erreur}\n"
            QMessageBox.warning(self,"Erreur",format_erreur)
            return
        else:
            pass













if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Program()
    window.show()
    sys.exit(app.exec())
