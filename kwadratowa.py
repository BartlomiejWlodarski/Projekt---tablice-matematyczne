import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import math

class kwadratowa:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    def get_delta(self):
        return (self.b * self.b) - (4 * self.a * self.c)

    def get_x1(self):
        return (-self.b + math.sqrt((self.b * self.b) - (4 * self.a * self.c))) / (2 * self.a)

    def get_x2(self):
        return (-self.b - math.sqrt((self.b * self.b) - (4 * self.a * self.c))) / (2 * self.a)

    def get_p(self):
        return -self.b/(2 * self.a)

    def get_q(self):
        return -((self.b * self.b) - (4 * self.a * self.c)) / (4 * self.a)

    def rysuj_wykres(self):
        p = -self.b/(2 * self.a)
        x = np.linspace(p-10,p+10,1000)
        y = ((x**2) * self.a) + (x * self.b) + self.c 
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.spines['left'].set_position('center')
        ax.spines['bottom'].set_position('zero')
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')
        plt.grid()
        plt.plot(x,y, 'r')
        plt.show()
