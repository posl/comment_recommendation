Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def get_input():
    N = int(input())
    X = []
    Y = []
    for i in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    return N, X, Y

=======
Suggestion 2

def main():
    pass

=======
Suggestion 3

def main():
    n = int(input())
    x = [0] * n
    y = [0] * n
    for i in range(n):
        x[i], y[i] = map(int, input().split())
    if n == 1:
        print(-1)
        return
    for i in range(n):
        for j in range(i + 1, n):
            if x[i] == x[j] and y[i] == y[j]:
                print(2)
                print(1, 1)
                print('UD')
                print('DU')
                return
    if n == 2:
        print(-1)
        return
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if x[i] == x[j] == x[k] or y[i] == y[j] == y[k]:
                    print(3)
                    print(1, 1, 1)
                    print('UDL')
                    print('DUL')
                    print('LUR')
                    return
    if n == 3:
        print(-1)
        return
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                for l in range(k + 1, n):
                    if x[i] == x[j] == x[k] == x[l] or y[i] == y[j] == y[k] == y[l]:
                        print(4)
                        print(1, 1, 1, 1)
                        print('UDLR')
                        print('DULR')
                        print('LURD')
                        print('RDLU')
                        return
    print(5)
    print(1, 1, 1, 1, 1)
    print('UDLRL')
    print('DULRL')
    print('LURDL')
    print('RDLUR')
    print('LRDLU')

main()

=======
Suggestion 4

def get_direction(x, y, x1, y1):
    if x == x1 and y == y1:
        return ""
    if x == x1:
        if y1 > y:
            return "U"
        else:
            return "D"
    elif y == y1:
        if x1 > x:
            return "R"
        else:
            return "L"
    else:
        return ""

=======
Suggestion 5

def main():
    n = int(input())
    points = []
    for i in range(n):
        points.append(list(map(int, input().split())))
    if n == 1:
        print(0)
        print(0)
        print(" ")
        print(" ")
    elif n == 2:
        print(1)
        print(abs(points[1][0] - points[0][0]))
        print("L" if points[1][0] < points[0][0] else "R")
        print(" ")
    else:
        print(2)
        print(abs(points[1][0] - points[0][0]))
        print("L" if points[1][0] < points[0][0] else "R")
        print("U" if points[1][1] < points[0][1] else "D")
        print(" ")

=======
Suggestion 6

def solve():
    pass

=======
Suggestion 7

def func():
    N = int(input())
    X = []
    Y = []
    for i in range(N):
        a, b = map(int, input().split())
        X.append(a)
        Y.append(b)
    print(X)
    print(Y)
    if N == 1:
        print(1)
        print(1)
        print('U')
        return
    if N == 2:
        if X[0] == X[1]:
            print(2)
            print(1, 1)
            print('RU')
            print('UR')
            return
        elif Y[0] == Y[1]:
            print(2)
            print(1, 1)
            print('UR')
            print('RU')
            return
        else:
            print(-1)
            return
    if N == 3:
        if X[0] == X[1] == X[2]:
            print(2)
            print(1, 1)
            print('RUU')
            print('URD')
            return
        elif Y[0] == Y[1] == Y[2]:
            print(2)
            print(1, 1)
            print('URR')
            print('RUL')
            return
        else:
            print(-1)
            return
    if N >= 4:
        if X[0] == X[1] == X[2] == X[3]:
            print(2)
            print(1, 1)
            print('RUUU')
            print('URDD')
            for i in range(4, N):
                if X[i] != X[0]:
                    print('R'*(i-3)+'U'+'R'*(N-1-i)+'D')
                    return
            return
        elif Y[0] == Y[1] == Y[2] == Y[3]:
            print(2)
            print(1, 1)
            print('URRR')
            print('RULL')
            for i in range(4, N):
                if Y[i] != Y[0]:
                    print('U'*(i-3)+'R'+'U'*(N-1-i)+'L')
                    return
            return
        else:
            print(-1)
            return
