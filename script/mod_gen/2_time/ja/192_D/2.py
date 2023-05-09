def main():
    X = input()
    M = int(input())
    d = int(max(X))
    if len(X) == 1:
        if d > M:
            print(0)
        else:
            print(1)
        return
    l = d
    r = M + 1
    while r - l > 1:
        mid = (r + l) // 2
        if int(X, mid) <= M:
            l = mid
        else:
            r = mid
    print(l - d)

if __name__ == '__main__':
    main()