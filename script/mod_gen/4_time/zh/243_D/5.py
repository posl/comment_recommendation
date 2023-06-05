def main():
    N, X = map(int, input().split())
    S = input()
    for i in range(N):
        if S[i] == 'U':
            X = (X + 1) // 2
        elif S[i] == 'L':
            X = X * 2 - 1
        else:
            X = X * 2 + 1
    print(X)

if __name__ == '__main__':
    main()