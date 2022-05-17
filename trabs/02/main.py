# rota de serviço: é composta por C cidades e C−1 estradas: a primeira cidade da rota de serviço é a origem da encomenda,
## a última o destino da encomenda. A rota de serviço não passa duas vezes pela mesma cidade, e o veículo escolhido para 
## fazer o transporte de uma encomenda pode trafegar apenas pela rota de serviço definida.

#representando, respectivamente, o número de cidades do país, o número de estradas, o número de cidades na rota de serviço e a 
#cidade em que o veículo foi consertado. As cidades são identificadas por inteiros de 0 a N−1. A rota de serviço é 0, 1, ... , 
#C−1, ou seja, a origem é 0, de 0 passa para 1, de 1 para 2 e assim por diante, até o destino C−1.


def bfs(grafo, root, t, L, pai, C, F = []):
    t[0] += 1
    L[root] = t[0]

    F.append(root)


    while len(F) > 0:
        v = F.pop()

        if grafo[v] is None: continue # don't have neighbours

        # restricao do problema
        # if v < C:
        #     prev = v
        #     for rota in range(v+1, C):
        #         print(v, rota, pai)
        #         t[0] += 1
        #         L[rota] = t[0]
        #         pai[rota] = prev
        #         prev = rota
            
        #     return


        for w in range(len(grafo)):
            if grafo[v][w] is None: continue # isn't neighbour

            if L[w] == 0:
                pai[w] = v
                t[0] += 1
                L[w] = t[0]
                F.append(w)



# N cidades
# M estradas
# C cidades na rota de servico. A rota de serviço é 0, 1, ... , C−1
# K cidade na qual o veiculo foi consertado
if __name__ == "__main__":
    while True:
        N, M, C, K = map(int, input().split())

        if N == 0 and M == 0 and C == 0 and K == 0:
            break

        grafo = [None for j in range(N)]
        for i in range(M):
            # estrada entre U e V com pedagio P
            U, V, P = map(int, input().split())

            if grafo[U] is None:
                grafo[U] = [None for i in range(N)]
            if grafo[V] is None:
                grafo[V] = [None for i in range(N)]
            
            grafo[U][V] = P
            grafo[V][U] = P

        L = [0 for x in range(N)]
        pai = [None for x in range(N)]

        t = [0]
        bfs(grafo, K, t, L, pai, C)
        print(f"N = {N}, M = {M}, C = {C}, K = {K}")
        print(f"L: {L}")
        print(f"pai: {pai}")

        cost = 0
        v = C-1
        while pai[v] is not None:
            cost += grafo[pai[v]][v]
            v = pai[v]

        print(f"Cost = {cost}\n")