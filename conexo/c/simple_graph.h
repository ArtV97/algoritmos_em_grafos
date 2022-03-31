#include <stdlib.h>
#include <string.h>
#include <stdio.h>

typedef struct adjacency_list {
    char info[8];
    struct adjacency_list *next;
} L;


int **generate_matrix(int n, int m, char *v, char *e);
int has_path(int **matrix, int n, int src, int dst, int *visited);
void print_matrix(int **matrix, int n);

L* init_list(int n, int m);