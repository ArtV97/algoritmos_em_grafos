import heapq

N, M = map(int, input().split())         # ler numero de vertices e arestas

H = []

while(N != 0 and M != 0):
    custo_total = 0
    for j in range(M):                          # ler as M arestas do digrafo
        a, b, c =  map(int, input().split())    # ler aresta de a para b com custo c
        custo_total += c
        heapq.heappush(H, (c, a, b))  # colocar aresta no heap. O custo "c" determina a prioridade

    C = [[] * N for i in range(N)]    # criar N conjuntos

    for i in range(N):
        C[i].append(i)                # cada C[i] é inicializado com {i}

    S = []
    for i in range(N):
        S.append(i)                   # S[i] é o conjunto ao qual o vértice i pertence

    cont = 0
    custo = 0

    while cont < N-1:                 # bastam N-1 arestas
        c, a, b = heapq.heappop(H)    # remover a próxima aresta do heap
        if S[a] != S[b]:              # se as arestas unem árvores diferentes...
            custo = custo + c
            p = S[a]
            q = S[b]
            if q < p:
                p, q = q, p
            for j in C[q]:           # para cada j no conjunto C[q]
                S[j] = p
            C[p].extend(C[q])        # unir C[p] e C[q] (a união fica em C[p])
            C[q] = []                # esvaziar C[q]
            cont = cont + 1
    
    print(custo_total-custo)

    N, M = map(int, input().split())         # ler numero de vertices e arestas

    H = []