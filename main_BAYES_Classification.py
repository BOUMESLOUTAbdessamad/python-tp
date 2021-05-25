# coding=utf-8
"""
Programme permettant d'appliquer la lois de BAYES pour la classification
de un cas de pré-detection de mauvais commentaires de consomateurs
"""

# coding=utf-8
# Importation de la bibliothèque Pandas pour la lecture du fichier .csv
import pandas as pnd

# Fonction permettant de lire un fichier .csv et retourne le contenu du fichier sous le format DataFrame de Pandas
from pandas import DataFrame


def readCSVfile(fileName) :
    nRowsRead = None  # None pour la lecture de tout le fichier sinon on détermine le nombre de lignes
    try:
        print("\nLecture du fichier ... "+fileName+"\n")
        fichier = pnd.read_csv(fileName, delimiter=';', nrows=nRowsRead)
        return fichier
    except IOError:
        print("Fichier innaccessible !")
        exit()

def pos_probability(data) :
    classes = data['Classe'].tolist();
    pos = 0;
    for c in classes:
        if c== 1 :
            pos +=1;

    result = pos / classes.__len__()
    return float(result);

def neg_probability(data) : # cls for class

    classes = data['Classe'].tolist();
    neg = 0;
    for c in classes:
        if c == 0:
            neg += 1;
    result = neg / classes.__len__()
    return float(result);

# Fonction main :
if __name__ == '__main__':
    # Lecture du fichier CSV contenant la base de donnée :
    data = readCSVfile("BaseAvisConsomateurs.csv")
    #print("Voici un aperçu des 3 premières lignes du fichier : \n")
    #print(data.head(3))

    # Nombre de lignes et de colonnes :
    nRow, nCol = data.shape
    dataList = data.values.tolist() #Conversion en liste
df = DataFrame(dataList, columns=['Quality', 'Livraison', 'ProduitConforme', 'Classe'])

#les probabilités à priori de chaque caractéristique
print(neg_probability(df) )

