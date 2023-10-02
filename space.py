import pygame  # necessaire pour charger les images et les sons
import random
import math

class Joueur() : # classe pour créer le vaisseau du joueur
    
    def __init__(self) :
        self.sens = "O"
        self.position = 330
        self.image = pygame.image.load('vaisseau.png')
        self.score = 0
        self.hauteur = 470
        self.point_vie = 3
    
    def deplacer(self) :
        if self.sens=='gauche' and self.position!=0 :
            self.position-=10
        elif self.sens=='droite' and self.position!=735 :
            self.position+=10

    def marquer(self) :
        self.score += 1
    
    def perte_de_vie(self,coeur):
        self.point_vie-=1
        coeur.perdre_vie()
        return True
    
    def tirer(self) :
        pass
    
class Balle() :
    
    def __init__(self, tireur) :
        self.tireur = tireur
        self.depart = tireur.position + 48  # Stockez la position initiale
        self.hauteur = 492
        self.image = pygame.image.load('balle.png')
        self.etat = "chargee"
        self.vitesse = 30

    def bouger(self) :
        if self.etat == "attente" :
            self.depart = self.tireur.position + 48
            self.hauteur = 492
        elif self.etat == "tiree" :
            self.hauteur = self.hauteur - self.vitesse
        
        if self.hauteur < 0 :
            self.etat = "attente"
    
    def toucher(self, vaisseau):
        if (math.fabs(self.hauteur - vaisseau.hauteur) < 40) and (math.fabs(self.depart - vaisseau.depart) < 40) and self.etat=='tiree':
            self.etat = "attente"
            vaisseau.reapparaitre()
            return True

class Ennemi() :
    NbEnnemis = 6
    
    def __init__(self) :
        self.reapparaitre()
        self.depart = random.randint(1,700)
        self.hauteur = 10
        self.type = random.randint(1,6)
        if self.type == 1 :
            self.image = pygame.image.load("invader1.png")
            self.vitesse = 1
        elif self.type == 2 :
            self.image = pygame.image.load("invader2.png")
            self.vitesse = 1
        elif self.type == 3 :
            self.image = pygame.image.load("invader3.png")
            self.vitesse = 1
        elif self.type == 4 :
            self.image = pygame.image.load("invader4.png")
            self.vitesse = 1
        elif self.type == 5 :
            self.image = pygame.image.load("invader5.png")
            self.vitesse = 1
        elif self.type == 6 :
            self.image = pygame.image.load("invader6.png")
            self.vitesse = 1
            
    def avancer(self):
        self.hauteur = self.hauteur + self.vitesse
        if self.hauteur == 600 :
            self.hauteur = 0
        if self.hauteur > 700 :
            self.respawn()
    
    def reapparaitre(self):
        self.depart = random.randint(1,700)
        self.hauteur = 10
        self.type = random.randint(1,6)
        if self.type == 1 :
            self.image = pygame.image.load("invader1.png")
            self.vitesse = 1
        elif self.type == 2 :
            self.image = pygame.image.load("invader2.png")
            self.vitesse = 1
        elif self.type == 3 :
            self.image = pygame.image.load("invader3.png")
            self.vitesse = 1
        elif self.type == 4 :
            self.image = pygame.image.load("invader4.png")
            self.vitesse = 1
        elif self.type == 5 :
            self.image = pygame.image.load("invader5.png")
            self.vitesse = 1
        elif self.type == 6 :
            self.image = pygame.image.load("invader6.png")
            self.vitesse = 1
    
    def touchejoueur(self,joueur):
        if (math.fabs(self.hauteur - joueur.hauteur) < 40) and (math.fabs(self.depart - joueur.position) < 40):
            self.reapparaitre()
            return True
    
class Point_de_vie():
    def __init__(self, joueur):
        self.joueur = joueur
        self.position = 0
        self.hauteur = 0
        self.point_de_vie_image = pygame.image.load('coeur.png')

    def perdre_vie(self):
        self.position -= 200