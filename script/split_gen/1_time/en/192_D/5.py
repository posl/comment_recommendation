def main():
    X = input()
    M = int(input())
    d = 0
    for i in range(len(X)):
        if int(X[i]) > d:
            d = int(X[i])
    if len(X) == 1:
        if int(X) <= M:
            print(1)
        else:
            print(0)
    else:
        l = d
        r = M + 1
        while r - l > 1:
            m = (r + l) // 2
            N = 0
            for i in range(len(X)):
                N = N * m + int(X[i])
            if N <= M:
                l = m
            else:
                r = m
        print(l - d)
