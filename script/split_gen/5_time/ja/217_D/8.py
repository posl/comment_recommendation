def main():
    L, Q = map(int, input().split())
    X = [0, L]
    for _ in range(Q):
        c, x = map(int, input().split())
        if c == 1:
            X.append(x)
        else:
            X.sort()
            idx = X.index(x)
            print(X[idx] - X[idx - 1])
