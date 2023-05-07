def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    X = 0
    for i in range(40, -1, -1):
        if K & (1 << i):
            X = X | (1 << i)
            f = [0] * (N + 1)
            for j in range(N):
                f[j + 1] = f[j] + (A[j] ^ X)
            f.sort()
            g = [0] * (N + 1)
            for j in range(N):
                g[j + 1] = g[j] + (A[j] ^ (X - 1))
            g.sort()
            S = 0
            for j in range(N + 1):
                S += (j - bisect_left(g, f[j])) * (f[j] - g[j])
            if S <= (N * (N + 1)) // 2:
                X = X - 1
    print(X)

if __name__ == '__main__':
    main()