def main():
    N = int(input())
    X = []
    Y = []
    for i in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if -1 <= (Y[j] - Y[i]) / (X[j] - X[i]) <= 1:
                ans += 1
    print(ans)

if __name__ == '__main__':
    main()