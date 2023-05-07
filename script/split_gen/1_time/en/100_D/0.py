def main():
    N, M = map(int, input().split())
    X, Y, Z = [], [], []
    for _ in range(N):
        x, y, z = map(int, input().split())
        X.append(x)
        Y.append(y)
        Z.append(z)
    ans = 0
    for i in range(2**3):
        x = [0] * N
        for j in range(N):
            if i & 1:
                x[j] += X[j]
            else:
                x[j] -= X[j]
            if i & 2:
                x[j] += Y[j]
            else:
                x[j] -= Y[j]
            if i & 4:
                x[j] += Z[j]
            else:
                x[j] -= Z[j]
        x.sort(reverse=True)
        ans = max(ans, sum(x[:M]))
    print(ans)
