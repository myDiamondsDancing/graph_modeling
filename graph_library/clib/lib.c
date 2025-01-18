#include "lib.h"

uint has_route(GRAPH graph, int N, int start, int end) {
    uint * visited = (uint *) malloc(N);

    for (int i = 0; i < N; i++)
        visited[i] = 0;

    return dfs(graph, N, visited, start, end);
}

uint dfs(GRAPH graph, int N, uint * visited, int start, int end){
    if (start == end)
        return 1;

    visited[start] = 1;

    for (int j = 0; j < N; j++)
        if (graph[index(start, j)])
            if (!visited[j])
                if (dfs(graph, N, visited, j, end))
                    return 1;

    return 0;
}
