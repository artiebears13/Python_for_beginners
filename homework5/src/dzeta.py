from mpmath import *
import matplotlib.pyplot as plt
import random


def dzeta_f(n):
    for i in range(1, n + 1):
        print (i, zetazero(i))
        yield i, zetazero(i)

def main():
    s = random.randint(4, 30)

    a=dzeta_f(s)
    fig=plt.figure()
    ax=plt.axes()
    for i in a:
        ax.plot(i[0],i[1].imag,'-^')

    plt.show()
