def main():
    X = input()
    M = int(input())
    d = 0
    for x in X:
        d = max(d, int(x))
    if len(X) == 1:
        print(1 if d <= M else 0)
        return
    left = d
    right = M + 1
    while right - left > 1:
        mid = (left + right) // 2
        if int(X, mid) <= M:
            left = mid
        else:
            right = mid
    print(left - d)

if __name__ == '__main__':
    main()