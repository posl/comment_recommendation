def main():
    X = input()
    M = int(input())
    d = max([int(i) for i in X])
    if len(X) == 1:
        print(1 if int(X) <= M else 0)
        return
    left = d
    right = M + 1
    while right - left > 1:
        mid = (right + left) // 2
        if int(X, mid) > M:
            right = mid
        else:
            left = mid
    print(left - d)

if __name__ == '__main__':
    main()