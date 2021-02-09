class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def semelhantes(self, triangulo):
        lados1 = [self.a, self.b, self.c]
        lados2 = [triangulo.a, triangulo.b, triangulo.c]
        lados1.sort()
        lados2.sort()
        if (lados1[0]/lados2[0]) == (lados1[1]/lados2[1]) == (lados1[2]/lados2[2]):
            return True
        else:
            return False

