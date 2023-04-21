# Importo la libreria
from random import *

# Apro il mio file contenente le domande
with open("domande-esame.txt","r") as fout:
    domande=fout.read()

# Splitto in una variabile le singole righe del foglio di testo
frasi = domande.split("\n")

# Creo una lista vuota e ci inserisco successivamente le domande
lista_domande = []
for i in frasi:
    lista_domande.append(i)
        
# Creo una variabile che prenda un valore intero casuale tra 0 e la lunghezza della mia lista
n =(randint(0,len(lista_domande)))


# Stampo a schermo una domanda casuale
print(lista_domande[n])