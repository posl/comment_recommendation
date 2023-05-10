def main():
    N, X = map(int, input().split())
    S = input()
    for s in S:
        if s == 'U':
            X = (X + 1) // 2
        elif s == 'L':
            X = 2 * X
        else:
            X = 2 * X + 1
    print(X)

if __name__ == '__main__':
    main()