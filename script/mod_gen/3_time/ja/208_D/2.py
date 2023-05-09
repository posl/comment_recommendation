def solve():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    C = [0] * M
    for i in range(M):
        A[i], B[i], C[i] = map(int, input().split())
        A[i] -= 1
        B[i] -= 1
    from collections import defaultdict
    d = defaultdict(list)
    for i in range(M):
        d[A[i]].append((B[i], C[i]))
    ans = 0
    for k in range(N):
        dist = [float('inf')] * N
        dist[k] = 0
        for i in range(N):
            for j in range(N):
                for v, c in d[j]:
                    if dist[j] + c < dist[v]:
                        dist[v] = dist[j] + c
        for i in range(N):
            if dist[i] != float('inf'):
                ans += dist[i]
    print(ans)
    return

if __name__ == '__main__':
    solve()