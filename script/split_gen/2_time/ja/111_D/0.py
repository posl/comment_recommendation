def main():
    N = int(input())
    X = []
    Y = []
    for i in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    if N == 1:
        print(1)
        print(1, 1)
        print("R")
        return
    if N == 2:
        if X[0] == X[1] and Y[0] == Y[1]:
            print(2)
            print(1, 1)
            print("RU")
            print("UR")
            return
        else:
            print(-1)
            return
    if N == 3:
        if X[0] == X[1] and Y[0] == Y[1]:
            if X[1] == X[2] and Y[1] == Y[2]:
                print(2)
                print(1, 1)
                print("RU")
                print("UR")
                return
            else:
                print(-1)
                return
        else:
            if X[1] == X[2] and Y[1] == Y[2]:
                print(-1)
                return
            else:
                if X[0] == X[1] and X[1] == X[2]:
                    print(2)
                    print(1, 1)
                    print("RU")
                    print("UR")
                    return
                elif Y[0] == Y[1] and Y[1] == Y[2]:
                    print(2)
                    print(1, 1)
                    print("RU")
                    print("UR")
                    return
                elif (X[0] - X[1]) == (X[1] - X[2]) and (Y[0] - Y[1]) == (Y[1] - Y[2]):
                    print(2)
                    print(1, 1)
                    print("RU")
                    print("UR")
                    return
                else:
                    print(-1)
                    return
    if N == 4:
        if X[0] == X[1] and Y[0] == Y[1]:
            if X[1] == X[2] and Y[1] == Y[2]:
                if X[2] == X[3] and Y[2]
