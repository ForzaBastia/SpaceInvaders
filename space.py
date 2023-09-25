import pygame  # necessaire pour charger les images et les sons
import random
import math

class Joueur() : # classe pour créer le vaisseau du joueur
    
    def __init__(self) :
        self.sens = "O"
        self.position = 330
        self.image = pygame.image.load('vaisseau.png')
        self.score = 0
    
    def deplacer(self) :
        if self.sens=='gauche' and self.position!=0 :
            self.position-=5
        elif self.sens=='droite' and self.position!=735 :
            self.position+=5

    def marquer(self) :
        self.score += 1
        
    
    def tirer(self) :
        pass


class Balle() :
    
    def __init__(self, tireur) :
        self.tireur = tireur
        self.depart = tireur.position + 48
        self.hauteur = 492
        self.image = pygame.image.load('balle.png')
        self.etat = "chargee"
        self.vitesse = 10
    
    def bouger(self) :
        if self.etat == "attente" :
            self.depart = self.tireur.position + 30
            self.hauteur = 492
        elif self.etat == "tiree" :
            self.hauteur = self.hauteur - self.vitesse
        
        if self.hauteur < 0 :
            self.etat = "attente"

    def toucher(self, vaisseau) :
        if (math.fabs(self.hauteur - vaisseau.hauteur) < 40) and (math.fabs(self.depart - vaisseau.depart) < 40) :
            self.etat = "attente"
            return True

class Ennemi() :
    NbEnnemis = 6
    
    def __init__(self) :
        self.depart = random.randint(1,700)
        self.hauteur = 10
        self.type = random.randint(1,2)
        if self.type == 1 :
            self.image = pygame.image.load("invader1.png")
            self.vitesse = 0.1
        elif self.type == 2 :
            self.image = pygame.image.load("invader2.png")
            self.vitesse = 0.2
            
    def avancer(self):
        self.hauteur = self.hauteur + self.vitesse

    def disparaitre(self) :
        self.depart = random.randint(1,700)
        self.hauteur = 10
        self.type = random.randint(1,2)
        if self.type == 1 :
            self.image = pygame.image.load("invader1.png")
            self.vitesse = 0.1
        elif self.type == 2 :
            self.image = pygame.image.load("invader2.png")
            self.vitesse = 0.2