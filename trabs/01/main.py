# -*- coding: utf-8 -*-

def pathR(grafo, v, lvl, t, depth=0):
    depth += 1
    t[0] += 1
    lvl[v] = t[0]

    if grafo[v] is None: return # don't have neighbours

    for w in range(len(grafo)):
        if grafo[v][w] == 1:
            whitespaces = " " * 2 * depth
            
            if lvl[w] == -1:
                print("{}{}-{} pathR(G,{})".format(whitespaces, v, w, w))
                pathR(grafo, w, lvl, t, depth)

            else:
                print("{}{}-{}".format(whitespaces, v, w))
    


N = int(input())
for x in range(N):
    V, E = map(int, input().split())
    grafo = [None for j in range(V)]
    t = [0]
    for y in range(E):
        a,b = map(int, input().split())
        if grafo[a] is None: grafo[a] = [0 for i in range(V)]
        grafo[a][b] = 1
    
    print("Caso {}:".format(x+1))
    lvl = [-1 for x in range(len(grafo))]
    pathR(grafo, 0, lvl, t)

    for v in range(len(lvl)):
        if lvl[v] == -1 and grafo[v] is not None:
            print()
            val = pathR(grafo, v, lvl, t)

    print()
        
        