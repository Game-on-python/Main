#sers à former un seule tableau au lieu de tableau dans un tableau
def tableau_aplatir(tableau):
    if len(tableau)==0:
        return []
    elif not isinstance(tableau[0],list):
        return [tableau[0]] + tableau_aplatir(tableau[1:])
    else:
        return tableau_aplatir(tableau[0]) + tableau_aplatir((tableau[1:]))


if __name__ == "__main__":
    test = [[1,67,9,1],
            [4,0,7,1,1]]
    print(isinstance(test,dict))
    print(tableau_aplatir(test))
