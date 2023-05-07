def main():
    N = int(input())
    X = []
    Y = []
    for i in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    X = sorted(X)
    Y = sorted(Y)
    if N == 1:
        print(1)
        return
    if N == 2:
        if X[0] == X[1] or Y[0] == Y[1]:
            print(1)
        else:
            print(2)
        return
    if N == 3:
        if (X[0] == X[1] and X[1] == X[2]) or (Y[0] == Y[1] and Y[1] == Y[2]):
            print(1)
        elif (X[0] == X[1] and Y[1] == Y[2]) or (X[1] == X[2] and Y[0] == Y[1]):
            print(1)
        elif (X[0] == X[2] and Y[0] == Y[1]) or (X[0] == X[1] and Y[1] == Y[2]):
            print(1)
        elif (X[0] == X[1] and X[2] == X[0]+2) or (Y[0] == Y[1] and Y[2] == Y[0]+2):
            print(2)
        elif (X[1] == X[2] and X[0] == X[1]-2) or (Y[1] == Y[2] and Y[0] == Y[1]-2):
            print(2)
        elif (X[0] == X[1] and X[2] == X[0]+1) or (Y[0] == Y[1] and Y[2] == Y[0]+1):
            print(2)
        elif (X[1] == X[2] and X[0] == X[1]-1) or (Y[1] == Y[2] and Y[0] == Y[1]-1):
            print(2)
        else:
            print(3)
        return
    if N == 4:
        if (X[0]
