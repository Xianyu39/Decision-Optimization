import numpy as np
import random as rd
import matplotlib.pyplot as pl


class solution(np.ndarray):
    pass

# Check whether the mt is in the collection.
def isIn(mt:np.ndarray, ls:list)->bool:
    r = mt.shape[0]
    c = mt.shape[1]
    for each in ls:
        equal = True
        for i in range(r):
            for j in range(c):
                if mt[i,j] != each[i,j]:
                    equal=False
                    break
            else:
                continue
            break
        if equal:
            return True

        
    return False


class TS:
    """Get solution through here."""

    def __init__(self, lands:tuple, plants:tuple, production:np.ndarray, tabuLength:int) -> None:
        self.plants = plants
        self.lands = lands
        self.rows = len(plants)
        self.cols = len(lands)
        self.production = production
        self.optSolution = solution((self.rows, self.cols))

        self.tabuLength = tabuLength
        self.tabuList = list()

        # Visualize
        self.axesX = []
        self.axesY = []


    def isValid(self, x:solution)->bool:
        UsingLands=[0 for item in self.lands]
        PlantingPlants=[0 for item in self.plants]

        for i in range(self.rows):
            for j in range(self.cols):
                UsingLands[j] += x[i,j]
                PlantingPlants[i] += x[i,j]
                if x[i,j] < 0:
                    return False

        for i in range(self.cols):
            if UsingLands[i] > self.lands[i]:
                return False

        for i in range(self.rows):
            if PlantingPlants[i] > self.plants[i]:
                return False

        return True
        

    def adjacentSolution(self, x:solution)->list:
        adjSolutionSet = []
        rowChange = np.array(x[0, :])

        i = 0
        while i < self.rows:
            # Generate a vector of random numbers.
            for j in range(self.cols):
                rowChange[j] = rd.randint(-1, 1)

            tmp = np.array(x)
            tmp[i] += rowChange

            # Check whether it is valid and filter the invalid solutions.
            if self.isValid(tmp):
                adjSolutionSet.append(tmp)
                i += 1

        return adjSolutionSet


    def grade(self, x:solution)->int:
        sum = 0
        for i in range(self.rows):
            for j in range(self.cols):
                sum += x[i,j] * self.production[i, j]

        return sum


    def getOptimalSolution(self, origin: solution, iter_times:int)->solution:
        slt = np.array(origin)
        for k in range(iter_times):
            # print(len(self.tabuList), end=' ')
            adj = self.adjacentSolution(slt)
            adj.sort(key=lambda a:self.grade(a), reverse=True)

            # Choose the best one which is not in tabu list.
            for item in adj:
                if not isIn(item, self.tabuList):
                    # The optimal solution of each iteration. 
                    slt = item
                    self.optSolution = slt

                    self.axesX.append( k + 1 )
                    self.axesY.append(self.grade(slt))

                    while len(self.tabuList) >= self.tabuLength:
                        self.tabuList.pop(0)
                        
                    self.tabuList.append(item)

                    break

        # Find the best in tabu list.
        bst = np.zeros(slt.shape)
        for i in self.tabuList:
            # print(self.grade(i))
            if self.grade(bst) < self.grade(i):
                bst = i
        return bst

    def showChart(self):
        pl.plot(self.axesX, self.axesY, color='orange')
        pl.title("The Production-Iteration Chart")
        pl.xlabel("Iteration")
        pl.ylabel("Production")
        pl.show()