def main():
    #输入
    X = input()
    M = int(input())
    #初始化
    d = 0
    for i in range(len(X)):
        if d < int(X[i]):
            d = int(X[i])
    #二分查找
    l = d
    r = M + 1
    while r - l > 1:
        m = (l + r) // 2
        sum = 0
        for i in range(len(X)):
            sum = sum * m + int(X[i])
            if sum > M:
                break
        if sum <= M:
            l = m
        else:
            r = m
    print(l - d)

if __name__ == '__main__':
    main()