import pygame

class Joueur(pygame.sprite.Sprite):
    def __init__(self,x,y,skin,taille,largeur):
        self.x = x
        self.y = y
        self.skin = skin
        self.taille= taille
        self.largeur = largeur



    def image(self,skin):
        
