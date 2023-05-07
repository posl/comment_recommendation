def main():
    X = input()
    M = int(input())
    d = int(max(X))
    if len(X) == 1:
        if d <= M:
            print(1)
        else:
            print(0)
        return
    l = d + 1
    r = 10**18 + 1
    while r - l > 1:
        m = (l + r) // 2
        if check(X, M, m):
            l = m
        else:
            r = m
    print(l - d)
