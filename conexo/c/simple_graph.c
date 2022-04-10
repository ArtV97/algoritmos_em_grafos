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
    int **matrix = (int **)calloc(n-1, sizeof(int *));
    
    for (int i = 0; i < n-1; i++) {
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
        i = vertex_index(v, edge[0]);
        j = vertex_index(v, edge[1]);

        edge = strtok_r(NULL, ",", &context);
        if (i == -1 || j == -1) {
            fprintf(stderr, "Invalid edge: %s Skiping...\n", edge);
            continue;
        }

        if (i < j) matrix[j-1][i] = 1;
        else matrix[i][j] = 1;
    }
    free(s);
}


int **generate_matrix(int n, int m, char *v, char *e) {
    int **matrix = init_matrix(n);

    fill_matrix(matrix, v, e);

    return matrix;
}

int *neighbours_of(int **matrix, int n, int index) {
    int *neighbours = (int *)calloc(n, sizeof(int));

    for (int j = 0; j < n; j++) {
        if (index == j) continue;

        if (index < j) neighbours[j] = matrix[j-1][index];
        else if (index == n-1) neighbours[j] = matrix[index-1][j];
        else neighbours[j] = matrix[index][j];
    }

    return neighbours;
}

int are_neighbours(int **matrix, int n, int a, int b) {
    if (a == b) return 0;

    if (a < b) return matrix[b-1][a];
    else if (a == n-1) return matrix[a-1][b];
    else return matrix[a][b];
}

int has_path(int **matrix, int n, int src, int dst, int *visited) {
    visited[src] = 1;
    
    // search in everyone that is conected with src
    if (are_neighbours(matrix, n, src, dst)) return 1; // src and dst are neighbours 
    else {
        for (int i = 0; i < n; i++) {
            if (visited[i]) continue; // vertex already visited
            if (are_neighbours(matrix, n, src, i) && has_path(matrix, n, i, dst, visited)) return 1;
        }
    }

    return 0;
}

void bfs(int **matrix, int n, int v, int *visited) {
    if (visited[v] == 1) return;

    visited[v] = 1;
    for (int i = 0; i < n; i++) {
        if (are_neighbours(matrix, n, v, i) && visited[i] == 0) bfs(matrix, n, i, visited);
    }
}

void print_matrix(int **matrix, int n) {
    for (int i = 0; i < n-1; i++) {
        for (int j = 0; j <= i; j++) {
            fprintf(stderr, "%d ", matrix[i][j]);
        }
        printf("\n");
    }
    
    printf("\n\n");
}

L* init_list(int n, int m) {
    L *l;
    return l;
}