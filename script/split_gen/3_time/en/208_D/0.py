def solve():
    N, M = map(int, input().split())
    A = []
    B = []
    C = []
    for _ in range(M):
        a, b, c = map(int, input().split())
        A.append(a)
        B.append(b)
        C.append(c)
    # f(s,t,k) = min cost from s to t using only cities 1, 2, ..., k
    f = [[10**18] * (N + 1) for _ in range(N + 1)]
    for i in range(N):
        f[i][i] = 0
        f[i + 1][i + 1] = 0
    for i in range(M):
        a = A[i]
        b = B[i]
        c = C[i]
        f[a][b] = min(f[a][b], c)
    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                f[i][j] = min(f[i][j], f[i][k] + f[k][j])
    ans = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            for k in range(1, N + 1):
                ans += f[i][j]
    print(ans)
solve()
I’m not sure if this is the best solution, but it works. The solution is based on floyd-warshall algorithm. The time complexity is O(N^3) and the space complexity is O(N^2).
I also tried to solve this problem using Dijkstra’s algorithm, but it didn’t work. Here is my solution.
