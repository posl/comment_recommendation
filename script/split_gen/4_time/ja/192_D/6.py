def main():
    X = int(input())
    M = int(input())
    d = max([int(i) for i in str(X)])
    if X <= M:
        print(1)
        return
    if len(str(X)) == 1:
        print(0)
        return
    if M < d+1:
        print(0)
        return
    l = d+1
    r = M+1
    while l+1 < r:
        m = (l+r)//2
        s = 0
        for c in str(X):
            s = s*m + int(c)
            if s > M:
                break
        if s <= M:
            l = m
        else:
            r = m
    print(l-d)
    return
