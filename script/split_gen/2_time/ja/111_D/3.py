def main():
    N = int(input())
    X = []
    Y = []
    for _ in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    if N == 1:
        print(0)
        return
    if N == 2:
        if X[0] != X[1] and Y[0] != Y[1]:
            print(2)
            print(1, 1)
            print('RU' if X[0] < X[1] else 'DR')
            print('UR' if X[0] < X[1] else 'LD')
        else:
            print(1)
            print(1)
            print('R' if X[0] < X[1] else 'L')
        return
    if N == 3:
        if X[0] != X[1] and Y[0] != Y[1] and X[1] != X[2] and Y[1] != Y[2]:
            print(2)
            print(1, 1)
            print('RU' if X[0] < X[1] else 'DR')
            print('UR' if X[0] < X[1] else 'LD')
        else:
            print(1)
            print(1)
            print('R' if X[0] < X[1] else 'L')
        return
    if N == 4:
        if X[0] != X[1] and Y[0] != Y[1] and X[1] != X[2] and Y[1] != Y[2] and X[2] != X[3] and Y[2] != Y[3]:
            print(2)
            print(1, 1)
            print('RU' if X[0] < X[1] else 'DR')
            print('UR' if X[0] < X[1] else 'LD')
        else:
            print(1)
            print(1)
            print('R' if X[0] < X[1] else 'L')
        return
    if N == 5:
        if X[0] != X[1] and Y[0] != Y[1] and X[1] != X[2]
