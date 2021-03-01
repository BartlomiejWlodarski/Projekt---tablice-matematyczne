import math

class ciagZ:
    def __init__(self, a1, q):
        self.a1 = a1
        self.q = q
        
    def get_wynik(self):
        return self.a1 / (1 - self.q)