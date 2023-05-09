def main():
    N = int(input())
    LR = [list(map(int, input().split())) for _ in range(N)]
    LR.sort()
    X = []
    Y = []
    i = 0
    while i < N:
        j = i
        while j < N-1 and LR[j][1] >= LR[j+1][0]:
            j += 1
        X.append(LR[i][0])
        Y.append(LR[j][1])
        i = j + 1
    print(len(X))
    for i in range(len(X)):
        print(X[i], Y[i])
