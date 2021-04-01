import pygame
from Code.Joueur import Joueur
from Code.Lecteur_De_Matrice import Lecteur_De_Matrice
from Code.Test_matrice import matrice
from Code.Point import Point



pygame.init()

# Code RGB du noir et du blanc
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
# Taille de l'écran
SIZE = (700, 500)
# l'horloge est utilisée pour le contrôle de la vitesse de rafraîchissement de l’écran
clock = pygame.time.Clock()


#apparition du personnage
J1=Joueur(Point(0,0),0.04,Point(1,0))
Sprite_J1=pygame.image.load('../Texture/Joueur/Heros_vue_de_cote.png')
# Création d'une fenêtre à la taille choisie
pygame.display.set_caption("Pixel Run")
screen = pygame.display.set_mode(SIZE)


running = True 
#boucle tant que cette condition est vraie (running)
while running :
  #récupère un morceaux de la colonne de la matrice dans lequelle le joueur est entrain de tomber
  tranche = [matrice[i][int(J1.Pied().x//64)] for i in range(int(J1.Pied().y//64),int((J1.Pied().y + J1.Velocite.y)//64+1))]
  # détermine si c'est un bloc plein ou pas (collision)
  if 0 in tranche:
    if J1.Velocite.y!=0:
      y_Block=tranche.index(0)
      J1.Velocite.y=((J1.Pied().y//64 + y_Block)*64) - J1.Pied().y
  else:
    J1.Chute_Libre()
  J1.Changer_Position()
  #si user ferme la fenetre
  for event in pygame.event.get():
    #que l'event est fermeture de la fenetre
      if event.type == pygame.QUIT :
        running = False
        print("Fermeture du jeu")
  # affichage de la matrice et du joueur
  screen.fill(BLACK)
  Lecteur_De_Matrice(0, 10, 0, 10, matrice, screen)
  screen.blit(Sprite_J1, (int(J1.Position.x), int(J1.Position.y)))
  # --- ‘update’ l’écran avec le dessin des lignes
  pygame.display.flip()
  # --- limité à 60 ‘cadres’ par seconde
  clock.tick(60)


pygame.quit()







