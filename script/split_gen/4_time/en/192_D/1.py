def main():
    X = input()
    M = int(input())
    if len(X) == 1:
        if int(X) <= M:
            print(1)
        else:
            print(0)
        exit()
    d = max(X)
    d = int(d)
    l = d + 1
    r = M + 1
    while r - l > 1:
        m = (l + r) // 2
        v = 0
        for i in range(len(X)):
            v = v * m + int(X[i])
            if v > M:
                break
        if v <= M:
            l = m
        else:
            r = m
    print(l - d)
