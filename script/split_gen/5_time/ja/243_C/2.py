def main():
    N = int(input())
    X = []
    Y = []
    S = input()
    for i in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    X1 = []
    Y1 = []
    X2 = []
    Y2 = []
    for i in range(N):
        if S[i] == "R":
            X1.append(X[i])
            Y1.append(Y[i])
        else:
            X2.append(X[i])
            Y2.append(Y[i])
    X1.sort()
    Y1.sort()
    X2.sort()
    Y2.sort()
    if X1[-1] < X2[0] or Y1[-1] < Y2[0] or X2[-1] < X1[0] or Y2[-1] < Y1[0]:
        print("No")
    else:
        print("Yes")
