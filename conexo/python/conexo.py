import sys
from grafo import Grafo

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: python conexo.py <filename>")
        sys.exit(1)
    
    filename = sys.argv[1]
    print(f"Reading graph from: {filename}")

    n = None
    grafo = None
    vertex = None
    edges = None

    # reading graph from file
    with open(filename, "r") as f:
        for line in f:
            if line[0] == "#" or line[0] == "\r" or line[0] == "\n": continue

            line = line.strip()

            if line[0:2] == "v:":
                vertex_str = line.split(":")[1]
                vertex = vertex_str.split(",")

                n = len(vertex)
            
            elif line[0:2] == "e:":
                if vertex is None:
                    print("Missing vertex declaration")
                    sys.exit(1)

                edges_str = line.split(":")[1]
                edges = edges_str.split(",")
    

    grafo = Grafo(n, vertex, edges)

    visited, t = grafo.dfs()

    n_cycles = grafo.n_of_cycles()
    if n_cycles == 1:
        print("Grafo conexo!")
    else:
        print(f"Grafo desconexo! Ciclos Completos = {n_cycles}")