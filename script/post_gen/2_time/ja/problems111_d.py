Synthesizing 10/10 solutions

=======
Suggestion 1

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

=======
Suggestion 2

def main():
    N = int(input())
    X = []
    Y = []
    for i in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    if N == 1:
        print(2)
        print(1, 1)
        print('RU')
        return
    if N == 2:
        if X[0] == X[1] and Y[0] == Y[1]:
            print(2)
            print(1, 1)
            print('RU')
            print('UR')
            return
        else:
            print(-1)
            return
    if N == 3:
        if X[0] == X[1] and X[1] == X[2] and Y[0] == Y[1] and Y[1] == Y[2]:
            print(2)
            print(1, 1)
            print('RU')
            print('UR')
            print('RU')
            return
        else:
            print(-1)
            return
    if N == 4:
        if X[0] == X[1] and X[1] == X[2] and X[2] == X[3] and Y[0] == Y[1] and Y[1] == Y[2] and Y[2] == Y[3]:
            print(2)
            print(1, 1)
            print('RU')
            print('UR')
            print('RU')
            print('UR')
            return
        else:
            print(-1)
            return
    if N == 5:
        if X[0] == X[1] and X[1] == X[2] and X[2] == X[3] and X[3] == X[4] and Y[0] == Y[1] and Y[1] == Y[2] and Y[2] == Y[3] and Y[3] == Y[4]:
            print(2)
            print(1, 1)
            print('RU')
            print('UR')
            print('RU')
            print('UR')
            print('RU')
            return
        else:
            print(-1)
            return
    if N == 6:
        if X[0] == X[1

=======
Suggestion 3

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
    if N == 2:
        if X[0] == X[1] and Y[0] == Y[1]:
            print(1)
            print(1)
            print('R')
            print('L')
        else:
            print(-1)
        return
    d = []
    for i in range(N - 1):
        d.append(abs(X[i] - X[i + 1]) + abs(Y[i] - Y[i + 1]))
    if d[0] != d[1] or d[1] != d[2]:
        print(-1)
        return
    m = 0
    for i in range(N - 1):
        m = max(m, abs(X[i] - X[i + 1]))
        m = max(m, abs(Y[i] - Y[i + 1]))
    print(m)
    print(*d)
    for i in range(N):
        s = ''
        for j in range(m):
            if X[i] > 0:
                X[i] -= 1
                s += 'R'
            elif X[i] < 0:
                X[i] += 1
                s += 'L'
            elif Y[i] > 0:
                Y[i] -= 1
                s += 'U'
            else:
                Y[i] += 1
                s += 'D'
        print(s)

=======
Suggestion 4

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

=======
Suggestion 5

def solve():
    N = int(input())
    X = [0] * N
    Y = [0] * N
    for i in range(N):
        X[i], Y[i] = map(int, input().split())
    if N == 1:
        print(2)
        print(1, 1)
        print("RU")
        print("UR")
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
    # N >= 3
    m = 40
    d = [1] * m
    for i in range(1, m):
        d[i] = d[i-1] * 2
    w = [""] * N
    for i in range(N):
        if X[i] < 0:
            w[i] += "L" * abs(X[i])
        else:
            w[i] += "R" * abs(X[i])
        if Y[i] < 0:
            w[i] += "D" * abs(Y[i])
        else:
            w[i] += "U" * abs(Y[i])
    print(m)
    print(*d)
    for i in range(N):
        print(w[i])

=======
Suggestion 6

def main():
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]

    if N == 1:
        print(2)
        print(1, 1)
        print('RU')
        print('UR')
        return

    if N == 2:
        if sum(XY[0]) == sum(XY[1]):
            print(2)
            print(1, 1)
            print('RU')
            print('UR')
        else:
            print(-1)
        return

    if N == 3:
        if sum(XY[0]) == sum(XY[1]) == sum(XY[2]):
            print(2)
            print(1, 1)
            print('RU')
            print('UR')
        else:
            print(-1)
        return

    if N == 4:
        if sum(XY[0]) == sum(XY[1]) == sum(XY[2]) == sum(XY[3]):
            print(2)
            print(1, 1)
            print('RU')
            print('UR')
        else:
            print(-1)
        return

    if N == 5:
        if sum(XY[0]) == sum(XY[1]) == sum(XY[2]) == sum(XY[3]) == sum(XY[4]):
            print(2)
            print(1, 1)
            print('RU')
            print('UR')
        else:
            print(-1)
        return

    print(-1)

=======
Suggestion 7

def main():
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]
    if N == 1:
        print(1)
        print(1)
        print('R')
        return
    if N == 2:
        if XY[0] == XY[1]:
            print(2)
            print(1, 1)
            print('RU')
            print('UR')
            return
        else:
            print(-1)
            return
    if N == 3:
        if XY[0] == XY[1] == XY[2]:
            print(3)
            print(1, 1, 1)
            print('RUU')
            print('URU')
            print('UUR')
            return
        else:
            print(-1)
            return
    if N == 4:
        if XY[0] == XY[1] == XY[2] == XY[3]:
            print(4)
            print(1, 1, 1, 1)
            print('RUUU')
            print('URUU')
            print('UURU')
            print('UUUR')
            return
        else:
            print(-1)
            return
    if N == 5:
        if XY[0] == XY[1] == XY[2] == XY[3] == XY[4]:
            print(5)
            print(1, 1, 1, 1, 1)
            print('RUUUU')
            print('URUUU')
            print('UURUU')
            print('UUURU')
            print('UUUUR')
            return
        else:
            print(-1)
            return
    if N == 6:
        if XY[0] == XY[1] == XY[2] == XY[3] == XY[4] == XY[5]:
            print(6)
            print(1, 1, 1, 1, 1, 1)
            print('RUUUUU')
            print('URUUUU')
            print('UURUUU')
            print('UUURUU')
            print('UUUURU')
            print('UUUUUR')
            return
        else:
            print(-1)
            return
    if N == 7:
        if XY[0

=======
Suggestion 8

def main():
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]
    if N == 1:
        print(1)
        print(1)
        print('R')
        return
    if N == 2:
        if XY[0] == XY[1]:
            print(2)
            print(1, 1)
            print('RU')
            print('UR')
            return
        d = max(abs(XY[0][0] - XY[1][0]), abs(XY[0][1] - XY[1][1]))
        print(2)
        print(d, d)
        print('RU')
        print('UR')
        return
    d = max(abs(XY[0][0] - XY[1][0]), abs(XY[0][1] - XY[1][1]))
    for i in range(2, N):
        d = max(d, abs(XY[0][0] - XY[i][0]), abs(XY[0][1] - XY[i][1]))
    print(2)
    print(d, d)
    print('RU')
    print('UR')

=======
Suggestion 9

def main():
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]

    if N == 1:
        print(1)
        print(1)
        print(1)
        return

    if N == 2:
        if XY[0] == XY[1]:
            print(2)
            print(1, 1)
            print('RU')
            print('UR')
            return
        else:
            print(-1)
            return

    # N >= 3
    m = 40
    d = [1] + [2 ** i for i in range(1, m)]
    w = [''] * N
    for i in range(N):
        for j in range(m):
            if XY[i][0] & (1 << j):
                w[i] += 'R'
            else:
                w[i] += 'L'
            if XY[i][1] & (1 << j):
                w[i] += 'U'
            else:
                w[i] += 'D'

    print(m)
    print(*d)
    for wi in w:
        print(wi)

=======
Suggestion 10

def main():
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]
    if N == 1:
        print(0)
    elif N == 2:
        if XY[0][0] == XY[1][0] or XY[0][1] == XY[1][1]:
            print(1)
            print(abs(XY[0][0] - XY[1][0]) + abs(XY[0][1] - XY[1][1]))
            print(''.join(['R' if XY[0][0] < XY[1][0] else 'L' if XY[0][0] > XY[1][0] else '',
                           'U' if XY[0][1] < XY[1][1] else 'D' if XY[0][1] > XY[1][1] else '']))
            print(''.join(['R' if XY[0][0] > XY[1][0] else 'L' if XY[0][0] < XY[1][0] else '',
                           'U' if XY[0][1] > XY[1][1] else 'D' if XY[0][1] < XY[1][1] else '']))
        else:
            print(2)
            print(abs(XY[0][0] - XY[1][0]), abs(XY[0][1] - XY[1][1]))
            print(''.join(['R' if XY[0][0] < XY[1][0] else 'L' if XY[0][0] > XY[1][0] else '',
                           'U' if XY[0][1] < XY[1][1] else 'D' if XY[0][1] > XY[1][1] else '']))
            print(''.join(['R' if XY[0][0] > XY[1][0] else 'L' if XY[0][0] < XY[1][0] else '',
                           'U' if XY[0][1] > XY[1][1] else 'D' if XY[0][1] < XY[1][1] else '']))
    else:
        if XY[0][0] == XY[1][0] or XY[0][1
