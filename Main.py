from Geometría.py import Punto, Rectangulo

# Crear puntos
A = Punto(2, 3)
B = Punto(5, 5)

print("Punto A:", A)
print("Punto B:", B)
print("Cuadrante de A:", A.cuadrante())

# Vector AB
print("Vector AB:", A.vector(B))

# Distancia A-B
print("Distancia A-B:", A.distancia(B))

# Crear rectángulo con A y B
rect = Rectangulo(A, B)
print(rect)
print("Base:", rect.base())
print("Altura:", rect.altura())
print("Área:", rect.area())
