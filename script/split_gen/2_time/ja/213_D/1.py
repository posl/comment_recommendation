def main():
    N = int(input())
    A = [0] * (N-1)
    B = [0] * (N-1)
    for i in range(N-1):
        A[i], B[i] = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for i in range(N-1):
        graph[A[i]].append(B[i])
        graph[B[i]].append(A[i])
    for i in range(N+1):
        graph[i].sort()
    ans = [1]
    visited = [0] * (N+1)
    visited[1] = 1
    current = 1
    while len(ans) < N:
        if len(graph[current]) == 0:
            break
        elif visited[graph[current][0]] == 0:
            current = graph[current][0]
            ans.append(current)
            visited[current] = 1
        else:
            current = ans[-2]
            ans.append(current)
    print(*ans)
