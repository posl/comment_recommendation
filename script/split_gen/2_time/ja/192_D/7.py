def main():
    X = input()
    M = int(input())
    d = max(X)
    d = int(d) + 1
    if len(X) == 1:
        if int(X) <= M:
            print(1)
        else:
            print(0)
        return
    l = 0
    r = M
    while r - l > 1:
        m = (l + r) // 2
        t = 0
        for i in range(len(X)):
            t *= d
            t += int(X[i])
            if t > M:
                break
        if t <= M:
            l = m
        else:
            r = m
    print(l - d + 1)
