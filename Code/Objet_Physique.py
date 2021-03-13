from Code.Point import Point

class Objet_Physique:
    #constante modifiable
    GRAVITE=10
    def __init__(self,Position,Masse,Velocite=Point(0,0)):
        self.Position = Position
        self.Masse = Masse
        self.Velocite = Velocite

    # affiche la masse, la valeur et le Velocité
    def __str__(self):
        return "p="+ str(self.Position)+",M="+str(self.Masse)+",V="+str(self.Velocite)

    #Actualise la position de l'objet en fonction de sa vélocité
    def Changer_Position(self):
        self.Position = self.Position + self.Velocite

    # actualise la vélocité de l'objet en fonction de la Gravité
    def Chute_Libre(self):
        self.Velocite.y = self.Velocite.y + self.GRAVITE




if __name__ == "__main__":
    test = Objet_Physique(Point(23,78),89,Point(1,9))

    print(test)
    test.Changer_Position()
    print(test)
    test.Chute_Libre()
    test.Changer_Position()
    print(test)