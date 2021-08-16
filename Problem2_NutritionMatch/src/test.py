"""
This file has no use for solving the question, it was used to test or prove some features of Python.
"""

from os import system
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(8,6), dpi= 60)
x = np.linspace(0,10,1000)

plt.ion()
for k in range(20):
    # plt.cla()
    plt.plot(x, k*x, label='k='+str(k))
    plt.legend()
    plt.draw()
    plt.pause(0.2)

plt.ioff()
plt.show()
