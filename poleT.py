import math
import matplotlib
import matplotlib.pyplot as plt

class poleT:
    def __init__(self, XA, XB, XC, YA, YB, YC):
        self.XA = XA
        self.XB = XB
        self.XC = XC
        self.YA = YA
        self.YB = YB
        self.YC = YC

    def get_pole(self):
        return 0.5 * math.fabs((self.XB-self.XA)*(self.YC-self.YA) - (self.YB-self.YA)*(self.XC-self.XA))

    def rysuj_trojkat(self):
        plt.grid()
        plt.plot([self.XA, self.XB, self.XC, self.XA], [self.YA, self.YB, self.YC, self.YA])
        plt.show()