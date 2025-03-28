import math
class Punto():
#None no funciona
    def __init__(self, x, y):
        self.x = x
        self.y = y
        if x is None and y is None:
            x = 0
            y = 0
    
    def __str__(self):
        return f'({self.x}, {self.y})'
    
    def cuadrante(self):
        if self.x > 0 and self.y > 0:
            return 'Cuadrante 1'
        elif self.x < 0 and self.y > 0:
            return 'Cuadrante 2'
        elif self.x < 0 and self.y < 0:
            return 'Cuadrante 3'
        elif self.x > 0 and self.y < 0:
            return 'Cuadrante 4'
        elif self.x == 0 and self.y == 0:
            return 'Origen'
    
    def vector(self,punto):
        return (punto.x - self.x, punto.y - self.y)
        
    def distancia(self,punto):
        math.sqrt((self.x - punto.x)**2 + (self.y - punto.y)**2)