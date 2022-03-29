#include "simple_graph.h"
#include "util.h"


int is_conexo_matrix(int **matrix, int n, char *v) {
    char *s = strdup(v);
    char *tok = strtok(s, ",");
    int *neighbours;

    while (tok != NULL) {
        neighbours = neighbours_of(matrix, n, v, tok[0]);
        fprintf(stderr, "%c = ", tok[0]);
        for (int i = 0; i < n; i++) {
            fprintf(stderr, "%d ", neighbours[i]);
        }
        fprintf(stderr, "\n");
        free(neighbours);

        tok = strtok(NULL, ",");
    }
    free(s);
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
    if (is_conexo_matrix(matrix, n, v)) printf("Eh conexo!\n");
    else printf("Nao eh conexo!\n");

    free(v);
    free(e);
    return 0;
}