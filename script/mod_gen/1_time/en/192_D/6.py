def solve():
    X = input()
    M = int(input())
    d = max(X)
    d = int(d)
    if len(X) == 1:
        if d <= M:
            print(1)
        else:
            print(0)
        return
    l = d + 1
    r = M + 1
    while r - l > 1:
        m = (l + r) // 2
        v = 0
        for i in range(len(X)):
            v = v * m + int(X[i])
        if v <= M:
            l = m
        else:
            r = m
    print(l - d)
solve()

if __name__ == '__main__':
    solve()