import math
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

class logarytm:
    def __init__(self, liczba, podst):
        self.liczba = liczba
        self.podst = podst

    def get_wynik(self):
        return math.log(self.liczba, self.podst)

    def rysuj_wykres_liczba(self):
        x = np.linspace(1.5,(self.liczba)**3,1000)
        y = [math.log(self.liczba, i) for i in x]
        plt.grid()
        plt.plot(x,y)
        plt.show()

    def rysuj_wykres_podstawa(self):
        x = np.linspace(1,(self.podst)**3,1000)
        y = [math.log(i, self.podst) for i in x]
        plt.grid()
        plt.plot(x,y)
        plt.show()