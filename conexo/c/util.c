#include "util.h"

int read_file(char *filename, char **v, char **e) {
    FILE *f = fopen(filename, "r");
    if (f == NULL) return 1;

    int n;
    char line[BUFFER_SZ+1];
    char *p;
    while (fgets(line, BUFFER_SZ, f)) {
        if (line[0] == '#' || line[0] == '\r' || line[0] == '\n') continue; // ignore comment and empty lines

        n = strlen(line);
        if (line[--n] == '\n') line[n] = '\0'; // remove '\n'
        if (line[--n] == '\r') line[n] = '\0'; // remove '\r'

        p = strtok(line, ":");

        if (strcmp(p, "v") == 0) {
            p = strtok(NULL, ":");
            *v = strdup(p);
        }
        else if (strcmp(p, "e") == 0) {
            p = strtok(NULL, ":");
            *e = strdup(p);
        }
    }
    fclose(f);
    return 0;
}

void calc_m_n(char *v, char *e, int *m, int *n) {
    int i;
    
    *n = 0;
    for (i = 0; i < strlen(v); i++) {
        if (v[i] != ',') {
            *n = *n + 1;
        }
    }

    *m = 0;
    for (i = 0; i + 1 < strlen(e); i++) {
        if (e[i] != ',' && e[i+1] != ',') {
            *m = *m + 1;
        }
    }
}

// int main(int argc, char *argv[]){
//     char *v;
//     char *e;
//     read_file("data_example/1.txt", &v, &e);
//     printf("Vertex = %s\n", v);
//     printf("Edges = %s\n\n", e);


//     int m;
//     int n;

//     calc_m_n(v, e, &m, &n);

//     printf("m = %d, n = %d\n", m, n);
//     free(v);
//     free(e);
//     return 0;
// }