import math

class silnia:
    def __init__(self, N):
        self.N = N

    def get_silnia(self):
        i = 1
        if self.N == 0:
            return 1
        else:
            while self.N > 0:
                i = i * self.N
                self.N = self.N-1
            return i
