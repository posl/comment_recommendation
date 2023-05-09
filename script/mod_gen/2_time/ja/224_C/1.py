def main():
    N = int(input())
    X = []
    Y = []
    for i in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if X[i] == X[j] and X[j] == X[k]:
                    continue
                elif Y[i] == Y[j] and Y[j] == Y[k]:
                    continue
                elif (Y[j] - Y[i])*(X[k] - X[j]) == (Y[k] - Y[j])*(X[j] - X[i]):
                    continue
                else:
                    count += 1
    print(count)

if __name__ == '__main__':
    main()