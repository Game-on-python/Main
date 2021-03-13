from Code.Objet_Physique import Objet_Physique
from Code.Point import Point


#la classe Joueur hérite de la classe Objet_Physique et hérite donc des méthodes
class Joueur(Objet_Physique):
    #constante modifiable
    Vittese_Deplacement = 5
    Puissance_Saut = 200

    #vas changer la vélocité du Joueur en fonction de la direction demandé
    def Bouger_Joueur(self,Direction_Gauche):
        # si Direction_Gauche est vrai : vas vers la gauche
        if Direction_Gauche:
            self.Velocite.x = -self.Vittese_Deplacement
        # sinon vas vers la Droite
        else:
            self.Velocite.x = +self.Vittese_Deplacement

    #Changer la véolicté y en fonction de sa puissance de Saut (qui est une constante modifiable)
    def Sauter(self):
        self.Velocite.y = -self.Puissance_Saut



if __name__ == "__main__":
    test= Joueur(Point(21,8),12)
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





