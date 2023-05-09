def main():
    N = int(input())
    X = [0] * N
    Y = [0] * N
    P = [0] * N
    for i in range(N):
        x, y, p = map(int, input().split())
        X[i] = x
        Y[i] = y
        P[i] = p
    ans = 0
    for i in range(N):
        for j in range(N):
            if P[i] * (ans + 1) >= abs(X[i] - X[j]) + abs(Y[i] - Y[j]):
                ans = max(ans, abs(X[i] - X[j]) + abs(Y[i] - Y[j]))
    print(ans)

if __name__ == '__main__':
    main()