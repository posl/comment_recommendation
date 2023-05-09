def main():
    N = int(input())
    X = [0] * N
    Y = [0] * N
    for i in range(N):
        x, y = map(int, input().split())
        X[i] = x
        Y[i] = y
    X.sort()
    Y.sort()
    ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            ans += (X[j] - X[i]) * (Y[j] - Y[i])
    print(ans)
main()

if __name__ == '__main__':
    main()