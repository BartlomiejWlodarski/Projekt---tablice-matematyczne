class ciagG:
    def __init__(self, a1, q, n):
        self.a1 = a1
        self.q = q
        self.n = n

    def get_wynik(self):
        return self.a1 * (1 - (self.q ** self.n)) / (1 - self.q)