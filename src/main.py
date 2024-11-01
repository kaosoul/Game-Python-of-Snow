"""
Le château au sommet du Python des Neiges
Auteur : Hervé Darce
Date : octobre 2024
C'est un jeu d’évasion dans lequel le joueur commande au
clavier les déplacements d’un personnage au sein d’un « château »
représenté en plan. Le château est constitué de cases vides (pièces,
couloirs), de murs, de portes, que le personnage ne pourra franchir qu’en
répondant à des questions, d’objets à ramasser, qui l’aideront à trouver
les réponses à ces questions et de la case de sortie / quête du château.
Le but du jeu est d’atteindre cette dernière.
Pixel château : coordonnées dans le plan du château
Pixel turtle : coordonnées dans la fenêtre turtle
Entrée : Une interaction avec le jeu en utilisant les touches "Left",
         "Right", "Up" et "Down" pour le déplacement et la touche "q"
         pour quitter le jeu
Résultat : Une fenêtre Turtle dans laquelle s'inscrit le jeu
"""


# Importation des modules


from CONFIGS import *
import turtle


# Définitions des constantes globales


NB_MAXIMUM_INVENTAIRE = 25   # Nombre maximum de caractères sur une ligne dans la cadre inventaire
LIGNES_MAXIMUM_INVENTAIRE = 23   # Nombre de lignes maximum dans le cadre inventaire
NB_MAXIMUM_ANNONCE = 73   # Nombre maximum de caractères sur une ligne dans la cadre inventaire
LIGNES_MAXIMUM_ANNONCE = 2   # Nombre de lignes maximum dans le cadre inventaire
TITRE = 'Le château au sommet du Python des Neiges'   # Titre de la fenêtre turtle
DIMENSION = 500   # Dimension horizontale et verticale de la fenêtre turtle
VITESSE_TURTLE = 'fastest'   # Vitesse de déplacement de curseur turtle
ZONE_ANNONCES_MAXI = (240, 240)   # Coin supérieur droit du cadre d'annonces
ZONE_ANNONCES_MINI = (-240, 210)   # Coin inférieur gauche du cadre d'annonces
ZONE_INVENTAIRE_MAXI = (240, 200)   # Coin supérieur droit du cadre inventaire
PADX = 0   # Ecart horizontal entre le texte et le cadre
PADY = 31   # Ecart vertical entre le texte et le cadre
PAD_CADRE = 10   # Espacement entre les cadres
FONTNAME = 'Arial'   # Police de caractère du texte
FONTTYPE = 'normal'   # Fonttype de la police de caractère du texte
SIZE_TITRE = 12   # Taille de la police de caractère du titre inventaire
SIZE_NORMAL = 10   # Taille de la police de caractère du texte normal
COULEUR_CADRE = 'black'   # Couleur du cadre des zones inventaires et annonces


# Définitions des fonctions


def tracer_case(case, couleur, pas):
    """
    Tracer un carre de couleur aux coordonnées pixel château du plan du
    château
    Entrées : (tuple) case : les coordonnées de la case dans le plan du
              château
              (str) couleur : du trait et de l'intérieur de la case
              (int) pas : côté de la case du château exprimé dans la
              fenêtre turtle
    Sortie : Dessin d'une case de couleur
    """
    turtle.up()   # Désactiver le dessin
    turtle.goto(coordonnees(case,pas))   # Aller au coin inférieur gauche de la case
    turtle.color(couleur)   # Couleur du trait et de l'intérieur
    turtle.begin_fill()   # Commencer le remplissage de l'intérieur de la case
    turtle.down()   # Activer le dessin
    tracer_carre(pas)   # Trace un carre
    turtle.up()   # Désactiver le dessin
    turtle.end_fill()   # Fin du remplissage de la case


def tracer_carre(dimension):
    """
    Tracer un carre de côté "dimension - 2" qui est la brique élémentaire
    Le "+1" ou le "-1" de mettre l'origine du tracé en tenant compte un
    espace vide entre les carrés. Le "+2" ou le "-2" permet de tenir
    compte des espaces vides à gauche et à droite ou en haut et en bas.
    Entrée : (int) dimension : côté du carré exprimé dans la fenêtre
             turtle
    Sortie : dessin d'un carré
    """
    turtle.up()    # Désactiver le dessin
    turtle.goto((turtle.position()[0]+1,
                 turtle.position()[1]+1))   # Coin inférieur gauche
    turtle.down()    # Activer le dessin
    turtle.goto((turtle.position()[0]+dimension-2,
                 turtle.position()[1]))   # Coin inférieur droit
    turtle.goto((turtle.position()[0],
                 turtle.position()[1]+dimension-2))   # Coin supérieur droit
    turtle.goto((turtle.position()[0]-dimension+2,
                 turtle.position()[1]))   # Coin supérieur gauche
    turtle.goto((turtle.position()[0],
                 turtle.position()[1]-dimension+2))   # Coin inférieur droit
    turtle.up()    # Désactiver le dessin
    turtle.goto((turtle.position()[0]-1,
                 turtle.position()[1]-1))   # Revenir à la position initiale

    
def tracer_rectangle(point_mini, point_maxi):
    """
    Tracer un rectangle avec les coordonnées du coin inférieur gauche
    et du coin supérieur droit
    Entrées : (tuple) point_mini : point du coin inférieur gauche du cadre
              (tuple) point_maxi : point du coin supérieur droit du cadre
    Sortie : Dessin d'un rectangle
    """
    turtle.up()   # Désactiver le dessin
    turtle.goto(point_mini)   # Aller aux coordonnées du coin inférieur gauche
    turtle.down()   # Activer le dessin
    turtle.goto(point_maxi[0], point_mini[1])   # Dessiner le rectangle
    turtle.goto(point_maxi)
    turtle.goto(point_mini[0], point_maxi[1])
    turtle.goto(point_mini) 
    turtle.up()   # Désactiver le dessin

    
def coordonnees(case, pas):
    """
    Cacul des coordonnées dans la fenêtre turtle à partir des coordonnées
    dans le plan du château
    Enrées : (tuple) case: les coordonnées de la case dans le plan
             du château en pixel château
             (int) pas : le côté de la case exprimé dans la fenêtre
             turtle
    Sortie : (tuple) coordonnées dans la fenêtre turtle du coin inférieur
             gauche de la case
    """
    return  ZONE_PLAN_MINI[0] + case[1]*pas , ZONE_PLAN_MAXI[1] - (case[0]+1)*pas


def coordonnees_inverse(position_w, pas):
    """
    Cacul des coordonnées dans le plan du château en pixel château
    Enrées : (tuple) position_w : les coordonnées du coin inférieur
             gauche de la case en pixel turtle
             (int) pas : le côté de la case exprimé dans la fenêtre
             turtle
    Sortie : (tuple) coordonnées dans le plan du château en pixel château
    """
    return  (int(ZONE_PLAN_MAXI[1] - position_w[1])//pas - 1,
             int((position_w[0] -ZONE_PLAN_MINI[0])//pas))


def inventaire_cadre(matrice, pas):
    """
    Construction du cadre inventaire avec ou non la liste des objets acquis
    par le personnage.
    Entrées : (matrice) matrice : représente le plan du château
              (int) pas : le côté de la case exprimé dans la fenêtre
              turtle
              (list) sac_m : liste des objets acquis
    Sortie : Affiche le contenu des objets acquis dans le cadre inventaire
    """
    point_maxi =  ZONE_INVENTAIRE_MAXI   # Coin supérieur droit du cadre inventaire
    point_mini = (len(matrice[0])*pas + ZONE_PLAN_MINI[0] + PAD_CADRE,
                  ZONE_PLAN_MAXI[1]- len(matrice)*pas) # Coin inférieur gauche du
                                                       # cadre inventaire
    affichage_texte('Inventaire', PADX, PADY,
                    point_mini, point_maxi, SIZE_TITRE,
                    'center')   # Titre du cadre inventaire
    if sac_m:   # Liste non vide des objets dans la liste sac_m, afficher la liste
        affichage_texte('* ' + '\n* '.join(sac_m), 3, len(matrice) *pas ,
                        point_mini, point_maxi, SIZE_NORMAL, 'left',
                        LIGNES_MAXIMUM_INVENTAIRE, False)   # Afficher tous les objets acquis
                                                     # dans l'iventaire
                                                     # dans la limite du cadre
    

def affichage_paragraphe(texte, nb_maximum):
    """
    Mettre le texte sur plusieurs lignes si la longueur du texte dépasse
    le nombre maximum de caractères nb_maximum
    Entrée : (str) texte
             (int) nb_maximum : nombre maximum de caractères par ligne
    Sortie : (str) texte : découpé en plusieurs lignes avec \n
    """
    chaine = texte.strip()   # Copier la chaine de caractère
    lignes = []   # Création d'une liste de lignes vides
    while chaine:   # Boucle à la recherche de la dernière ligne du paragraphe
        j = chaine.find(' ', 0)
        i = 0
        while i < len(chaine) and j < nb_maximum and j != -1: # Boucle à la recherche du dernier
                                                              # espace de la ligne
            j = chaine.find(' ', j+1)
            if j > i:
                i +=j
            else:
                i +=1
        if j != -1 and i > nb_maximum:   # Fin de la recherche du dernier espace de la ligne
                                         # si la longueur maximale de la chaîne est atteinte
                                         # ou s'il n'y a plus de caractère espace
            lignes.append(chaine[:j].strip())   # Ajouter la ligne à la liste lignes
            chaine = chaine[j:]   # Enlever de la chaîne de caractère la ligne ajouter
                                  # à la liste lignes
        if len(chaine) < nb_maximum: # Ajouter la dernière ligne à la liste lignes
            lignes.append(chaine.strip())
            chaine = ''   # Définir chaine à '' pour interrompre la première boucle
    return '\n'.join(lignes)   # Mettre \n entre les lignes


def emplacement_texte(point_mini, point_maxi, padx, pady, alignement):
    """
    Définir l'emplacement du texte par rapport aux caractéristiques du cadre et l'alignement
    Entrées : (tuple) point_mini : point du coin inférieur gauche du cadre
              (tuple) point_maxi : point du coin supérieur droit du cadre
              (int) padx : espace horizontal gauche avant le texte
              (int) pady : espace vertical haut avant le texte
              (str) alignement : texte 'center' sinon 'left'
    Sorties : (tuple) emplacement : coordonnées du début du texte
    """
    if alignement == 'center':
        emplacement = ((point_maxi[0] - point_mini[0])//2 + point_mini[0],
                       point_maxi[1] - pady)   # Coordonnées du point si alignement 'center'
    else:
        emplacement = (point_mini[0] + padx,
                       point_maxi[1] - pady)   # Coordonnées du point pour les autres cas
    return emplacement   # Coordonnées de l'emplacement du texte


def effacer_texte(point_mini, point_maxi):
    """
    Effacer le texte qui se trouve dans le cadre défini par le coin
    inférieur gauche point_mini et le coin supérieur droit
    point_maxi
    Entrées : (tuple) point_mini : point du coin inférieur gauche du cadre
              (tuple) point_maxi : point du coin supérieur droit du cadre
    Sortie : Dessiner un rectangle pour effacer le texte
    """
    turtle.color(COULEUR_CADRE,COULEUR_EXTERIEUR)   # Couleur du trait du cadre puis de l'intérieur
    turtle.begin_fill()
    turtle.down()
    tracer_rectangle(point_mini, point_maxi)   # Tracer le cadre vide
    turtle.up()
    turtle.end_fill()


def reduction_texte(texte, lignes_maximum):
    """
    Réduire le nombre de ligne, s'il dépasse le maximum lignes_maximum
    pour que le texte rentre dans le cadre
    Entrées : (str) texte
              (int) lignes_maximum : nombre de lignes maximum
    Sortie : (str) texte_new nouveau texte réduit à un nombre maximum
             de lignes lignes_maximum
    """
    liste_new = []   # liste_new qui va accueillir les lignes sélectionnées
    liste = texte.strip().split('\n')   # Création d'un liste de lignes
                                        # à partir du texte
    if len(liste) <= lignes_maximum:
        texte_new = texte.strip()
    else:
        for i in range(len(liste)-lignes_maximum, len(liste)):
            liste_new.append(liste[i])   # Ajouter les LIGNES_MAXIMUM_INVENTAIRE dernières
        texte_new = '\n'.join(liste_new)
    return texte_new   # Nouvelle chaîne de caractères réduites
    

def affichage_texte(texte, padx, pady, point_mini, point_maxi, size, alignement,
                    lignes_maximum=1, efface=True):
    """
    Affichage du texte dans un cadre défini par le coin inférieur gauche
    point_mini et le coin supérieur droit point_maxi
    Entrées : (string) texte : à afficher dans le cadre
              (int) padx : espace horizontal gauche avant le texte
              (int) pady : espace vertical haut avant le texte
              (tuple) point_mini : point du coin inférieur gauche du cadre
              (tuple) point_maxi : point du coin supérieur droit du cadre
              (int) size : taille de la police de caractère
              (str) alignement : texte 'center', 'left' (par défaut)
              (int) lignes_maximum (=1) : nombre de lignes maximum à afficher
              (bool) efface (=True) : effacer le texte originel
    Sortie : Affichage du texte dans les cadres
    """
    if efface:
        effacer_texte(point_mini, point_maxi)   # Effacer le texte du cadre
    emplacement = emplacement_texte(point_mini, point_maxi, padx, pady,
                                    alignement)   # Localisation de l'emplacement du texte
    turtle.up()
    turtle.goto(emplacement)   # Aller à la localisation de l'emplacement
    turtle.write(reduction_texte(texte, lignes_maximum), align=alignement,
                 font=(FONTNAME, size, FONTTYPE))   # Ecrire le texte dans les limites
                                                    # du cadre
            

def creer_dictionnaire_des_objets(fichier):
    """
    Création d'un dictionnaire à partir d'un fichier
    Entrée : (fichier) fichier : où est stockée l'information par ligne
             comme
             (11, 7), "indice4 = '(1, 2)'"            
    Sortie : (dict) dico_file : Dictionnaire des objets contenu dans
             fichier avec comme index un tuple et comme valeur un
             string
    """ 
    dico_file = {}   # Création d'un dictionnaire vide
    liste = []   # Création d'une liste vide
    with open(fichier, encoding='utf-8') as fichier_in:   # Ouverture du fichier
        for ligne in fichier_in.readlines():      # Décompose chaque ligne du fichier
            chaine = ligne.strip()                # en trois parties :
            chaine = chaine.removeprefix('(')     # Un entier représentant la ligne du château  
            chaine = chaine.replace(',','||', 1)  # Une chaîne de caractères
            chaine = chaine.replace('),','||', 1)
            liste.append(chaine.split('||'))   # Ajoute la chaîne de caractère à liste
            for i in liste:   # Création du dictionnaire à partir de la liste
                indice =eval(i[2])
                tuple = (eval(i[0]), eval(i[1]))
                dico_file[tuple] = indice   # Rentrer l'indice du jeu
                                            # dans le dictionnaire
    return dico_file


def action(annonce, matrice, case, mouvement, pas, possible=True):
    """
    Déplacement du personnage et affichage des annonces liées au déplacement
    Entrées : (str) annonce : message à afficher dans le cadre de l'annonce
              (matrice) matrice : représente le plan du château
              (tuple) case : où se trouve le personnage en pixel château    
              (tuple) mouvement :  demandé par le joueur
              (int) pas : pixel château du château
              (bool) possible (=True) : déplacement peut s'effectuer
              (bool) modification (=True) : modification de la matrice
    Sortie : Déplacement du personnage si possible et message dans la zone
             annonce
    """
    affichage_texte(annonce, PADX, PADY, ZONE_ANNONCES_MINI,
                    ZONE_ANNONCES_MAXI, SIZE_NORMAL,'center',
                    LIGNES_MAXIMUM_ANNONCE)    # Annonce de l'objet dans la zone annonce
                                               # dans la limite du cadre
    if possible:
        matrice[mouvement[0]][mouvement[1]] = 0   # Changement de la case objet en case couloir
        personnage(pas, case, mouvement)   # Déplacement du personnage
    else:
        personnage(pas, case, case) # Pas de déplacement du personnage

                                               
def ramassage_objet(case, mouvement, matrice, pas):
    """
    Mettre l'objet dans une liste sac_m et afficher l'objet ramassé dans
    le cadre de l'annonce et la liste des objets ramassés dans le cadre
    de l'inventaire
    Entrées : (matrice) matrice : représente le plan du château
              (tuple) mouvement :  demandé par le joueur
              (int) pas : pixel château du château
    Sortie : Déplacement du personnage, mise de l'objet dans le sac_m,
             Affichage d'un message dans la zone annonce et mise à jour
             de la zone inventaire
             Modification de la liste sac_m défini dans le code
             principal
    """
    dico_objet = creer_dictionnaire_des_objets(fichier_objets)   # Création
                                                                 # du dictionnaire des questions
    sac_m.append(affichage_paragraphe(dico_objet[mouvement],
                                      NB_MAXIMUM_INVENTAIRE))   # Ajouter l'objet au sac
    inventaire_cadre(matrice, pas)   # AAA Affichage dans l'inventaire des objets acquis
    action(affichage_paragraphe(f"Vous avez trouvé : {dico_objet[mouvement]}", NB_MAXIMUM_ANNONCE),
           matrice, case, mouvement, pas)   # BBB Annonce de l'objet dans la zone annonce
                                            # dans la limite du cadre et déplacement          


def poser_question(matrice, case, mouvement, pas):
    """
    Poser une question au joueur. Si la réponse est juste la porte
    s'ouvre et le personnage avance.
    Entrées : (matrice) matrice : représente le plan du château
              (tuple) case : où se trouve le personnage en pixel château
              (tuple) mouvement : demandé par le joueur
              (int) pas : pixel château du château
    Sortie : Déplacement du personnage si réponse juste
    """
    dico_question = creer_dictionnaire_des_objets(fichier_questions) # Dictionnaire des questions
    action('Cette porte est fermée.', matrice, case, mouvement, pas,
           possible=False) # Ne pas se déplacer devant la porte fermée
    reponse = turtle.textinput('Question',
                               dico_question[mouvement][0])   # Réponse du joueur à la question
    turtle.listen()   # Mettre le programme à l'écoute après l'interruption
    if reponse == dico_question[mouvement][1]:   # Réponse juste du joueur
        action('La porte est ouverte maintenant', matrice, case, mouvement,
               pas)   # Le personnage se déplace et affichage d'une annonce
    else:
        action('La réponse est mauvaise. La porte reste fermée.', matrice, case, mouvement, pas,
               possible=False) # Ne pas se déplacer devant la porte fermée


def deplacer(matrice, case, mouvement, pas):
    """
    Gestion des déplacements
    Entrées : (matrice) matrice : représente le plan du château
              (tuple) case : où se trouve le personnage en pixel château
              (tuple) mouvement : demandé par le joueur
              (int) pas : pixel château du château
    Sorties : si (1) mur rien ne se passe
              si (2) sortie du château
              si (3) répondre aux questions pour ouvrir la porte
              si (4) déplacement et prendre l'objet
              si (0) case vide, déplacement
    """
    if (mouvement[1] < len(matrice[0]) and mouvement[1] >= 0   # Le personnage reste dans le plan
        and mouvement[0] < len(matrice)  and  mouvement[0] >= 0):
        if matrice[mouvement[0]][mouvement[1]] == 4:   # Le personnage trouve un objet
            ramassage_objet(case, mouvement, matrice, pas)   # Rammassage de l'objet
        elif matrice[mouvement[0]][mouvement[1]] == 3:   # Le personnage veut ouvrir une porte
            poser_question(matrice, case,
                           mouvement, pas)   # Le joueur répond à une question pour ouvrir
                                             # la porte
        elif matrice[mouvement[0]][mouvement[1]] == 2:   # Le personnage arrive devant la sortie
            action('Bravo ! Vous avez gagné', matrice, case, mouvement,
                   pas)   # Déplacement et affichage d'une annonce
        elif matrice[mouvement[0]][mouvement[1]] != 1: # Le personnage est dans les couloirs
            personnage(pas, case, mouvement) # Le personnage se déplace

            
def afficher_plan(matrice):
    """
    Afficher le plan du château
    Entrée : (matrice) matrice : représente le plan du château avec des
             couleurs différentes pour : (0) vide, (1) mur, (2) sortie,
             (3) porte, (4) objet
    Sortie : Dessin du plan du château
    """
    for i in range(len(matrice)):
        for j in range(len(matrice[0])):
            tracer_case((i,j), COULEURS[matrice[i][j]],
                        calculer_pas(matrice))  # Tracer des carrés de couleur successifs
    

def personnage(pas, case, mouvement):
    """
    Définir le personnage, sa couleur, sa taille, sa case
    Entrées : (int) pas : la dimension du carré pixel château
              (tuple) case : où se trouve le personnage en pixel château
              (tuple) mouvement : demandé par le joueur             
    Sortie : Dessin du personnage
    """
    tracer_case(mouvement, COULEUR_CASES, pas)   # Effacer la trace d'objet ou de porte
    tracer_case(case, COULEUR_CASES, pas)    # Effacer la trace ancienne du personnage
    turtle.up()
    turtle.goto(coordonnees(mouvement,pas)[0]+pas//2,
                coordonnees(mouvement,pas)[1]+pas//2)   # Met le personnage au centre de la case
    turtle.down()
    turtle.dot(RATIO_PERSONNAGE * pas, COULEUR_PERSONNAGE)   # Trace le personnage
    turtle.up()
    turtle.goto(coordonnees(mouvement, pas))   # Déplacement du personnage vers la nouvelle case

    
def deplacer_bas():
    """
    Déplacement en bas du personnage
    Entrée : (event) touche Down pour déplacer le personnage
    Sortie : Déplacement en bas du personnage
    """
    global matrice_g, pas_g
    turtle.onkeypress(None, "Down")   # Désactive la touche bas
    case = coordonnees_inverse(turtle.position(), pas_g)
    deplacer(matrice_g, case, (case[0] + 1,
                               case[1]), pas_g)   # Déplacer le personnage d'une case en bas
    turtle.onkeypress(deplacer_bas, "Down")   # Réassocie la touche Down à la fonction deplacer_bas

    
def deplacer_haut():
    """
    Déplacement en haut du personnage
    Entrée : (event) touche Up pour déplacer le personnage
    Sortie : Déplacement en haut du personnage
    """
    global matrice_g, pas_g
    turtle.onkeypress(None, "Up")   # Désactive la touche haut
    case = coordonnees_inverse(turtle.position(), pas_g)
    deplacer(matrice_g, case, (case[0] - 1,
                               case[1]), pas_g)   # Déplacer le personnage d'une case en haut
    turtle.onkeypress(deplacer_haut, "Up")   # Réassocie la touche Up à la fonction deplacer_haut
    

def deplacer_droite():
    """
    Déplacement à droite du personnage
    Entrée : (event) touche Right pour déplacer le personnage
    Sortie : Déplacement à droite du personnage
    """
    global matrice_g, pas_g
    turtle.onkeypress(None, "Right")   # Désactive la touche Right
    case = coordonnees_inverse(turtle.position(), pas_g)
    deplacer(matrice_g, case, (case[0],
                               case[1] + 1), pas_g)   # Déplacer le personnage d'une case à droite
    turtle.onkeypress(deplacer_droite, "Right")   # Réassocie la touche Right
                                                  # à la fonction deplacer_droite

    
def deplacer_gauche():
    """
    Déplacement à gauche du personnage
    Entrée : (event) touche Left pour déplacer le personnage
    Sortie : Déplacement à gauche du personnage
    """
    global matrice_g, pas_g
    turtle.onkeypress(None, "Left")   # Désactive la touche Left
    case = coordonnees_inverse(turtle.position(), pas_g)
    deplacer(matrice_g, case, (case[0],
                               case[1] - 1), pas_g)   # Déplacer le personnage d'une case à gauche
    turtle.onkeypress(deplacer_gauche, "Left")   # Réassocie la touche Left
                                                 # à la fonction deplacer_gauche


def initialisation(case, matrice, pas):
    """
    Initialise la fenêtre du jeu, le plan du château, la position initiale du
    personnage.
    Entrées : (tuple) case : position en pixel château du personnage
              (matrice) matrice : plan du château
              (int) pas : 1 pixel château
    Sortie : Affichage du jeu dans la fenêtre turtle
    """
    turtle.up()   # Désactivation de l'action de dessiner
    turtle.speed(VITESSE_TURTLE)   # Vitesse de l'action de dessiner
    turtle.hideturtle()   # Rendre invisible turtle
    turtle.setup(width=DIMENSION, height=DIMENSION)   # Dimension de la fenêtre turtle
    turtle.bgcolor(COULEUR_EXTERIEUR)   # Couleur du fond de la fenêtre turtle
    turtle.title(TITRE)   # Titre de la fenêtre turtle
    inventaire_cadre(matrice, pas)   # Cadre inventaire
    tracer_rectangle(ZONE_ANNONCES_MINI, ZONE_ANNONCES_MAXI)   # Cadre d'annonces
    afficher_plan(matrice)   # Plan du château
    personnage(pas, case, case)   # Placer le personnage sur la case du départ

    
def calculer_pas(matrice):
    """
    Calcul du côté de la case du plan du château
    Entrée : (matrice) matrice : représente le plan du château
    Sortie : (int) dimension du côté de la case du plan du château
             exprimé en pixel turtle
    """
    return min((ZONE_PLAN_MAXI[0] - ZONE_PLAN_MINI[0])//len(matrice[0]),
               (ZONE_PLAN_MAXI[1] - ZONE_PLAN_MINI[1])//len(matrice[1]))
    

def lire_matrice(fichier):
    """
    Matrice du plan du château
    Entrée : (file utf-8) fichier : stockage persistant du plan du
             château
    Sortie : (matrice) matrice : représente le plan du château
    """
    matrice = []
    with open(fichier, encoding='utf-8') as fichier_in:
        return [[int(colonne) for colonne in ligne.split()]
                for ligne in fichier_in]


def quitter():
    """
    Appuyer sur la touche q pour quitter le jeu
    """
    turtle.bye()


# Code principal


matrice_g = lire_matrice(fichier_plan)   # Plan du château
pas_g = calculer_pas(matrice_g)   # Dimension du carré appelé Pixel Château
case_m = POSITION_DEPART   # Position de départ du personnage
sac_m = []   # Création du sac vide d'objets
             # qui sera rempli par ramassage_objet(mouvement, matrice, pas)
             # Cette liste sera modifiée par les fonctions

initialisation(case_m, matrice_g, pas_g)   # Initialise la fenêtre du jeu avant toute action

turtle.onkeypress(deplacer_gauche, "Left")   # Associe à la touche Left à deplacer_gauche
turtle.onkeypress(deplacer_droite, "Right")   # Associe à la touche Right à deplacer_droite  
turtle.onkeypress(deplacer_haut, "Up")   # Associe à la touche Up à deplacer_haut
turtle.onkeypress(deplacer_bas, "Down")   # Associe à la touche Down à deplacer_bas
turtle.onkeypress(quitter, "q")    # Associe à la touche q à quitter le jeu
turtle.listen()   # Place le code à l'écoute des actions du joueur
turtle.mainloop()   # Place le programme en attente d’une action du joueur


