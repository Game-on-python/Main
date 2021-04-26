def Charger_Level(Numeros_du_niveaux):
    matrice = __import__("Code.Level_"+str(Numeros_du_niveaux),fromlist=["Level_"+str(Numeros_du_niveaux)]).matrice
    return matrice