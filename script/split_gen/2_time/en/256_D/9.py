def main():
    N = int(input())
    LR = []
    for i in range(N):
        LR.append(list(map(int,input().split())))
    LR.sort()
    k = 1
    X = [LR[0][0]]
    Y = [LR[0][1]]
    for i in range(1,N):
        if Y[k-1] >= LR[i][0]:
            if Y[k-1] < LR[i][1]:
                Y[k-1] = LR[i][1]
        else:
            k += 1
            X.append(LR[i][0])
            Y.append(LR[i][1])
    for i in range(k):
        print(X[i],Y[i])
