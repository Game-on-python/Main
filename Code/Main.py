import pygame
import Joueur
import Lecteur_De_Matrice



pygame.init()

# Code RGB du noir et du blanc
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
# Taille de l'écran
SIZE = (700, 500)



# Code RGB du noir et du blanc
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
# Taille de l'écran
SIZE = (700, 500)


# Création d'une fenêtre à la taille choisie
pygame.display.set_caption("Pixel Run")
screen = pygame.display.set_mode(SIZE)

running = True 
#boucle tant que cette condition est vraie (running)
while running :
  #si user ferme la fenetre
  for event in pygame.event.get():
    #que l'event est fermeture de la fenetre
      if event.type == pygame.QUIT :
        running = False
        pygame.quit()
        print("Fermeture du jeu")


matrice = [[1,0,2,3]
           [1,2,3,4]]


