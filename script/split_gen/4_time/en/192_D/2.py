def main():
    X = input()
    M = int(input())
    d = 0
    for i in X:
        if int(i) > d:
            d = int(i)
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
        val = 0
        for i in X:
            val = val * m + int(i)
            if val > M:
                break
        if val > M:
            r = m
        else:
            l = m
    print(l - d)
