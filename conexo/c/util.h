#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define BUFFER_SZ 1024

// a = vertex string. delimiter ','
// b = edge string. delimiter ','
int read_file(char *filename, char **v, char **e);
void calc_m_n(char *v, char *e, int *m, int *n);
