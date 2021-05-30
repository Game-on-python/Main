import pygame
from Code.Point import Point

class Bouton:
    def __init__(self,Position,largeur,hauteur,fonction,image):
        self.Position = Position
        self.largeur = largeur
        self.hauteur = hauteur
        self.fonction = fonction
        self.image = pygame.image.load(image)

    def click(self,Position_souris):
        #vérifie si la position de la sourie est bien sur le bouton
        return self.Position.x<=Position_souris.x<=self.Position.x + self.largeur -1 and self.Position.y<=Position_souris.y<=self.Position.y + self.hauteur -1

def credit():
    # Code RGB du noir et du blanc
    # la taille de l'image sera pris en compte dans le menus
    # fond = pygame.image.load("../Texture/Menu/Menu.png")
    BLUE = (60, 60, 255)
    # Taille de l'écran
    SIZE = (720, 500)
    # Création d'une fenêtre à la taille choisie
    pygame.display.set_caption("Pixel Run")
    screen = pygame.display.set_mode(SIZE)
    # l'horloge est utilisée pour le contrôle de la vitesse de rafraîchissement de l’écran
    clock = pygame.time.Clock()
    running_2 = True
    Boutons = [Bouton(Point(25, 10), 64, 64, lambda: False, "../Texture/Menu/fleche_quitter.png")]
    while running_2:
        # si user ferme la fenetre
        for event in pygame.event.get():
            mouse = pygame.mouse.get_pressed()
            if mouse[0]:
                Position_sourie = Point(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
                for b in Boutons:
                    if b.click(Position_sourie):
                        running_2 = b.fonction()
            # que l'event est fermeture de la fenetre
            if event.type == pygame.QUIT:
                running_2 = True
                print("Fermeture du jeu")
        # affichage de la matrice et du
        screen.fill(BLUE)
        screen.blit(pygame.image.load("../Texture/Menu/credit_menu.png"),(0,0))
        for b in Boutons:
            screen.blit(b.image, (int(b.Position.x), int(b.Position.y)))
        # --- ‘update’ l’écran avec le dessin des lignes
        pygame.display.flip()
        # --- limité à 60 ‘cadres’ par seconde
        clock.tick(60)




def menus():
    # Code RGB du noir et du blanc
    #la taille de l'image sera pris en compte dans le menus
    #fond = pygame.image.load("../Texture/Menu/Menu.png")
    BLUE = (60, 60, 255)
    # Taille de l'écran
    SIZE = (720, 500)
    # Création d'une fenêtre à la taille choisie
    pygame.display.set_caption("Pixel Run")
    screen = pygame.display.set_mode(SIZE)
    # l'horloge est utilisée pour le contrôle de la vitesse de rafraîchissement de l’écran
    clock = pygame.time.Clock()
    running_1 = True
    Boutons=[Bouton(Point(210,100),400,100,lambda:False,"../Texture/Menu/Bouton_Start2.png"),Bouton(Point(210,300),400,100,credit,"../Texture/Menu/credit2.png")]
    while running_1:
        # si user ferme la fenetre
        for event in pygame.event.get():
            mouse = pygame.mouse.get_pressed()
            if mouse[0]:
                Position_sourie=Point(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])
                for b in Boutons:
                    if b.click(Position_sourie):
                        running_1 = b.fonction()
            # que l'event est fermeture de la fenetre
            if event.type == pygame.QUIT:
                running_1 = True
                print("Fermeture du jeu")
        # affichage de la matrice et du
        screen.fill(BLUE)
        #screen.blit(fond,(0,0))
        for b in Boutons:
            screen.blit(b.image,(int(b.Position.x),int(b.Position.y)))
        # --- ‘update’ l’écran avec le dessin des lignes
        pygame.display.flip()
        # --- limité à 60 ‘cadres’ par seconde
        clock.tick(60)

if __name__ == "__main__":
    pygame.init()
    menus()
    pygame.quit()