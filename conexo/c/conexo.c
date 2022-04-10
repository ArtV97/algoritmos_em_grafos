#include "simple_graph.h"
#include "util.h"


int is_conexo_matrix(int **matrix, int n) {
    int visited[n];
    for (int i = 0; i < n; i++) visited[i] = 0; // init empty visited array

    bfs(matrix, n, 0, visited);
    int visit_count = 0;
    for (int i = 0; i < n; i++) {
        if (visited[i] == 1) visit_count++;
    }

    if (visit_count != n) return 0;
    return 1;
}

int nofcycles(int **matrix, int n) {
    int visited[n];
    for (int i = 0; i < n; i++) visited[i] = 0; // init empty visited array

    bfs(matrix, n, 0, visited);
    int visit_count = 0;
    for (int i = 0; i < n; i++) {
        if (visited[i] == 1) visit_count++;
    }

    if (visit_count == n) return 1;

    int n_cycles = 1;
    for (int i = 0; i < n; i++) {
        if (visited[i] == 0) {
            bfs(matrix, n, i, visited);
            n_cycles++;
        }
    }

    return n_cycles;
}


int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Must have one argument(filename)!\n");
        return 1;
    }

    char *filename = argv[1];

    
    char *v;
    char *e;
    read_file(filename, &v, &e);

    int m;
    int n;
    calc_m_n(v, e, &m, &n);

    printf("v: %s\ne: %s\n", v, e);

    int **matrix = generate_matrix(n, m, v, e);
    
    print_matrix(matrix, n);
    
    if (is_conexo_matrix(matrix, n)) printf("Eh conexo!\n");
    else printf("Nao eh conexo! Quantidade de Ciclos Conexos = %d\n", nofcycles(matrix, n));

    free(v);
    free(e);
    for (int i = 0; i < n-1; i++) free(matrix[i]);
    free(matrix);
    return 0;
}