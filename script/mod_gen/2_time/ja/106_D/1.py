def main():
    N, M, Q = map(int, input().split())
    L = [0] * M
    R = [0] * M
    for i in range(M):
        L[i], R[i] = map(int, input().split())
    p = [0] * Q
    q = [0] * Q
    for i in range(Q):
        p[i], q[i] = map(int, input().split())
    train = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(M):
        train[L[i]][R[i]] += 1
    for i in range(N + 1):
        for j in range(N + 1):
            if i > 0:
                train[i][j] += train[i - 1][j]
    for i in range(Q):
        ans = 0
        for j in range(p[i], q[i] + 1):
            ans += train[j][q[i]]
        print(ans)

if __name__ == '__main__':
    main()