def main():
    X = input()
    M = int(input())
    if len(X) == 1:
        if int(X) <= M:
            print(1)
        else:
            print(0)
        return
    X = [int(x) for x in X]
    d = max(X)
    left = d
    right = 10**18+1
    while right - left > 1:
        mid = (right + left) // 2
        if check(X, M, mid):
            left = mid
        else:
            right = mid
    print(left - d)

if __name__ == '__main__':
    main()