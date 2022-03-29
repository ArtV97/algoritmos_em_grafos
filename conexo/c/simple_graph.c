#include "simple_graph.h"


int vertex_index(char *v, char c) {
    char *s = strdup(v);
    char *context = NULL;
    char *tok = strtok_r(s, ",", &context);
    
    // if (tok == NULL) return -1;
    // else if (is_row) tok = strtok_r(NULL, ",", &context); // ignore the first

    int index = 0; // index begins at 0
    while (tok != NULL) {
        if (tok[0] == c) {
            free(s);
            return index;
        }

        tok = strtok_r(NULL, ",", &context);
        index++;
    }

    free(s);
    return -1;
}

// n: quantity of vertex
// m: quantity of edges
int** init_matrix(int n) {
    int **matrix = (int **)calloc(n, sizeof(int *));
    
    for (int i = 0; i < n; i++) {
        matrix[i] = (int *)calloc((i+1), sizeof(int));
    }

    return matrix;
}


void fill_matrix(int **matrix, char *v, char *e) {
    char *s = strdup(e);
    char *context = NULL;
    char *edge = strtok_r(s, ",", &context); // strtok uses static global. Use this istead
    int i;
    int j;

    
    while (edge != NULL) {
        i = vertex_index(v, edge[1]);
        j = vertex_index(v, edge[0]);

        edge = strtok_r(NULL, ",", &context);
        if (i == -1 || j == -1) continue;

        if (i < j) continue;

        matrix[i][j] = 1;
    }
    free(s);
}


int **generate_matrix(int n, int m, char *v, char *e) {
    int **matrix = init_matrix(n);

    fill_matrix(matrix, v, e);

    return matrix;
}

int *neighbours_of(int **matrix, int n, char *v, char c) {
    int index = vertex_index(v, c);
    int *neighbours = (int *)calloc(n, sizeof(int));
    //int count = 0;


    // check index as row
    for (int j = 0; j <= index; j++) {
        if (matrix[index][j]) {
            neighbours[j] = 1;
        }
    }

    // check index as column
    for (int i = index; i < n-1; i++) {
        if (matrix[i][index]) {
            neighbours[i] = 1;
        }
    }

    return neighbours;
}


L* init_list(int n, int m) {
    L *l;
    return l;
}