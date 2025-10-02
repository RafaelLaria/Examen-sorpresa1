class Rectangulo:
    def __init__(self, p1=None, p2=None):
        # Si no se pasan puntos, ambos serán el origen
        if p1 is None:
            p1 = Punto()
        if p2 is None:
            p2 = Punto()
        self.p1 = p1
        self.p2 = p2

    def base(self):
        return abs(self.p2.x - self.p1.x)

    def altura(self):
        return abs(self.p2.y - self.p1.y)

    def area(self):
        return self.base() * self.altura()

    def __str__(self):
        return f"Rectángulo con vértices {self.p1} y {self.p2}"
