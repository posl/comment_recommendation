def solve():
    N, M = map(int, input().split())
    if M == 0:
        print('Yes')
        return
    A = [0] * M
    B = [0] * M
    for i in range(M):
        a, b = map(int, input().split())
        A[i] = a
        B[i] = b
    if N == 2:
        print('No')
        return
    adj = [[] for _ in range(N + 1)]
    for i in range(M):
        adj[A[i]].append(B[i])
        adj[B[i]].append(A[i])
    for i in range(1, N + 1):
        if len(adj[i]) == N - 1:
            print('Yes')
            return
    print('No')

if __name__ == '__main__':
    solve()