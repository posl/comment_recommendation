def main():
    N, M = map(int, input().split())
    x, y, z = [], [], []
    for _ in range(N):
        a, b, c = map(int, input().split())
        x.append(a)
        y.append(b)
        z.append(c)
    ans = 0
    for i in range(2):
        for j in range(2):
            for k in range(2):
                X = [x[l] if (i + j + k) % 2 == 0 else -x[l] for l in range(N)]
                Y = [y[l] if (i + j + k) % 2 == 0 else -y[l] for l in range(N)]
                Z = [z[l] if (i + j + k) % 2 == 0 else -z[l] for l in range(N)]
                X.sort(reverse=True)
                Y.sort(reverse=True)
                Z.sort(reverse=True)
                ans = max(ans, sum(X[:M]) + sum(Y[:M]) + sum(Z[:M]))
    print(ans)
