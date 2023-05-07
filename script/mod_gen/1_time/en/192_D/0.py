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
    l = 0
    r = M + 1
    while r - l > 1:
        m = (l + r) // 2
        if int(X, m) <= M:
            l = m
        else:
            r = m
    if d + 1 <= l:
        print(l - d)
    else:
        print(0)

if __name__ == '__main__':
    main()