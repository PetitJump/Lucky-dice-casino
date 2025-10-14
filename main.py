from random import randint
import random
import os
from time import sleep

class Jeu:
    def __init__(self, argent_base: int, signe: list[str]):
        self.__argent = argent_base
        self.__signe = signe
        self.__signe_sorti = ""
    
    def run(self):
        while self.__argent > 0:
            continuer = True
            while continuer:
                clear()
                print(f"Vous avez {self.__argent}$")
                mise = int(input(f'Combien voulez vous miser : '))
                clear()
                if self.__argent - mise >= 0:
                    continuer = False
                    self.__argent -= mise
                    choix_signe = True
                    while choix_signe:
                        clear()
                        print("Voici les signes possibles")
                        for i in range(len(self.__signe)):
                            print(f"{i + 1} : {self.__signe[i]}")
                        try:
                            choix = self.__signe[int(input("Quel signe voulez vous choisir : ")) - 1]
                            break
                        except Exception:
                            print("Pas possible")
                else:
                    print("Vous n'avez pas assez d'argent")
            clear()
            print("Nous allons tirer les de")
            sleep(3)
            self.__signe_sorti = random.choice(self.__signe)
            self.animation()
            if self.__signe_sorti == choix:
                self.__argent += mise * 2
        clear()
        print("Vous n'avez plus d'argent")    
        
    def animation(self):
        """Simule un lancer de des
        """
        clear()
        for i in range(30, 1, -1):
            print(self.__signe[i % len(self.__signe)])
            if i < 7:
                sleep(0.3)
            else:
                sleep(0.1)
            clear()
        print(self.__signe_sorti)
        sleep(2)
        print(f"Le signe sorti est : {self.__signe_sorti}")
        sleep(4)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear') #Cleat le terminal

################ Variable ################
argent = 100
signes = ["Policier", "Telephone", "Anneau", "Train", "Robinet", "Ampoule"]


Partie_en_cour = Jeu(argent, signes)
Partie_en_cour.run()