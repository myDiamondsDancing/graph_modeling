#include <stdlib.h>
#include <stdio.h>

#define GRAPH uint **
#define index(i, j) i * N + j

/*
:graph - graph which represented as matrix with size NxN
:N - size of matrix (number of nodes)
:start - index of node which is start of route
:end - index of node which is end of route
:returns - true if graph includes route start -> n1 -> ... -> end else false
*/
uint has_part(GRAPH graph, int N, int start, int end);

uint dfs(GRAPH graph, int N, uint * visited, int start, int end);
