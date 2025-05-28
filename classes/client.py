from classes.personne import Personne
from datetime import datetime

class Client(Personne):
    def __init__(self, nom_complet, date_naissance:datetime,password1,password2):
        super().__init__(nom_complet, date_naissance,password1,password2)
        pass