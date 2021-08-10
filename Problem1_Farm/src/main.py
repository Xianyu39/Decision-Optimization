import numpy as np
import search as sc

plants = ('wheat','corn','vegetable','friut')

prod = np.array([[500,550,630,1000,800,700],
                 [800,700,600,950,90,930],
                 [1200,1040,980,860,880,780],
                 [1000,960,840,650,600,700]])

ts = sc.TS((42,56,44,39,60,59),(76,88,40,96),prod)
ini = np.zeros((4,6))
ts.adjacentSolution(ini)