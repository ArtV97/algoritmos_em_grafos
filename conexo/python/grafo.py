class Grafo():
    def __init__(self, n:int, v:list, e:list):
        self.n = n
        self.v = v

        self.matrix = [None for i in range(n-1)]
        for i in range(n-1): self.matrix[i] = [False for j in range(i+1)]
        
        for edge in e:
            
            i = v.index(edge[0])
            j = v.index(edge[1])

            if i == -1 or j == -1:
                print(f"Invalid edge {edge} skipping...")
                continue
            
            if i < j: self.matrix[j-1][i] = True
            else: self.matrix[i][j] = True
    
    
    def are_neighbours(self, a, b):
        if a == b: return False

        if a < b: return self.matrix[b-1][a]
        elif a == self.n-1: return self.matrix[a-1][b]
        
        return self.matrix[a][b]
    
    
    def bfs(self, v = 0, visited = None, t=[0]):
        if visited is None: visited = [0 for i in range(self.n)]
        
        if visited[v] == 1:
            return
        
        t[0] = t[0] + 1
        #print("visitando o vértice", v, "no tempo", t[0])
        
        visited[v] = 1
        for w in range(self.n):
            if self.are_neighbours(v, w) and visited[w]  == 0:
                self.bfs(w, visited, t)
        
        return visited, t[0]
    
    
    def is_connected(self):
        visited, t = self.bfs()

        if t == self.n: return True
        return False
    

    def n_of_cycles(self):
        visited, t = self.bfs()

        if t == self.n: return 1

        n_cycles = 1
        for v in range(self.n):
            if (visited[v] == 0):
                self.bfs(v, visited)
                n_cycles += 1

        return n_cycles
