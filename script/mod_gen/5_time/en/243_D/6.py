def main():
    N, X = map(int, input().split())
    S = input()
    i = 0
    while i < N:
        if S[i] == 'U':
            X = X // 2
        elif S[i] == 'L':
            X = X * 2
        else:
            X = X * 2 + 1
        i += 1
    print(X)

if __name__ == '__main__':
    main()