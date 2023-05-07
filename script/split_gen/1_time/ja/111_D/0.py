def main():
    N = int(input())
    X = []
    Y = []
    for i in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    if N == 1:
        print(0)
        return
    elif N == 2:
        if X[0] == X[1] and Y[0] == Y[1]:
            print(1)
            print(0)
            print('R')
            print('L')
            return
        else:
            print(-1)
            return
    elif N == 3:
        if X[0] == X[1] and Y[0] == Y[1]:
            if X[1] == X[2] and Y[1] == Y[2]:
                print(2)
                print(0, 0)
                print('R')
                print('L')
                print('R')
                return
            else:
                print(-1)
                return
        else:
            print(-1)
            return
    else:
        if X[0] == X[1] and Y[0] == Y[1]:
            if X[1] == X[2] and Y[1] == Y[2]:
                if X[2] == X[3] and Y[2] == Y[3]:
                    print(3)
                    print(0, 0, 0)
                    print('R')
                    print('L')
                    print('R')
                    print('L')
                    return
                else:
                    print(-1)
                    return
            else:
                print(-1)
                return
        else:
            print(-1)
            return
