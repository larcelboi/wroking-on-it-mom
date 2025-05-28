import jsonpickle

class Stockage:
    def __init__(self):
        self.dict_uer = {}
        self.id_user = []
    def sauvegarder(self):
        with open("stockage.json","w",encoding="utf-8") as file:
            file.write(jsonpickle.encode(self,indent=4))

    @staticmethod
    def load():
        try:
            with open("stockage.json","r",encoding="utf-8") as file:
                return jsonpickle.decode(file.read())
        except FileNotFoundError:
            return Stockage()

stocker_fichier = Stockage.load()