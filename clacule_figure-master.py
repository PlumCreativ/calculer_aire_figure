import math

class deuxieme_D:

    def __init__(self, base, hauteur, rayon, longeur, largeur):
        self.base = base
        self.hauteur = hauteur
        self.rayon = rayon
        self.longeur = longeur
        self.largeur = largeur

    def triangle(base, hauteur):
        aire_triangle = (base * hauteur)/2
        return aire_triangle

    def rectangle(longeur, largeur):
        aire_rectangle = longeur * largeur
        return aire_rectangle

    def cercle_aire(rayon):
        aire_cercle = math.pi * rayon**2
        return aire_cercle

    def cercle_perimetre(rayon):
        perimetre_cercle = 2 * math.pi * rayon
        return perimetre_cercle

class troixieme_D:

    def __init__(self, aire_base_pyramide, rayon, base, hauteur, longeur, largeur):
        self.aire_base_pyramide = aire_base_pyramide
        self.rayon = rayon
        self.base = base
        self.hauteur = hauteur
        self.longeur = longeur
        self.largeur = largeur

    def prisme_droit(base, hauteur_v, hauteur):
        volum_prisme = ((base * hauteur_v)/2) * hauteur
        return volum_prisme

    def cylindre(rayon, hauteur):
        volum_cylindre = (math.pi * rayon**2) * hauteur
        return volum_cylindre

    def pyramide(aire_base_pyramide, hauteur):
        volum_pyramide = (aire_base_pyramide* hauteur)/3
        return volum_pyramide

    def cone(rayon, hauteur):
        volum_cone = ((math.pi * rayon**2) * hauteur)/3
        return volum_cone

    def spher(rayon):
        volum_spher = 4/3 * math.pi * rayon**2
        return volum_spher

    def parallelepiped_rectangle(hauteur, longeur, largeur):
        volum_parallelepiped = hauteur * longeur * largeur
        return volum_parallelepiped

def new_func():

    print('Rentrer le mode: 2D ou 3D ?')
    get = input('Choisisez entre deux modes:')
# while: get = int() posé des questions
    def partie_3D(choos_y):

        if choos_y == 'Sphère' or choos_y == 'sphère':
            rayon = float(input("Rentrer le rayon: "))
            print("Le volume de la sphère est", troixieme_D.spher(rayon))

        elif choos_y == 'Prisme droit' or choos_y == 'prisme droit':
            base = float(input('Rentrer la base du triangle: '))
            hauteur_v = float(input('Rentrer la hauteur du triangle: '))
            hauteur = float(input('Rentrer la hauteur du prisme droit: '))
            print("Le volume de prisme droit est", troixieme_D.prisme_droit(base, hauteur_v, hauteur))

        elif choos_y == 'Cylindre' or choos_y == 'cylindre':
            rayon = float(input("Rentrer le rayon: "))
            hauteur = float(input('Rentrer la hauteur: '))
            print("Le volume du cylindre est", troixieme_D.cylindre(rayon, hauteur))

        elif choos_y == 'Pyramide' or choos_y == 'pyramide':
            aire_base_pyramide = float(input('Rentrer la base de pyramide pour continué:'))
            hauteur = float(input('Rentrer la hauteur: '))
            print("Le volume de la pyramide est", troixieme_D.pyramide(aire_base_pyramide, hauteur))

        elif choos_y == 'Cône' or choos_y == 'cône':
            rayon = float(input("Rentrer le rayon: "))
            hauteur = float(input('Rentrer la hauteur: '))
            print("Le volume du cône est", troixieme_D.cone(rayon, hauteur))            

        elif choos_y == 'Parallélépipède' or choos_y == 'parallélépipède':
            longeur = float(input('Rentrer la longeur: '))
            largeur = float(input('Rentrer la longeur: '))
            hauteur = float(input('Rentrer la hauteur: '))
            print("La volume de parallélépipède est", troixieme_D.parallelepiped_rectangle(hauteur, largeur, longeur))

        else:
            print('Rentrer sphère, prisme droit, cylindre, pyramide ou parallélépipède !')
            print(new_func)

    def partie_2D(choos_x):
    # l'Etape premier: demandé à l'utilisateur de choisir le mode.
        if choos_x == 'cercle' or choos_x == 'Cercle':
            rayon = float(input("Rentrer le rayon: "))
            print("L'aire du cercle est de", math.floor(deuxieme_D.cercle_aire(rayon)), "et son périmètre est égal à", math.floor(deuxieme_D.cercle_perimetre(rayon)))

        elif choos_x == 'triangle' or choos_x == 'Triangle':
            base = float(input('Rentrer la base: '))
            hauteur = float(input('Rentrer la hauteur: '))
            print("L'aire du triangle est de", math.floor(deuxieme_D.triangle(base, hauteur)))

        elif choos_x == 'rectangle' or choos_x == 'Rectangle':
            longeur = float(input('Rentrer la longeur: '))
            largeur = float(input('Rentrer la longeur: '))
            print("L'aire du rectangle est de", math.floor(deuxieme_D.rectangle(longeur, largeur)))

        else:
            print('Rentrer triangle, rectangle ou cercle !')
            print(new_func)

    if get == '3D' or get == '3d':
        choos_y = str(input("Choisissez maintenant la figure, entre les figures suivantes: Sphère; Prisme droit; Cylindre, Cône, Pyramide ou Parallélépipède? : "))

        partie_3D(choos_y)
        # Le troisième étape pour calculé la volume, en reprenant les formules de l'aire pour ne pas se répéter, très déconseilé dans la programmation pour tenire le code visible !

    elif get == '2D' or get == '2d':
        choos_x = str(input("Choisissez maintenant la figure, entre: Cercle; Triangle; Rectangle, uniqument pour l'aire? : "))

        partie_2D(choos_x)
        # Deuxièmz étape consiste d'acompagner le choix.

    else:
        if get =='' or get == ' ':
            print("Rentrer l'une des deux possibilité ")
            print(new_func)

# else: print('Rentrer les nombres pour continué')

new_func()

