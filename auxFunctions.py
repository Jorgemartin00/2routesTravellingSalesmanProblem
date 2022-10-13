from itertools import permutations, combinations

def rotateCoords(coords):
    listpop=coords.pop(0)
    coords.insert(len(coords), listpop)
    return(coords)

def rotateGraphOrigin(graph):
    V=len(graph)

    #THIS FUNCTION TAKES THE PREVIOUS ORIGIN, LOCATED AT VERTEX 0, AND PLACES IT AT THE END OF THE GRAPH.
    #IT ALSO REASSIGN THE COSTS TO ITS RESPECTIVES RUTES
    listpop=graph.pop(0)
    graph.insert(len(graph), listpop)
    newgraph=[]
    #print(graph)
    for vertex in graph:
        auxlist=vertex[:]
        changeInt=auxlist.pop(0)
        #print(changeInt)
        auxlist.insert(len(auxlist), changeInt)
        newgraph.append(auxlist)
    return(newgraph)
    

def getLines(coords):
    v=len(coords)
    combs=combinations([a for a in range(v)], 2)
    lines=[]
    for comb in combs:
        comb=list(comb)
        coord1=coords[comb[0]]
        coord2=coords[comb[1]]

        x=[coord1[0], coord2[0]]
        y=[coord1[1], coord2[1]]

        lines.append([x, y])

    return(lines)

def getLinesOpt(coords):
    v=len(coords)
    auxCoords=coords[:]
    auxCoords.append(coords[0])

    lines=[]

    for i in range(v):
        coord1=auxCoords[i]
        
        coord2=auxCoords[i+1]

        x=[coord1[0], coord2[0]]
        y=[coord1[1], coord2[1]]
        lines.append([x, y])
    return(lines)




def printGraph(coords, ax, color="k", optimal=False):
    
    if optimal==False:
        marker="o"
        color="k"
        ls="--"
    else:
        marker="^"
        ls="-"

    if optimal==False:
        for point in coords:
            ax.scatter(point[0], point[1],  color=color, marker=marker)

    if optimal==False:
        lines=getLines(coords)
    else:
        lines=getLinesOpt(coords)

    
    for line in lines:
        ax.plot(line[0], line[1], color=color, ls=ls, linewidth=3)

    return(0)