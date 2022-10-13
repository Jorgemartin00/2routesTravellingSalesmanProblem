
import matplotlib.pyplot as plt
from itertools import permutations, combinations
from math import floor
from re import sub
from auxFunctions import *




# traveling Salesman Problem
def travellingSalesmanProblem(graph, s, V):
 
    vertex = []
    for i in range(V):
        if i != s:
            vertex.append(i)

 
    # calculate Hamiltonian Cycles
    min_path = 1000000000
    minPermutation=["error"]
    next_permutation=permutations(vertex)
    for i in next_permutation:
 
        # store current Path weight(cost)
        current_pathweight = 0
 
        # compute current path weight
        k = s
        for j in i:
            #print(k, j)
            current_pathweight += graph[k][j]
            k = j
        current_pathweight += graph[k][s]
        # update minimum
        if min_path==current_pathweight:
            minPermutation.append(i)
        if current_pathweight<min_path:
            minPermutation=[]
            min_path = min(min_path, current_pathweight)
            minPermutation.append(i)
    
    solutionPermutation=[]
    for perm in minPermutation:
        perm=list(perm)
        perm.insert(0, s)
        solutionPermutation.append(perm)
         
    return min_path, solutionPermutation

def findOptimalRute(graph, s, V):
    optimalRutes=[]
    auxiliarList=graph[:]
    origin=graph[s]

    vertex = []
    for i in range(V):
        if i != s:
            vertex.append(i)

    #USING 1 TRANSPORT
    minimumCost0, minimumPaths0=(travellingSalesmanProblem(graph, s, V))
    optimalRutes.append([minimumCost0, minimumPaths0])

    #USING 2 TRANSPORTS-> SUB1 AND SUB2

    #set the maximum number of vertex per rute
    maxNVertex=V-1
    if maxNVertex%2==0:
        topn2=floor(maxNVertex/2)
    else:
        topn2=floor(maxNVertex/2)+1 


    for nSub2 in range(1, topn2):
        costs=[]
        bestRutes=[]
        for comb in combinations(vertex, maxNVertex-nSub2):
            vertexNotIncluded=[]
            for n in range(V):
                if n not in comb:
                    vertexNotIncluded.append(n)
            #print("vertex not included in comb ", vertexNotIncluded)

            auxiliarList=graph[:]
            
            comb=list(comb)
            comb.insert(s, s)
            sub1=[]
            for i in comb:
                sub1.append([auxiliarList[i][v] for v in comb])
        

            

            sub2=[]
            for vNo in vertexNotIncluded:
                sub2.append([auxiliarList[vNo][v] for v in vertexNotIncluded])
            

            #print(sub1, sub2)
            minimumCost1, minimumPermutaion1= travellingSalesmanProblem(sub1, s, V=len(sub1))
            minimumPaths1=[comb[a] for a in minimumPermutaion1[0]]

            minimumCost2, minimumPermutaion2= travellingSalesmanProblem(sub2, 0, V=len(sub2))
            minimumPaths2=[vertexNotIncluded[a] for a in minimumPermutaion2[0]]
            
            totalCost=minimumCost1+minimumCost2 #aqui se podrian incluir costes fijos (por autobus) y costes variables, los de la ruta
            costs.append(totalCost)
            bestRutes.append([minimumPaths1, minimumPaths2])
        
        minCost=min(costs) #SOLO RETURNEA UNO, PERO PUEDE HABER OPTIMO MULTIPLE
        bestRute=bestRutes[costs.index(minCost)]
        optimalRutes.append([minCost, bestRute])

    minGlobal=500000000
    index=0
    for i in range(len(optimalRutes)):
        minGlobal=min(optimalRutes[i][0], minGlobal)
        if minGlobal==optimalRutes[i][0]:
            index=i
    return(optimalRutes[index][0], optimalRutes[index][1])


 
# Driver Code
if __name__ == "__main__":
    V = 6
 
    # matrix representation of graph
    graph = [[0,    100,    100000,   200,    600,    200   ],      #vertex 0
            [100,   0,      200,    600,    500,    100000  ],    #vertex 1
            [100000,  200,    0,      1100,   1600,   100000],     #vertex 2
            [200,   600,    1100,   0,      1500,   100000  ],     #vertex 3
            [600,   500,    1600,   1500,   0,      1500    ],      #vertex 4
            [200,   100000,   100000,   100000,   1500,   0 ]]            #vertex 5
    
    cords=[ [0,0],      #madrid
            [2,2],      #zgz
            [1,3],      #bilbao 
            [-1,1],     #valladolid
            [3, 0],     #valencia
            [-1, -2]]   #sevilla
    
   

    
    s = 0
    for i in range(V):
        
        minCost, minRutes=findOptimalRute(graph, s, V)
        print(minCost, minRutes)
        #print(minRutes[1][0])

        
        
        fig, ax = plt.subplots()

        printGraph(cords, ax )
        printGraph([cords[n] for n in minRutes[0]], ax, optimal=True, color="b")
        printGraph([cords[n] for n in minRutes[1]], ax, optimal=True, color="r")
        ax.plot(cords[0][0], cords[0][1], marker="o", c="g", markersize=10)
        fig.show() 
        plt.show()
        graph=rotateGraphOrigin(graph)
        cords=rotateCoords(cords)
    


