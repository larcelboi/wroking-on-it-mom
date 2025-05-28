# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_app_code.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDateEdit, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(523, 421)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.stackedWidget = QStackedWidget(Form)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.welcome_page = QWidget()
        self.welcome_page.setObjectName(u"welcome_page")
        self.verticalLayout_2 = QVBoxLayout(self.welcome_page)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.welcome_texte = QLabel(self.welcome_page)
        self.welcome_texte.setObjectName(u"welcome_texte")
        font = QFont()
        font.setPointSize(20)
        self.welcome_texte.setFont(font)
        self.welcome_texte.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.welcome_texte)


        self.verticalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(100, -1, 100, -1)
        self.pushButton = QPushButton(self.welcome_page)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"QPushButton{color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 0, 0);\n"
"border:2  solid white;\n"
"        border-radius: 6px;\n"
"paddding: 10px\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(255, 0, 0);\n"
"	background-color: rgb(255, 255, 255);\n"
"border: 2px solid white;\n"
"        border-radius: 5px;}\n"
"")

        self.verticalLayout_4.addWidget(self.pushButton)


        self.verticalLayout_2.addLayout(self.verticalLayout_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(100, -1, 100, -1)
        self.bout_sign_up = QPushButton(self.welcome_page)
        self.bout_sign_up.setObjectName(u"bout_sign_up")

        self.horizontalLayout_2.addWidget(self.bout_sign_up)

        self.bout_log_in = QPushButton(self.welcome_page)
        self.bout_log_in.setObjectName(u"bout_log_in")

        self.horizontalLayout_2.addWidget(self.bout_log_in)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.verticalSpacer = QSpacerItem(20, 150, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.stackedWidget.addWidget(self.welcome_page)
        self.sign_up_page = QWidget()
        self.sign_up_page.setObjectName(u"sign_up_page")
        self.gridLayout = QGridLayout(self.sign_up_page)
        self.gridLayout.setObjectName(u"gridLayout")
        self.sign_password_enter1 = QLineEdit(self.sign_up_page)
        self.sign_password_enter1.setObjectName(u"sign_password_enter1")

        self.gridLayout.addWidget(self.sign_password_enter1, 10, 1, 1, 1)

        self.sign_date_naissance = QLabel(self.sign_up_page)
        self.sign_date_naissance.setObjectName(u"sign_date_naissance")

        self.gridLayout.addWidget(self.sign_date_naissance, 7, 0, 1, 1)

        self.signpassword2 = QLineEdit(self.sign_up_page)
        self.signpassword2.setObjectName(u"signpassword2")

        self.gridLayout.addWidget(self.signpassword2, 13, 1, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(150, -1, 150, -1)
        self.sign_up_fini_boutton = QPushButton(self.sign_up_page)
        self.sign_up_fini_boutton.setObjectName(u"sign_up_fini_boutton")

        self.horizontalLayout_6.addWidget(self.sign_up_fini_boutton)


        self.gridLayout.addLayout(self.horizontalLayout_6, 17, 0, 1, 2)

        self.go_back_sign_up = QPushButton(self.sign_up_page)
        self.go_back_sign_up.setObjectName(u"go_back_sign_up")

        self.gridLayout.addWidget(self.go_back_sign_up, 0, 0, 1, 1)

        self.erruer_sign_password2 = QLabel(self.sign_up_page)
        self.erruer_sign_password2.setObjectName(u"erruer_sign_password2")
        self.erruer_sign_password2.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.gridLayout.addWidget(self.erruer_sign_password2, 14, 1, 1, 1)

        self.sign_password = QLabel(self.sign_up_page)
        self.sign_password.setObjectName(u"sign_password")

        self.gridLayout.addWidget(self.sign_password, 10, 0, 1, 1)

        self.sign_password2 = QLabel(self.sign_up_page)
        self.sign_password2.setObjectName(u"sign_password2")

        self.gridLayout.addWidget(self.sign_password2, 13, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_5, 16, 0, 1, 2)

        self.erreur_sign_password1 = QLabel(self.sign_up_page)
        self.erreur_sign_password1.setObjectName(u"erreur_sign_password1")
        self.erreur_sign_password1.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.gridLayout.addWidget(self.erreur_sign_password1, 11, 1, 1, 1)

        self.sign_nom_enter = QLineEdit(self.sign_up_page)
        self.sign_nom_enter.setObjectName(u"sign_nom_enter")

        self.gridLayout.addWidget(self.sign_nom_enter, 4, 1, 1, 1)

        self.sign_nom = QLabel(self.sign_up_page)
        self.sign_nom.setObjectName(u"sign_nom")

        self.gridLayout.addWidget(self.sign_nom, 4, 0, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_8, 6, 1, 1, 1)

        self.dateEdit = QDateEdit(self.sign_up_page)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setCalendarPopup(True)

        self.gridLayout.addWidget(self.dateEdit, 7, 1, 1, 1)

        self.label_2 = QLabel(self.sign_up_page)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(15)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 2)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_7, 9, 1, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_6, 12, 1, 1, 1)

        self.erreur_sign_nom = QLabel(self.sign_up_page)
        self.erreur_sign_nom.setObjectName(u"erreur_sign_nom")
        self.erreur_sign_nom.setStyleSheet(u"color: rgb(255, 0, 0);")

        self.gridLayout.addWidget(self.erreur_sign_nom, 5, 1, 1, 1)

        self.stackedWidget.addWidget(self.sign_up_page)
        self.log_in_page = QWidget()
        self.log_in_page.setObjectName(u"log_in_page")
        self.gridLayout_2 = QGridLayout(self.log_in_page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer_4, 6, 1, 1, 1)

        self.label_10 = QLabel(self.log_in_page)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font1)
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_2.addWidget(self.label_10, 1, 0, 1, 2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(150, -1, 150, -1)
        self.log_in_bout_fini = QPushButton(self.log_in_page)
        self.log_in_bout_fini.setObjectName(u"log_in_bout_fini")

        self.verticalLayout.addWidget(self.log_in_bout_fini)


        self.gridLayout_2.addLayout(self.verticalLayout, 8, 0, 1, 2)

        self.log_in_password = QLineEdit(self.log_in_page)
        self.log_in_password.setObjectName(u"log_in_password")

        self.gridLayout_2.addWidget(self.log_in_password, 5, 1, 1, 1)

        self.g_back_log_in = QPushButton(self.log_in_page)
        self.g_back_log_in.setObjectName(u"g_back_log_in")

        self.gridLayout_2.addWidget(self.g_back_log_in, 0, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer_3, 9, 0, 1, 1)

        self.log_in_nom = QLabel(self.log_in_page)
        self.log_in_nom.setObjectName(u"log_in_nom")

        self.gridLayout_2.addWidget(self.log_in_nom, 2, 0, 1, 1)

        self.log_in_nom_enter = QLineEdit(self.log_in_page)
        self.log_in_nom_enter.setObjectName(u"log_in_nom_enter")

        self.gridLayout_2.addWidget(self.log_in_nom_enter, 2, 1, 1, 1)

        self.login_password = QLabel(self.log_in_page)
        self.login_password.setObjectName(u"login_password")

        self.gridLayout_2.addWidget(self.login_password, 5, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 2, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 4, 1, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer_9, 3, 1, 1, 1)

        self.stackedWidget.addWidget(self.log_in_page)
        self.bienvenue_page = QWidget()
        self.bienvenue_page.setObjectName(u"bienvenue_page")
        self.gridLayout_3 = QGridLayout(self.bienvenue_page)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.bien_nomPutlisateur = QLabel(self.bienvenue_page)
        self.bien_nomPutlisateur.setObjectName(u"bien_nomPutlisateur")
        self.bien_nomPutlisateur.setFont(font1)
        self.bien_nomPutlisateur.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.bien_nomPutlisateur, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.bienvenue_page)

        self.horizontalLayout.addWidget(self.stackedWidget)


        self.retranslateUi(Form)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.welcome_texte.setText(QCoreApplication.translate("Form", u"Welcome to Mirabelle site", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Get an initial assessment", None))
        self.bout_sign_up.setText(QCoreApplication.translate("Form", u"Sign up", None))
        self.bout_log_in.setText(QCoreApplication.translate("Form", u"Log in", None))
        self.sign_password_enter1.setPlaceholderText(QCoreApplication.translate("Form", u"Entrer votre password", None))
        self.sign_date_naissance.setText(QCoreApplication.translate("Form", u"Date naissance:", None))
        self.signpassword2.setPlaceholderText(QCoreApplication.translate("Form", u"Entrer votre password", None))
        self.sign_up_fini_boutton.setText(QCoreApplication.translate("Form", u"Fini", None))
        self.go_back_sign_up.setText(QCoreApplication.translate("Form", u"go back", None))
        self.erruer_sign_password2.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.sign_password.setText(QCoreApplication.translate("Form", u"Password:", None))
        self.sign_password2.setText(QCoreApplication.translate("Form", u"Passowrd: ", None))
        self.erreur_sign_password1.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.sign_nom_enter.setPlaceholderText(QCoreApplication.translate("Form", u"Entrer votre nom", None))
        self.sign_nom.setText(QCoreApplication.translate("Form", u"Nom:", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Sign up", None))
        self.erreur_sign_nom.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Log in", None))
        self.log_in_bout_fini.setText(QCoreApplication.translate("Form", u"Fini", None))
        self.log_in_password.setPlaceholderText(QCoreApplication.translate("Form", u"Entrer votre pasword", None))
        self.g_back_log_in.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.log_in_nom.setText(QCoreApplication.translate("Form", u"Nom:", None))
        self.log_in_nom_enter.setPlaceholderText(QCoreApplication.translate("Form", u"Entrer votre nom", None))
        self.login_password.setText(QCoreApplication.translate("Form", u"Passowrd: ", None))
        self.bien_nomPutlisateur.setText(QCoreApplication.translate("Form", u"Bienvenue nom", None))
    # retranslateUi

