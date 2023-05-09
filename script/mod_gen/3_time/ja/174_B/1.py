def main():
    N, D = map(int, input().split())
    X = []
    Y = []
    for i in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    count = 0
    for i in range(N):
        if (X[i]**2 + Y[i]**2) ** 0.5 <= D:
            count += 1
    print(count)

if __name__ == '__main__':
    main()