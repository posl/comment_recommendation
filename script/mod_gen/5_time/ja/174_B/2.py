def main():
    N, D = map(int, input().split())
    X = []
    Y = []
    for i in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    cnt = 0
    for i in range(N):
        if pow(pow(X[i],2) + pow(Y[i],2), 1/2) <= D:
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()