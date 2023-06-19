Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solve():
    #输入
    N = int(input())
    X = []
    Y = []
    for i in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)

    #确定机械臂的长度
    m = 1
    wh

=======
Suggestion 2

def findD(x,y):
    return y

=======
Suggestion 3

def main():
    pass

=======
Suggestion 4

def get_input():
    N = int(input())
    XY = []
    for _ in range(N):
        x, y = map(int, input().split())
        XY.append((x, y))
    return N, XY

=======
Suggestion 5

def solve():
    pass

=======
Suggestion 6

def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        a,b = map(int,input().split())
        x.append(a)
        y.append(b)
    #print(x)
    #print(y)
    if n == 1:
        print(0)
        print(1)
        print("U")
        return
    if n == 2:
        if x[0] == x[1] and y[0] == y[1]:
            print(0)
            print(1)
            print("U")
            return
        else:
            print(-1)
            return
    if n == 3:
        if x[0] == x[1] and x[1] == x[2]:
            if y[0] < y[1] and y[1] < y[2]:
                print(2)
                print(1,1)
                print("UD")
                print("UD")
                print("UD")
                return
            elif y[0] > y[1] and y[1] > y[2]:
                print(2)
                print(1,1)
                print("DU")
                print("DU")
                print("DU")
                return
            else:
                print(-1)
                return
        elif y[0] == y[1] and y[1] == y[2]:
            if x[0] < x[1] and x[1] < x[2]:
                print(2)
                print(1,1)
                print("RL")
                print("RL")
                print("RL")
                return
            elif x[0] > x[1] and x[1] > x[2]:
                print(2)
                print(1,1)
                print("LR")
                print("LR")
                print("LR")
                return
            else:
                print(-1)
                return
        else:
            print(-1)
            return
    if n == 4:
        if x[0] == x[1] and x[1] == x[2] and x[2] == x[3]:
            if y[0] < y[1] and y[1] < y[2] and y[2] < y[3]:
                print(2)
                print(1,

=======
Suggestion 7

def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        x1, y1 = map(int, input().split())
        x.append(x1)
        y.append(y1)
    #print(x)
    #print(y)
    #print("----------")
    #print(x[0])
    #print(y[0])
    #print("----------")
    #print(x[1])
    #print(y[1])
    #print("----------")
    #print(x[2])
    #print(y[2])
    #print("----------")
    #print(x[0], y[0])
    #print(x[1], y[1])
    #print(x[2], y[2])
    #print("----------")
    #print(x[0], y[0])
    #print(x[1], y[1])
    #print(x[2], y[2])
    #print("----------")
    #print(x[0], y[0])
    #print(x[1], y[1])
    #print(x[2], y[2])
    #print("----------")
    #print(x[0], y[0])
    #print(x[1], y[1])
    #print(x[2], y[2])
    #print("----------")
    #print(x[0], y[0])
    #print(x[1], y[1])
    #print(x[2], y[2])
    #print("----------")
    #print(x[0], y[0])
    #print(x[1], y[1])
    #print(x[2], y[2])
    #print("----------")
    #print(x[0], y[0])
    #print(x[1], y[1])
    #print(x[2], y[2])
    #print("----------")
    #print(x[0], y[0])
    #print(x[1], y[1])
    #print(x[2], y[2])
    #print("----------")

    m = 0
    d = []
    w = []
    for i in range(n):
        d.append(0)
        w.append("")
    #print(d)
    #print(w)
    #print("----------")
    #print(d[0])
    #print(w[0])
    #

=======
Suggestion 8

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
        print(0)
        print("U")
        return

    for m in range(1, 41):
        for i in range(1, N):
            if abs(X[i] - X[i-1]) + abs(Y[i] - Y[i-1]) != m:
                break
        else:
            break
    else:
        print(-1)
        return

    print(m)
    d = [abs(X[i] - X[i-1]) + abs(Y[i] - Y[i-1]) for i in range(1, N)]
    print(" ".join(map(str, d)))
    for x, y in zip(X[1:], Y[1:]):
        s = ""
        if x > X[0]:
            s += "R" * (x - X[0])
        elif x < X[0]:
            s += "L" * (X[0] - x)

        if y > Y[0]:
            s += "U" * (y - Y[0])
        elif y < Y[0]:
            s += "D" * (Y[0] - y)

        print(s)

=======
Suggestion 9

def f():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        temp = input().split()
        x.append(int(temp[0]))
        y.append(int(temp[1]))
    if n == 1:
        print(-1)
        return
    if n == 2:
        if x[0] == x[1] and y[0] == y[1]:
            print(-1)
            return
        else:
            print(2)
            print(1, 1)
            print('LR')
            print('RL')
            return
    if n == 3:
        if x[0] == x[1] and x[1] == x[2]:
            print(2)
            print(1, 1)
            print('UDL')
            print('LDR')
            print('RUR')
            return
        if y[0] == y[1] and y[1] == y[2]:
            print(2)
            print(1, 1)
            print('LDR')
            print('RUR')
            print('UDL')
            return
        print(-1)
        return
    print(5)
    print(3, 1, 4, 1, 5)
    print('LRDUL')
    print('RDULR')
    print('DULRD')
    print('ULRDL')
    print('RDLRU')
    return

f()
