def bfs(graph, v, visited, t):
    t[0] += 1

    visited[v] = t[0]
    
    if graph[v] is None: return # don't have neighbours

    for w in range(len(graph)):
        if graph[v][w] == 1:
            if visited[w] == -1:
                bfs(graph, w, visited, t)
                t[0] += 1
                visited[v] = t[0]





T = int(input())

for x in range(T):
    N = int(input()) # begin's in N
    V, A = map(int, input().split()) # vertex, edges

    graph = [None for i in range(V)]
    for y in range(A):
        v, w = map(int, input().split())

        if graph[v] is None:
            graph[v] = [0 for i in range(V)]
        if graph[w] is None:
            graph[w] = [0 for i in range(V)]
        
        graph[v][w] = 1
        graph[w][v] = 1

    t = [-1]
    visited = [-1 for k in range(V)]
    bfs(graph, N, visited, t)
    for w in range(V):
        if visited[w] == 0:
            if graph[w] is not None:
                bfs(graph, v, visited, t)
            else:
                t[0] += 1
                visited[w] = t[0]

    print(max(visited))