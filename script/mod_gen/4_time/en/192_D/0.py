def main():
    X = input()
    M = int(input())
    d = max(X)
    if len(X) == 1:
        if int(X) <= M:
            print(1)
        else:
            print(0)
        return
    start, end = int(d) + 1, M + 1
    while end - start > 1:
        mid = (start + end) // 2
        v = 0
        for c in X:
            v = v * mid + int(c)
            if v > M:
                break
        if v <= M:
            start = mid
        else:
            end = mid
    print(start - int(d))

if __name__ == '__main__':
    main()