def main():
    X = input()
    M = int(input())
    d = max([int(x) for x in X])
    if len(X) == 1:
        if d <= M:
            print(1)
        else:
            print(0)
        return
    low = d
    high = M+1
    while high - low > 1:
        mid = (low + high) // 2
        n = 0
        for x in X:
            n = n * mid + int(x)
            if n > M:
                break
        if n > M:
            high = mid
        else:
            low = mid
    print(low - d)
main()

if __name__ == '__main__':
    main()