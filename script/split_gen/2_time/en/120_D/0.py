def main():
    N, M = map(int, input().split())
    A = [0] * M
    B = [0] * M
    for i in range(M):
        A[i], B[i] = map(int, input().split())
    G = [set() for _ in range(N + 1)]
    for i in range(M):
        G[A[i]].add(B[i])
        G[B[i]].add(A[i])
    ans = [0] * M
    ans[M - 1] = N * (N - 1) // 2
    for i in range(M - 1, 0, -1):
        ans[i - 1] = ans[i]
        if len(G[A[i]]) > len(G[B[i]]):
            A[i], B[i] = B[i], A[i]
        for j in G[A[i]]:
            if j < A[i]:
                ans[i - 1] -= 1
            G[j].remove(A[i])
            G[j].add(B[i])
        G[B[i]].update(G[A[i]])
        G[A[i]] = set()
    print('
'.join(map(str, ans)))
