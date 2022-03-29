#include <stdlib.h>
#include <string.h>
#include <stdio.h>

typedef struct adjacency_list {
    char info[8];
    struct adjacency_list *next;
} L;


int **generate_matrix(int n, int m, char *v, char *e);
int *neighbours_of(int **matrix, int n, char *v, char c);

L* init_list(int n, int m);