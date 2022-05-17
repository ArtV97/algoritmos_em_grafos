import heapq

def alterar_prioridade(w,D):
    for i in range(len(D)):
        if D[i][1] == w:
            pos = i
            break
    D[pos] = (L[w], w)
    heapq._siftdown(D, 0, pos)
    return



while True:
    N, M, C, K = map(int, input().split())

    if N == 0 and M == 0 and C == 0 and K == 0:
        break

    grafo = [[] * N for i in range(N)]  # definir listas de adjacencia
    custo = []
    infty = 99999999
    # definir a matriz de custos (pesos)
    for i in range(N):
        linha = []
        for j in range(N):
            if i == j:
                linha.append(0)
            else:
                linha.append(infty)
        custo.append(linha)

    for j in range(M):
        # estrada entre U e V com pedagio P
        U, V, P = map(int, input().split())

        grafo[U].append(V)
        grafo[V].append(U)
        custo[U][V] = P
        custo[V][U] = P

    #inicializacoes

    marca = N*[0]
    L = N*[infty]
    raiz = K
    L[raiz] = 0
    D = [(0, raiz)]      # cada posição do heap guarda (L(w), w)
    for w in range(0, N):
        if w != raiz:
            heapq.heappush(D, (L[w], w))  # iniciar o heap com todos os valores
    pai = N*[-1]

    # print(f"N = {N}, M = {M}, C = {C}, K = {K}")

    while D != []:
        Lmin, v = heapq.heappop(D)      # tirar a raiz do heap
        marca[v] = 1

        # restricao do problema
        if v < C:
            custo_v2x = L[v]
            for x in range(v, C-1):
                custo_v2x += custo[x][x+1]
                if custo_v2x < L[x+1]:
                    L[x+1] = custo_v2x
            
            continue

        for w in grafo[v]:
            if marca[w] == 0:
                custo_v2w = L[v]
                
                custo_v2w += custo[v][w]
                    
                if custo_v2w < L[w]:
                    L[w] = custo_v2w          # atualizar o valor de L[w]
                    alterar_prioridade(w, D)    # atualizar o heap
                    pai[w] = v

    # print(f"L = {L}")
    # print(f"pai = {pai}")
    # print("\n\n")
    print(L[C-1])