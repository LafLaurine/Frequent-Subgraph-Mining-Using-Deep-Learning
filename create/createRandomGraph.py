# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 16:35:40 2020

@author: YuJeong
"""
import os 
import random
from pathlib import Path

def readRepresentGraph():
    path = str(Path(__file__).parent.parent) 
    files = path + '\\datasets\\structure_fsm\\rep2.txt'
    print(files)  
    adMatrix = []
    with open(files, 'r') as f:
        for line in f:     
            l = []
            for num in line.split(' '):
                if num.isdigit(): 
                    l.append(int(num))
            adMatrix.append(l)
    
    return adMatrix
    #inp = np.loadtxt(files, dtype='i', delimiter=' ')
    #print(inp)

class Graph(object):

    # Initialize the matrix
    def __init__(self, size, index):
        self.adjMatrix = []
        self.index = index
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
        self.size = size

    # Add edges
    def add_edge(self, v1, v2, weight):
        if v1 == v2:
            print("Same vertex %d and %d" % (v1, v2))
        self.adjMatrix[v1][v2] = weight
        self.adjMatrix[v2][v1] = weight

    # Remove edges
    def remove_edge(self, v1, v2):
        if self.adjMatrix[v1][v2] == 0:
            print("No edge between %d and %d" % (v1, v2))
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0

    def __len__(self):
        return self.size

    def writeFile(self):
        ind = '0 '
        ind0 = '0 '
        for i in range(self.size):
            ind = ind + chr(ord('A') + i) + ' '
            ind0 = ind0 + '0 '
        
        filename = "\\datasets\\structure_fsm\\random" + "\\2graph" + str(self.index) + '.txt'
        path =  str(Path(__file__).parent.parent) + filename
     
        f = open(path, 'w')
        for row in self.adjMatrix:
            line = ''
            for val in row:
                line = line + str(val) + ' '
            f.write(line+'\n')
        f.close()
        #f.write()


def createRandomGraph(rangeN):
    for i in range(100):
        if rangeN == 1:     # weight range 0-10
            #sumVal = random.randint(0, 5)
            sumVal = 0
        elif rangeN == 2:    # weight range 30-50
            sumVal = random.randint(30, 50)
        elif rangeN == 3:    # weight range 80-100
            sumVal = random.randint(80, 100)
        randG = Graph(len(originMat), i)
        randEdge = random.randint(0, len(originMat))
        for row in range(len(originMat)):
            for val in range(row):
                if originMat[row][val] != 0:
                    #randG.add_edge(row, val, sumVal+round(originMat[row][val]*random.uniform(0, 1), 3))
                    randG.add_edge(row, val, round((originMat[row][val]+random.uniform(0, 1)), 4))
        #        if val == randEdge:
        #            break
        randG.writeFile()

        
if __name__ == "__main__":
    originMat = readRepresentGraph()    
    rangeN = int(input("Random value range(1: 0-10, 2: 30-50, 3: 80-100): "))
    createRandomGraph(rangeN) 

    
    
    
    
    
    
    
    
    