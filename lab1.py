# Importer la bibliothèque math
import math

def add(x,y):
    "" "Simple function return the sum of the arguments" ""
    return x+y
def multiply(x,y):
    "" "Simple function return the product of the arguments" ""
    return x*y
def diff(x,y):
    "" "Simple function return the difference of the arguments" ""
    return x-y
# result = add(3,7)
# print(result)
# print(add.__name__)
# print(add.__doc__)

def calc_distance(point1, point2):
    # Décomposer les points en leurs coordonnées x, y et z
    x1, y1, z1 = point1
    x2, y2, z2 = point2

    # Calculer la différence de coordonnées
    dx = x2 - x1
    dy = y2 - y1
    dz = z2 - z1

    # Calculer la distance euclidienne
    distance = math.sqrt(dx ** 2 + dy ** 2 + dz ** 2)

    # Retourner la distance
    return distance


def my_map(func,arg1,arg2):
    #input arg1 annd arg2
    """
    this will return
    """
    res = [] #output
    for i,j in zip(arg1,arg2):
        res.append(func(i,j))
    return res
a = [1,2,3,4,5]
b = [6,7,8,9,10]

# Définir deux listes de points 3D
points1 = [(1.0, 1.0, 1.0), (2.0, 2.0, 2.0), (3.0, 3.0, 3.0)]
points2 = [(4.0, 4.0, 4.0), (5.0, 5.0, 5.0), (6.0, 6.0, 6.0)]
# Appliquer la fonction calc_distance à chaque paire de points dans les listes points1 et points2
distances = my_map(calc_distance, points1, points2)

# Afficher les distances calculées
print(distances)

