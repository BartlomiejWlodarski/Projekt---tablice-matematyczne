class ciagA:
    def __init__(self, a1, r, n):
        self.a1 = a1
        self.r = r
        self.n = n

    def get_wynik(self):
        return 0.5 * self.n * (2 * self.a1 + self.r * (self.n - 1))