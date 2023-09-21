import pygame  # necessaire pour charger les images et les sons


class Joueur() : # classe pour créer le vaisseau du joueur
    def __init__(self) :
        self.sens = "O"
        self.position = 400
        self.image = pygame.image.load('background.png')