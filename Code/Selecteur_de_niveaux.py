def Charger_Level_old(Numeros_du_niveaux):
    matrice = __import__("Level_"+str(Numeros_du_niveaux),fromlist=["Level_"+str(Numeros_du_niveaux)]).matrice
    return matrice

def Charger_Level(niveau):
    import json
    return json.load(open(f"Level_{niveau}.json","r"))