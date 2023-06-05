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
        # 二分查找
        left = d
        right = 10 ** 18 + 1
        while left + 1 < right:
            mid = (left + right) // 2
            if check(mid, X, M):
                left = mid
            else:
                right = mid
        print(left - d)

if __name__ == '__main__':
    main()