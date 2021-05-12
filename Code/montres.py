import pygame

from Code.Objet_Physique import Objet_Physique
from Code.Point import Point

#class Blob 
class Blob(Objet_Physique):
    Vitesse = 5
    Hauteur = 22
    Largeur = 28

    def collision_Haut_Gauche(self):
        return Point(self.Position.x, self.Position.y)
    def collision_Haut_Droite(self):
        return Point(self.Position.x + self.Largeur, self.Position.y)
    def collision_Bas_Gauche(self):
        return Point(self.Position.x , self.Position.y + self.Hauteur -1)
    def collision_Bas_Droite(self):
        return Point(self.Position.x+self.Largeur, self.Position.y + self.Hauteur -1)   
    