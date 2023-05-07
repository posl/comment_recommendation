def main():
    N, M, Q = map(int, input().split())
    train = [[0] * (N + 1) for i in range(N + 1)]
    for _ in range(M):
        L, R = map(int, input().split())
        train[L][R] += 1
    for i in range(N + 1):
        for j in range(N):
            train[i][j + 1] += train[i][j]
    for _ in range(Q):
        p, q = map(int, input().split())
        ans = 0
        for i in range(p, q + 1):
            ans += train[i][q] - train[i][p - 1]
        print(ans)
