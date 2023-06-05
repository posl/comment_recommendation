def main():
    L, Q = map(int, input().split())
    X = [0, L]
    for _ in range(Q):
        c, x = map(int, input().split())
        if c == 1:
            X.append(x)
        else:
            X.sort()
            for i in range(len(X)):
                if X[i] == x:
                    print(X[i + 1] - X[i - 1])
                    break
