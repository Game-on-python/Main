import pygame

clock = pygame.time.Clock()
running = True
# Création d'une fenêtre à la taille choisie
pygame.display.set_caption("Pixel Run")
screen = pygame.display.set_mode((1000,700))


bouton = pygame.image.load("./fleche_quitter.png")

while running:
    # si user ferme la fenetre
    for event in pygame.event.get():
        # que l'event est fermeture de la fenetre
        if event.type == pygame.QUIT:
            running = False
            print("Fermeture du jeu")
    # affichage de la matrice et du
    screen.fill((0,0,0))
    screen.blit(bouton,(0,0))
    # --- ‘update’ l’écran avec le dessin des lignes
    pygame.display.flip()
    # --- limité à 60 ‘cadres’ par seconde
    clock.tick(60)