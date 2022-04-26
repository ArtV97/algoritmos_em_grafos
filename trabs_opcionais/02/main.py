def foo(graph, v, t, pe, ps, back, father, dst, bridges_stack):
    t[0] += 1
    pe[v] = t[0]
    back[v] = t[0]

    if v == dst:
        return True

    for w in graph[v]:
        #if pe[w] == 0:
        if w not in pe:
            father[w] = v
            result = foo(graph, w, t, pe, ps, back, father, dst, bridges_stack)

            back[v] = min(back[v], back[w])

            if back[w] > pe[v]:
                bridges_stack.append((v,w))
            
            if result:
                return True

        #elif ps[w] == 0 and w != father[v]:
        elif w not in ps and v in father and w != father[v]:
            back[v] = min(back[v], pe[w])
    
    t[0] += 1
    ps[v] = t[0]




# R = número de salas do labirinto (vertices)
# C = o número de corredores (arestas)
# Q = número de consultas
R, C, Q = map(int, input().split())

while R != 0 and C != 0 and Q != 0:
    graph = [[] for x in range(R)]

    for x in range(C):
        a, b = map(lambda val: int(val)-1, input().split())
        
        graph[a].append(b)
        graph[b].append(a)

    pe = {}
    ps = {}
    back = {}
    father = {}    
    for x in range(Q):
        src, dst = map(lambda val: int(val)-1, input().split())

        # pe = [0 for x in range(R)]
        # ps = [0 for x in range(R)]
        # back = [0 for x in range(R)]
        # father = [-1 for x in range(R)]
        t = [0]
        bridges = []

        result = foo(graph, src, t, pe, ps, back, father, dst, bridges)

        #if bridges[-1][0] == src and bridges[0][1] == dst:
        if result and len(bridges) == t[0] -1:
            print("Y")
        else:
            print("N")
        
        pe.clear()
        ps.clear()
        back.clear()
        father.clear()

    print("-")
    
    
    R, C, Q = map(int, input().split())
