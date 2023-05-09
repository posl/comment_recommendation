def main():
    S = input()
    N = len(S)
    X = [0] * N
    X[0] = 1
    X[-1] = 1
    for i in range(1, N - 1):
        if S[i - 1] == S[i]:
            X[i] = X[i - 1] + 1
        else:
            X[i] = 1
    for i in range(N - 2, 0, -1):
        if S[i - 1] == S[i]:
            X[i] = X[i + 1] + 1
    print(*X)

if __name__ == '__main__':
    main()