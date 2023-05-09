def main():
    X = input()
    M = int(input())
    X = list(X)
    X = list(map(int, X))
    X.sort(reverse=True)
    d = X[0]
    X = list(map(str, X))
    X = "".join(X)
    X = int(X)
    if d+1 > M:
        print(1)
    else:
        left = d+1
        right = M+1
        while right - left > 1:
            mid = (left + right) // 2
            if mid**len(str(X)) > M:
                right = mid
            else:
                left = mid
        print(left-d)

if __name__ == '__main__':
    main()