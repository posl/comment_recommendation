def main():
    N, X = map(int, input().split())
    S = input()
    for i in range(N):
        if S[i] == 'L':
            X = 2 * X
        elif S[i] == 'R':
            X = 2 * X + 1
        else:
            X = (X + 1) // 2
    print(X)

if __name__ == '__main__':
    main()