import pygame

Tab_matrice = [pygame.image.load("../Texture/Niveaux 1/Bloc_de_terre_1.png") ,pygame.image.load("../Texture/Niveaux 1/ciel.png") , pygame.image.load("../Texture/Niveaux 1/test_1.png") , pygame.image.load("../Texture/Niveaux 1/test_2.png")]
Taille_di_une_case = 64

def Lecteur_De_Matrice (x_depart, x_arrive,y_depart,y_arrive,matrice,Screen) :
    for i in range(max(x_depart,0),min(x_arrive,len(matrice))):
        for j in ra   nge(max(y_depart,0),min(y_arrive,len(matrice[i]))):
            temporaire = matrice[i][j]
            sprite = Tab_matrice[temporaire]
            y=Taille_di_une_case*(i-x_depart)
            x=Taille_di_une_case*(j-y_depart)
            Screen.blit(sprite,(x,y))
