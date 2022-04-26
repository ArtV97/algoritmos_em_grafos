def dfs_interactive(graph, visited, t, v):
    stack = [v]

    while len(stack) > 0:
        v = stack.pop()

        if visited[v] != 0: continue

        t[0] += 1
        visited[v] = t[0]

        for w in graph[v]:
            if visited[w] == 0:
                stack.append(w)


#######
# Main
#######
N, M = map(int, input().split())

graph = []
prev_line = None
vertex_count = -1

for x in range(N):
    #line = input()
    line_conf = []

    for i, pixel in enumerate(input()):
        if pixel == "o":
            line_conf.append((pixel, vertex_count))
            continue

        vertex_count += 1
        line_conf.append((pixel, vertex_count))
        
        graph.append([]) # new vertex

        if i - 1 >= 0 and line_conf[i-1][0] == ".": # vizinho da esquerda
            #graph[line_conf[i][1]].append(line_conf[i-1][1])
            graph[line_conf[i-1][1]].append(line_conf[i][1])
        if prev_line and prev_line[i][0] == ".": # vizinho de cima
            #graph[line_conf[i][1]].append(prev_line[i][1])
            graph[prev_line[i][1]].append(line_conf[i][1])

    prev_line = line_conf


if vertex_count != -1:
    visited = [0 for x in range(vertex_count+1)]
    t = [0]
    dfs_interactive(graph, visited, t, 0)
    n_cycles = 1

    if t[0] != vertex_count:
        for v in range(vertex_count+1):
            if (visited[v] == 0):
                dfs_interactive(graph, visited, t, v)
                n_cycles += 1
    
    print(vertex_count)
    print(n_cycles)
else:
    print(0) # nada para colorir
