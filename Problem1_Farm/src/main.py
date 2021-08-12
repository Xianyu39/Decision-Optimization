import numpy as np
import search as sc
import matplotlib.pyplot as plt

prod = np.array([[500,550,630,1000,800,700],
                 [800,700,600,950,90,930],
                 [1200,1040,980,860,880,780],
                 [1000,960,840,650,600,700]])
lands = (42,56,44,39,60,59)
plants = (76,88,40,96)
lenList = (10,60,110,160,210,260)
iterations = 2000 # 2k might be the optimal value of iterations.

ini = np.ones((4,6))
opt = np.zeros((4,6))
ag = None

fig, ax=plt.subplots()

print('Calculating...')
for l in lenList:
    ag = sc.TS(lands, plants, prod, l)
    ag.getOptimalSolution(ini, iterations)
    if ag.grade(opt) < ag.grade(ag.optSolution):
        opt = ag.optSolution

    ax.plot(ag.axesX, ag.axesY, label='Tabu list length = '+str(l))

ax.set_title('Production-Iteration Chart')
ax.set_xlabel('Iteration')
ax.set_ylabel('Production')
ax.legend()
ax.grid(axis='both')

print('Calculation done!')

print('The optimal solution is: ')
for i in range(opt.shape[0]):
    for j in range(opt.shape[1]):
        print('%8.0f'%opt[i,j], end=' ')
    else:
        print()
print('The production is {pd}'.format(pd=ag.grade(opt)))

plt.show()