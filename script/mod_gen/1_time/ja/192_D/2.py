def main():
    X = input()
    M = int(input())
    d = int(max(X))
    if len(X) == 1:
        if d <= M:
            print(1)
        else:
            print(0)
    else:
        left = d
        right = M+1
        while right - left > 1:
            mid = (left + right) // 2
            tmp = 0
            for i in range(len(X)):
                tmp *= mid
                tmp += int(X[i])
                if tmp > M:
                    break
            if tmp <= M:
                left = mid
            else:
                right = mid
        print(left - d)

if __name__ == '__main__':
    main()