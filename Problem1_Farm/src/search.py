import numpy as np
import random as rd

class solution(np.ndarray):
    pass

class TS:
    """Get solution through here."""

    def __init__(self, lands:tuple, plants:tuple, production:np.ndarray) -> None:
        self.plants = plants
        self.lands = lands
        self.rows = len(plants)
        self.cols = len(lands)
        self.production = production

        self.tabuLength = 10
        self.tabuList = list()
        

    def adjacentSolution(self, x:solution)->tuple:
        adjSolutionSet = []
        rowChange = np.array(x[0, :])

        for i in range(self.rows):

            for j in range(self.cols):
                rowChange[j] = rd.randint(-1, 1)

            tmp = np.array(x)
            tmp[i] += rowChange
            adjSolutionSet.append(tmp)

        # Check whether these solutions are valid.

        return tuple(adjSolutionSet)




    def grade(self, x:solution)->int:
        sum = 0
        for i in range(self.rows):
            for j in range(self.cols):
                sum += x[i,j] * self.production[i, j]

        return sum


    def isValid(self, x:solution)->bool:
        UsingLands=[0 for item in self.lands]
        PlantingPlants=[0 for item in self.plants]

        for i in range(self.rows):
            for j in range(self.cols):
                UsingLands[j] += x[i,j]
                PlantingPlants[i] += x[i,j]

        for i in range(self.cols):
            if UsingLands[i] > self.lands[i]:
                return False

        for i in range(self.rows):
            if PlantingPlants[i] > self.plants[i]:
                return False

        return True
