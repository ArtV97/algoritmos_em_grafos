#include "simple_graph.h"
#include "util.h"


int is_conexo_matrix(int **matrix, int n) {
    int visited[n];
    for (int i = 0; i < n; i++) visited[i] = 0;

    for (int src = 0; src < n; src++) {
        for (int dst = src+1; dst < n; dst++) {
            if (!has_path(matrix, n, src, dst, visited)) return 0;
        }
    }
    return 1;
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

    printf("v: %s, e: %s\n", v, e);

    int **matrix = generate_matrix(n, m, v, e);
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; j <= i; j++) {
            fprintf(stderr, "%d ", matrix[i][j]);
        }
        printf("\n");
    }
    
    printf("\n\n");
    
    if (is_conexo_matrix(matrix, n)) printf("Eh conexo!\n");
    else printf("Nao eh conexo!\n");

    free(v);
    free(e);
    for (int i = 0; i < n; i++) free(matrix[i]);
    free(matrix);
    return 0;
}