def solve():
    X = input()
    M = int(input())
    if len(X) == 1:
        if int(X) <= M:
            print(1)
        else:
            print(0)
        return
    d = int(max(X))
    ans = 0
    l = d
    r = M + 1
    while r - l > 1:
        m = (l + r) // 2
        v = 0
        for x in X:
            v = v * m + int(x)
            if v > M:
                break
        if v <= M:
            l = m
        else:
            r = m
    print(l - d)

if __name__ == '__main__':
    solve()