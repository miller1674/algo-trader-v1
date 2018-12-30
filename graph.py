

import matplotlib.pyplot as plt

import numpy as np

class Graph:
    def __init__(self):
        print("graph is ready")
    
    def draw_graph(self, y):
    
        x = np.linspace(0, 2, 100)
        p=range(1,len(y)+1)
        plt.plot(p, y)

        plt.xlabel('x label')
        plt.ylabel('y label')

        plt.title("Simple Plot")

        plt.legend()

        plt.show()