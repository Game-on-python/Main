from Code.Objet_Physique import Objet_Physique
from Code.Point import Point


# la classe Joueur hérite de la classe Objet_Physique et hérite donc des méthodes
class Joueur(Objet_Physique):
    # constante modifiable
    Vittese_Deplacement = 5
    Puissance_Saut = 11
    Hauteur = 32
    Largeur = 32

    # vas changer la vélocité du Joueur en fonction de la direction demandé
    def Bouger_Joueur(self, Direction_Gauche):
        # si Direction_Gauche est vrai : vas vers la gauche
        if Direction_Gauche:
            self.Velocite.x = -self.Vittese_Deplacement
        # sinon vas vers la Droite
        else:
            self.Velocite.x = +self.Vittese_Deplacement

    # Changer la véolicté y en fonction de sa puissance de Saut (qui est une constante modifiable)
    def Sauter(self):
        self.Velocite.y = -self.Puissance_Saut

    # accéde au pied du joueur pour ses colisions
    def Pied(self):
        return Point(self.Position.x + self.Largeur / 2, self.Position.y + self.Hauteur)

    def Tete(self):
        return Point(self.Position.x + self.Largeur / 2, self.Position.y)

    def collision_Haut_Gauche(self):
        return Point(self.Position.x, self.Position.y)

    def collision_Haut_Droite(self):
        return Point(self.Position.x + self.Largeur, self.Position.y)

    def collision_Bas_Gauche(self):
        return Point(self.Position.x, self.Position.y + self.Hauteur - 1)

    def collision_Bas_Droite(self):
        return Point(self.Position.x + self.Largeur, self.Position.y + self.Hauteur - 1)


if __name__ == "__main__":
    test = Joueur(Point(21, 8), 12)
    print(test)
    test.Bouger_Joueur(True)
    print(test)
    test.Changer_Position()
    print(test)
    test.Sauter()
    test.Changer_Position()
    print(test)
    test.Chute_Libre()
    test.Changer_Position()
    print(test)
