def solve():
    X = input()
    M = int(input())
    d = int(max(X))
    n = d + 1
    while True:
        v = 0
        for c in X:
            v = v * n + int(c)
            if v > M:
                break
        if v <= M:
            n += 1
        else:
            break
    print(n - d - 1)
