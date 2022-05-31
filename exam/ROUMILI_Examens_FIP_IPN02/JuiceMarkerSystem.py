from argparse import ArgumentError, ArgumentTypeError
from enum import Enum

class TypeGout(Enum) :
    The_Boost = 1
    The_Fresh = 2
    The_Fusion = 3
    The_Detox = 4

class TypeJus(Enum):
    Small = 0
    Medium = 1
    Large = 2


class Commande():
    _type = TypeJus.Small

    def __init__(self, type):
        self._type = type

    @property
    def JusSelectionnee(self):
        return self._type

    def Prix(self):
        return self._type


class Jus():
    _nom = ""
    _ingredients = ""
    _Disponibilite = 0


    def __init__(self, nom, ingredients, disponibilite):
        self._nom = nom
        self._ingredients = ingredients
        self._Disponibilite = disponibilite

    @property
    def nom(self):
        return self._nom

    @property
    def ingredients(self):
        return self._ingredients

    @property
    def disponibilite(self):
        return self._Disponibilite


class Borne():
    _listeJus = list()
    _JusSelectionne = list()
    _estPayee = False
    _estValidee = False

    @property
    def commander(self):
        total = 0
        for Commande in self._JusSelectionne:
            if Commande.type == TypeJus.Small:
                total += 0.5
            elif Commande.type == TypeJus.Medium:
                total += 1
            elif Commande.type == TypeJus.Large:
                total += 1.5
            else:
                raise ArgumentTypeError("TypeJus unknown!")

        return total

    @property
    def estAnnulee(self):
        return self._JusSelectionne == None

    @property
    def estValide(self):
        return self._JusSelectionne != None

    @property
    def estPayee(self):
        return self._estPayee

    @property
    def estValidee(self):
        return self._estValidee

    def consulterDiponibilite(self):
        return self._ListeDisponibilite

    def valider(self):
        if self.estValide:
            self._estValidee = True
        else:
            self._estValidee = False
        return self._estValidee

    def annulerCommande(self):
        self._JusSelectionne = list()
        self._estPayee = False
        self._estValidee = False

    def payer(self, somme):
        if not self.estValidee:
            raise BaseException("command must be confirmed!")

        reste = somme - self.commander
        if reste < 0:
            self._estPayee = False
        else:
            self._estPayee = True
        return (self._estPayee, reste)

    def imprimer(self):
        if not self.estValidee or not self.estPayee:
            raise BaseException("command must be confirmed and payed!")

        return True


    # init borne
    borne = Borne()
    print("borne initialisee!")

    # selection billet
    Juss = list()
    Jus.append(Jus(TypeJus.Small))
    Jus.append(Jus(TypeJus.Medium))
    JusSelectionne = borne.commande(Jus)
    print("Jus selectionne(s) ? %s" % JusSelectionne)

    # validation
    estValidee = borne.valider()
    print("commande validee ? %s" % estValidee)

    # payer
    (estPayee, reste) = borne.payer(26)
    print("commande payee (%d euros) ? %s" % (reste, estPayee))

    # imprimmer
    estImprimee = borne.imprimer()
    print("commande imprimee ? %s" % estImprimee)
