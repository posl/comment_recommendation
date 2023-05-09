def main():
    N = int(input())
    LR = [list(map(int, input().split())) for _ in range(N)]
    LR.sort(key=lambda x: x[0])
    X = []
    Y = []
    for i in range(N):
        if len(X) == 0:
            X.append(LR[i][0])
            Y.append(LR[i][1])
        else:
            if LR[i][0] <= Y[-1]:
                Y[-1] = max(LR[i][1], Y[-1])
            else:
                X.append(LR[i][0])
                Y.append(LR[i][1])
    for i in range(len(X)):
        print(X[i], Y[i])

if __name__ == '__main__':
    main()