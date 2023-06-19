def main():
    X = input()
    M = int(input())
    d = int(max(X))
    if len(X) == 1:
        if int(X) <= M:
            print(1)
        else:
            print(0)
    else:
        l = d + 1
        r = M + 1
        while r - l > 1:
            m = (l + r) // 2
            if int(X, m) <= M:
                l = m
            else:
                r = m
        print(l - d)
