def main():
    X = input()
    M = int(input())
    if len(X) == 1:
        if int(X) <= M:
            print(1)
        else:
            print(0)
        return
    X = [int(x) for x in X]
    D = max(X)
    X = X[::-1]
    l, r = D+1, 10**18+1
    while r - l > 1:
        m = (l + r) // 2
        v = 0
        for i in range(len(X)):
            v += X[i] * m ** i
        if v <= M:
            l = m
        else:
            r = m
    print(l - D)
