from Vector import Punto
from Rectangulo import Rectangulo
import math




#1
A=Punto(2,3)
B=Punto(5,5)
C=Punto(-3,-1)
D=Punto()
print(f"{A}\n{B}\n{C}\n{D}\n")


#2
print(f"{A.cuadrante()} {C.cuadrante()} {D.cuadrante()}")

#3
print(f"{A.vector(B)} {B.vector(A)}")

#4
print(f"{A.distancia(B)} {B.distancia(A)}")

#5
distanciaDorigenA = A.distancia(Punto(0,0))
distanciaDorigenB = B.distancia(Punto(0,0))
distanciaDorigenC = C.distancia(Punto(0,0))

print(f"El mas lejos de el origen es: {max(distanciaDorigenA,distanciaDorigenB,distanciaDorigenC)}")

#6
R=Rectangulo(A,B)

#7
print(f"Base: {R.base()}")
print(f"Altura: {R.altura()}") 
print(f"Area: {R.area()}")




