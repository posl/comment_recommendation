def main():
    X = input()
    M = int(input())
    d = max([int(i) for i in list(X)])
    if len(X) == 1:
        if d > M:
            print(0)
        else:
            print(1)
        return
    l = d
    r = M+1
    while r-l > 1:
        m = (r+l)//2
        if int(X, m) <= M:
            l = m
        else:
            r = m
    print(l-d)
