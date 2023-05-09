def main():
    X = input()
    M = int(input())
    if len(X) == 1:
        if int(X) <= M:
            print(1)
        else:
            print(0)
        return
    d = max(X)
    d = int(d)
    l = d + 1
    r = 10**18 + 1
    while r - l > 1:
        mid = (l + r) // 2
        num = 0
        for i in range(len(X)):
            num *= mid
            num += int(X[i])
        if num <= M:
            l = mid
        else:
            r = mid
    print(l - d)

if __name__ == '__main__':
    main()