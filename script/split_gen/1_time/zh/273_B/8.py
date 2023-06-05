def round_up(x, n):
    if n == 1:
        return x
    else:
        return (x // (10 ** n) + 1) * (10 ** n)
X, K = map(int, input().split())
for _ in range(K):
    X = round_up(X, K)
print(X)
