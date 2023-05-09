def main():
    N, M = map(int, input().split())
    X = []
    Y = []
    Z = []
    for i in range(N):
        x, y, z = map(int, input().split())
        X.append(x)
        Y.append(y)
        Z.append(z)
    ans = 0
    for i in range(8):
        x = sorted([x if i & 1 == 0 else -x for x in X])
        y = sorted([y if i & 2 == 0 else -y for y in Y])
        z = sorted([z if i & 4 == 0 else -z for z in Z])
        ans = max(ans, sum([x[i] + y[i] + z[i] for i in range(M)]))
    print(ans)
