def main():
    X = int(input())
    M = int(input())
    X = str(X)
    X = list(X)
    X = [int(i) for i in X]
    X = sorted(X,reverse=True)
    X = X[0]
    if X == 1:
        print(1)
        exit()
    if M < X:
        print(0)
        exit()
    else:
        left = X
        right = M + 1
        while (right - left) > 1:
            mid = (left + right) // 2
            num = 0
            for i in range(len(str(M))):
                num += (mid ** i) * int(str(M)[i])
            if num > M:
                right = mid
            else:
                left = mid
        print(left - X)

if __name__ == '__main__':
    main()