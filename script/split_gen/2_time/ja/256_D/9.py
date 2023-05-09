def main():
    N = int(input())
    LR = []
    for i in range(N):
        LR.append(list(map(int, input().split())))
    LR.sort()
    X = []
    Y = []
    #print(LR)
    X.append(LR[0][0])
    Y.append(LR[0][1])
    for i in range(1, N):
        if LR[i][0] <= Y[len(Y)-1]:
            Y[len(Y)-1] = max(Y[len(Y)-1], LR[i][1])
        else:
            X.append(LR[i][0])
            Y.append(LR[i][1])
    for i in range(len(X)):
        print(X[i], Y[i])
