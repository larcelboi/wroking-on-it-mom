import random
import sys

from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QMessageBox

from classes import Personne
from ui_main_app_code import Ui_Form
from classes.stockage import stocker_fichier


class Program(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.date = self.ui.dateEdit.date()
        self.client = None

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
        self.ui.log_in_bout_fini.clicked.connect(self.log_in_information)

        self.ui.sign_nom_enter.textChanged.connect(self.changement_nom)
        self.ui.sign_password_enter1.textChanged.connect(self.changement_password1)
        self.ui.signpassword2.textChanged.connect(self.changement_password2)



    def changement_nom(self):
        nom = self.ui.sign_nom_enter.text().capitalize().strip()

        if nom =="":
            self.ui.erreur_sign_nom.hide()

        for lettre in nom:
            if lettre.isnumeric():
                self.ui.erreur_sign_nom.hide()
            else:
                self.ui.erreur_sign_nom.setText(f"the name must contain one number")
                self.ui.erreur_sign_nom.show()

    def changement_password1(self):
        password1 = self.ui.sign_password_enter1.text().strip()
        symbol = False
        number = False
        capital = False
        if password1 =="":
            self.ui.erreur_sign_password1.hide()
        for lettre in password1:
            if lettre.isnumeric():
                number = True
            if not lettre.isalnum():
                symbol = True
            if lettre.isupper():
                capital = True
        if  symbol and number and capital:
            self.ui.erreur_sign_password1.hide()

        else:
            self.ui.erreur_sign_password1.setText(f"the password must contain 1.symbole,1.number and 1.capital letter ")
            self.ui.erreur_sign_password1.show()

    def changement_password2(self):

        password2 = self.ui.signpassword2.text().strip()
        password1 = self.ui.sign_password_enter1.text().strip()

        match = "this password must match the other one"
        symbol = False
        number = False
        capital = False
        if password2 =="":
            self.ui.erruer_sign_password2.hide()
        for lettre in password2:
            if lettre.isnumeric():
                number = True
            if not lettre.isalnum():
                symbol = True
            if lettre.isupper():
                capital = True
        if  symbol and number and capital and password2 == password1:
            self.ui.erruer_sign_password2.hide()
        else:
            if password2 != password1:
                self.ui.erruer_sign_password2.setText(
                    f"the password must contain 1.symbole,1.number and 1.capital letter\n{match}")
                self.ui.erruer_sign_password2.show()


    def welcome_page(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def sign_up(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def log_in(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def client_page(self):
        self.ui.bien_nomPutlisateur.setText(f"Bienvenue {self.client.nom_complet}")
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
        nom = self.ui.sign_nom_enter.text().capitalize()
        date_naissance = self.ui.dateEdit.date()
        password1 = self.ui.sign_password_enter1.text()
        password2 = self.ui.signpassword2.text()

        if self.ui.erruer_sign_password2.isVisible() or self.ui.erreur_sign_password1.isVisible() or self.ui.erreur_sign_nom.isVisible():
            QMessageBox.warning(self, "Erreur", f"they are still read text showing")
            return

        verification_personne = Personne(nom, date_naissance, password1, password2)
        format_erreur = ""
        if len(verification_personne.liste_erreur) >= 1:
            for chiffre,erreur in enumerate(verification_personne.liste_erreur):
                format_erreur += f"{erreur}\n"
            QMessageBox.warning(self,"Erreur",format_erreur)
            return
        else:
            while True:
                if verification_personne.id in stocker_fichier.id_user:
                    verification_personne.id = random.choice(range(10000))
                    continue
                else:
                    break
            self.client = verification_personne
            QMessageBox.information(self,"Valide",f"Création de {nom} finit")
            stocker_fichier.dict_uer[verification_personne.id] = verification_personne
            stocker_fichier.id_user.append(verification_personne.id)
            stocker_fichier.sauvegarder()
        self.client_page()

    def log_in_information(self):
        trouver = False
        nom = self.ui.log_in_nom_enter.text().capitalize()
        password = self.ui.log_in_password.text()
        for le_id,attribut in stocker_fichier.dict_uer.items():
            if nom == attribut.nom_complet and password == attribut.password1:
                self.client = stocker_fichier.dict_uer[le_id]
                QMessageBox.information(self,"Valide","Nom et mot de passe trouvés :)!")
                trouver = True
                break
        if not trouver:
            QMessageBox.warning(self, "Invalide", "Nom et mot de passe invalide :(!")
            return
        self.client_page()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Program()
    window.show()
    sys.exit(app.exec())
