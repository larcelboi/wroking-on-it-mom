from datetime import datetime,date
import random

from PySide6.QtCore import QDate


class Personne:
    def __init__(self, nom_complet, date_naissance:datetime,password1,password2):
        self.liste_erreur = []
        self.id  = random.choice(range(10000))

        self.nom_complet = nom_complet
        self.date_naissance = date_naissance
        self.password1 = password1
        self.password2 = password2


    @property
    def nom_complet(self):
        return self._nom_complet

    @nom_complet.setter
    def nom_complet(self, nom_complet):
        self.verification_nom(nom_complet)

    def verification_nom(self,nom_complet):
        try:
            if isinstance(nom_complet, str) and nom_complet.strip() != "":
                self._nom_complet = nom_complet
            else:
                raise ValueError("Vous devez entrer un nom")
        except Exception as e:
            self.liste_erreur.append(e)

    @property
    def date_naissance(self):
        return self._date_naissance

    @date_naissance.setter
    def date_naissance(self,date_naissance):
        self.verification_date(date_naissance)

    def verification_date(self,date_naissance):
        nouv_date = date_naissance.toPython()
        try:
            if isinstance(nouv_date, date):
                self._date_naissance = nouv_date
            else:
                raise ValueError("date invalide ")
        except Exception as e:
            self.liste_erreur.append(e)

    @property
    def password1(self):
        return self._password1
    @password1.setter
    def password1(self,password1):
        self.verification_password(password1=password1)

    @property
    def password2(self):
        return self._password2
    @password2.setter
    def password2(self,password2):
        self.verification_password(password2=password2)

    def verification_password(self,password1=None,password2=None):

        if password1 is not None:
            try:
                if isinstance(password1, str) and password1.strip() != "":
                    self._password1 = password1
                else:
                    raise ValueError("Vous devez entrer un password1")
            except Exception as e:
                self.liste_erreur.append(e)
        elif password2 is not None:
            try:
                if isinstance(password2, str) and password2.strip() != "":
                    self._password2 = password2
                else:
                    raise ValueError("Vous devez entrer un password2")
            except Exception as e:
                self.liste_erreur.append(e)

    def __str__(self):
        return f"ID: {self.id} Nom: {self.nom_complet} - Date naissance: {self.date_naissance} - Password1: {self.password1} - Password2: {self.password2}"

