import pygame # importation de la librairie pygame
import space
import sys # pour fermer correctement l'application

# lancement des modules inclus dans pygame
pygame.init() 
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Space Invaders")

# chargement de l'image de fond
fond = pygame.image.load('background.png')
fin_screen = pygame.Surface((800,600))
fin_fond = pygame.image.load('game_over.png')
fin = False

# creation du joueur
player = space.Joueur()

# creation de la balle
tir = space.Balle(player)
tir.etat = "chargee"
# creation des points de vie
listePv = []
for indice in range(player.point_vie):
    pv = space.Point_de_vie(player)
    listePv.append(pv)

# creation des ennemis
listeEnnemis = []
for indice in range(space.Ennemi.NbEnnemis):
    vaisseau = space.Ennemi()
    listeEnnemis.append(vaisseau)

# creation du score

### BOUCLE DE JEU  ###
running = True # variable pour laisser la fenêtre ouverte

while running : # boucle infinie pour laisser la fenêtre ouverte
    # dessin du fond
    screen.blit(fond,(0,0))
    temps_actif = pygame.time.get_ticks()
    ### Gestion des événements  ###
    for event in pygame.event.get(): # parcours de tous les event pygame dans cette fenêtre
        if event.type == pygame.QUIT : # si l'événement est le clic sur la fermeture de la fenêtre
            running = False # running est sur False
            sys.exit() # pour fermer correctement
       
       # gestion du clavier
        if event.type == pygame.KEYDOWN : # si une touche a été tapée KEYUP quand on relache la touche
            if event.key == pygame.K_LEFT : # si la touche est la fleche gauche
                player.sens = "gauche" # on déplace le vaisseau de 1 pixel sur la gauche
            elif event.key == pygame.K_RIGHT : # si la touche est la fleche droite
                player.sens = "droite" # on déplace le vaisseau de 1 pixel sur la gauche
            elif event.key == pygame.K_SPACE : # espace pour tirer
                player.tirer()
                tir.etat = "tiree"
        else :
            player.sens= "O"
    if player.point_vie <= 0:
        fin = True
        screen.blit(fin_fond,(0, 0))
    ### Actualisation de la scene ###
    # Gestions des collisions
    for ennemi in listeEnnemis:
        if tir.toucher(ennemi):
            player.marquer()
            print(f"Score : {player.score} points")
        if ennemi.touchejoueur(player)==True:
            player.perte_de_vie(pv)
            print(f'Point de vie : {player.point_vie}')
            if len(listePv)==0:
                listePv.pop(player.point_vie)
    
    font = pygame.font.SysFont("Pixeltype.ttf", 0)
    score_display = font.render(f'Score : {player.score}', 1, (255,255,0))
    screen.blit(score_display, (25, 25))
    
    # placement des objets
    # le joueur
    player.deplacer()
    screen.blit(tir.image,[tir.depart,tir.hauteur]) # appel de la fonction qui dessine le vaisseau du joueur
    # les cœurs de vie
    x = 0
    for point_vie in listePv:
        screen.blit(point_vie.point_de_vie_image,[point_vie.position + x, point_vie.hauteur])
        x += 30
    # la balle
    tir.bouger()
    screen.blit(player.image,[player.position,player.hauteur])# appel de la fonction qui dessine le vaisseau du joueur
    # les ennemis
    for ennemi in listeEnnemis:
        ennemi.avancer()
        screen.blit(ennemi.image,[ennemi.depart, ennemi.hauteur]) # appel de la fonction qui dessine le vaisseau du joueur
    if fin:
        screen.blit(fin_fond, (0, 0))
        font = pygame.font.SysFont("Pixeltype.ttf", 40)
        fin_text = font.render("Game Over", 1, (255, 0, 0))
        score_text = font.render(f'Score : {player.score}', 1, (255, 255, 0))
        screen.blit(fin_text, (200, 250))
        screen.blit(score_text, (200, 300))
    
    pygame.display.update() # pour ajouter tout changement à l'écran