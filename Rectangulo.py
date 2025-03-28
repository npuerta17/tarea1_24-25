from Vector import Punto
import math

class Rectangulo(Punto):
    def __init__(self,inicio,final):
        self.inicio = inicio
        self.final = final
        if inicio is None or final is None:
            inicio = 0
            final = 0
    def  base(self):
        return abs(self.final.x - self.inicio.x)
    def altura(self):
        return abs(self.final.y - self.inicio.y)
    def area(self):
        return self.base() * self.altura()

