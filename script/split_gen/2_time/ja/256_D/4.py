def main():
    N = int(input())
    LR = []
    for _ in range(N):
        LR.append(list(map(int, input().split())))
    LR.sort()
    X = LR[0][0]
    Y = LR[0][1]
    for i in range(1, N):
        if LR[i][0] <= Y:
            Y = max(Y, LR[i][1])
        else:
            print(X, Y)
            X = LR[i][0]
            Y = LR[i][1]
    print(X, Y)
