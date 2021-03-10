import pygame

class Joueur(pygame.sprite.Sprite):
    def __init__(self,x,y,skin,taille,largeur):
        self.x = x
        self.y = y
        self.skin = skin
        self.taille= taille
        self.largeur = largeur



    def joueur(self,skin):
        skin =pygame.image.load("idée perso.png")
        skin = pygame.transform.scale((110, 110))
        self.skin = pygame.Surface((34,34))
        mouvement =





