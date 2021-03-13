
class Point:
    def __init__(self,x,y):
        self.x = float (x)
        self.y = float (y)
    # convertit x et y en chaine de caractère pour l'affichage
    def __str__(self):
        return "("+str(self.x) +(",")+ str(self.y)+")"

    # additionne les points self et value entre eux
    def __add__(self,value):
        if type(value).__name__== "Point":
            self.x = self.x + value.x
            self.y = self.y + value.y
        return self

    # meme fonction
    def __radd__(self,value):
        return value.__add__(self)



if __name__ == "__main__":
    test = Point(4.5,8.9)

    print(test)
    test= test+Point(6,9)
    print(test)

