# coding=utf-8
from __future__ import division

#1
def AffichageTransactions(transactions) :
    for trans in transactions:
        print ("Ticket N°" + str(trans) + " : " + str(transactions[trans]))

#2
def NombreTransactions(transactions) :
    sizes = []
    for trans in transactions :
        sizes.append(len(transactions[trans]));

    print("\nNombre d'articles par ticket : \n" + str(sizes))

#3
def GetUniqueValues(transactions) :
    result = []
    for trans in transactions :
        for t in transactions[trans] :
            if t in result : # check value existance
                continue
            else :
                result.append(t)
    return result


#4
def GetOneItemFrequences(transactions, itemsList, minsup) :
    result = {}
    #supp = freq(x) / n
    for item in itemsList:
        freq = 0
        supp = 0
        for trans in transactions :
            if item in transactions[trans]:
                freq += 1;

        supp = freq/len(transactions)
        if supp > minsup :
            result[item] = round(supp, 2)

    return result

if __name__ == '__main__':

    # données d'entrée de l'algorithme
    transactions = {1: ['A', 'B', 'E', 'C'],
                    2: ['A', 'E', 'F'],
                    3: ['A', 'B', 'C'],
                    4: ['A', 'B', 'C', 'D', 'F'],
                    5: ['A', 'C', 'F', 'B'],
                    6: ['B', 'F', 'C'],
                    7: ['C', 'A', 'F', 'B'],
                    8: ['D', 'E', 'F'],
                    9: ['F', 'E', 'B']}

    #1 Afficahge des transactions
    AffichageTransactions(transactions);

    #2 Nbr d'articles par ticket
    NombreTransactions(transactions);

    #3 Unique values
    print("Les valeurs qui sont dans les articels : \n" + str(GetUniqueValues(transactions)));

    #4 minsup = 0.5
    print ( "Itemset a un articles avec leur frequences : \n" + str(GetOneItemFrequences(transactions, GetUniqueValues(transactions), 0.5)))


