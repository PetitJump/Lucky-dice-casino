# Lucky-dice-casino

Ce projet est un petit jeu de pari sur la console dans lequel le joueur mise une somme d’argent sur un symbole. Un symbole aléatoire est ensuite tiré, et le joueur gagne ou perd selon le résultat.

# Fonctionnement du jeu
Le joueur commence avec un montant d’argent défini (par défaut : 100$).

À chaque tour :
- Il choisit combien il veut miser.
- Il sélectionne un symbole parmi une liste.
- Une animation simule un tirage.
Si le symbole tiré correspond à celui choisi, le joueur remporte le double de sa mise.

La partie continue jusqu’à ce que le joueur n’ait plus d’argent.


## Variables modifiables

- argent = 100
- signes = ["Policier", "Telephone", "Anneau", "Train", "Robinet", "Ampoule"]

Tu peux donc modifier :
- Le montant de départ
- La liste des symboles disponibles