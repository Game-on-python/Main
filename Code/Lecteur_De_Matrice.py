import pygame

Tab_matrice = ["C:\Users\degru\Desktop\Cartable (2020-2021)\NSI\Projet jeux de platforme\Main\Texture\Niveaux 1\Bloc_de_terre_1.png" , "C:\Users\degru\Desktop\Cartable (2020-2021)\NSI\Projet jeux de platforme\Main\Texture\Niveaux 1\ciel.png" , "C:\Users\degru\Desktop\Cartable (2020-2021)\NSI\Projet jeux de platforme\Main\Texture\Niveaux 1\test_1.png" ,  "C:\Users\degru\Desktop\Cartable (2020-2021)\NSI\Projet jeux de platforme\Main\Texture\Niveaux 1\test_2.png"]
Taille_di_une_case = 64

def Lecteur_De_Matrice (x_depart, x_arrive,y_depart,y_arrive,matrice) :
    for i in range(max(x_depart,0),min(x_arrive,len(matrice))):
        for j in range(max(y_depart,0),min(y_arrive,len(matrice))):
            temporaire = matrice[i][j]
            sprite = Tab_matrice[temporaire]
            x=Taille_di_une_case*(i-x_depart)
            y=Taille_di_une_case*(j-y_depart)
            1=pygame.image.load("C:\Users\degru\Desktop\Cartable (2020-2021)\NSI\Projet jeux de platforme\Main\Texture\Niveaux 1\Bloc_de_terre_1.png")
            2=pygame.image.load("C:\Users\degru\Desktop\Cartable (2020-2021)\NSI\Projet jeux de platforme\Main\Texture\Niveaux 1\ciel.png")
            3=pygame.image.load("C:\Users\degru\Desktop\Cartable (2020-2021)\NSI\Projet jeux de platforme\Main\Texture\Niveaux 1\test_1")
            4=pygame.image.load("C:\Users\degru\Desktop\Cartable (2020-2021)\NSI\Projet jeux de platforme\Main\Texture\Niveaux 1\test_2")