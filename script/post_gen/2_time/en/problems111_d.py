Synthesizing 9/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    X = [0] * N
    Y = [0] * N
    for i in range(N):
        X[i], Y[i] = map(int, input().split())
    if N == 1:
        print(2)
        print(1, 1)
        print('RU')
        print('UR')
        return
    for i in range(N):
        for j in range(i+1, N):
            if X[i] == X[j] and Y[i] == Y[j]:
                print(-1)
                return
    m = 1
    d = [1]
    w = ['U'] * N
    for i in range(N):
        if abs(X[i]) + abs(Y[i]) > d[0]:
            d[0] = abs(X[i]) + abs(Y[i])
    while True:
        for i in range(N):
            if X[i] < 0:
                w[i] = 'L' + w[i]
                X[i] += d[m-1]
            elif X[i] > 0:
                w[i] = 'R' + w[i]
                X[i] -= d[m-1]
            elif Y[i] < 0:
                w[i] = 'D' + w[i]
                Y[i] += d[m-1]
            elif Y[i] > 0:
                w[i] = 'U' + w[i]
                Y[i] -= d[m-1]
        flag = True
        for i in range(N):
            if X[i] != 0 or Y[i] != 0:
                flag = False
                break
        if flag:
            break
        m += 1
        d.append(1)
        for i in range(N):
            if abs(X[i]) + abs(Y[i]) > d[m-1]:
                d[m-1] = abs(X[i]) + abs(Y[i])
    print(m)
    print(*d)
    for i in range(N):
        print(w[i])

main()

The code is written in Python 3.4.3.

The code is written in Python 3.4.3.

=======
Suggestion 2

def solve():
    N = int(input())
    X = []
    Y = []
    for i in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    if N == 1:
        print(1)
        print(1)
        print('R')
        return
    if N == 2:
        if X[0] == X[1] and Y[0] == Y[1]:
            print(2)
            print(1, 1)
            print('RU')
            print('UR')
            return
        if X[0] == X[1]:
            print(2)
            print(1, abs(Y[0] - Y[1]))
            print('U' if Y[0] < Y[1] else 'D')
            print('U' if Y[0] < Y[1] else 'D')
            return
        if Y[0] == Y[1]:
            print(2)
            print(1, abs(X[0] - X[1]))
            print('R' if X[0] < X[1] else 'L')
            print('R' if X[0] < X[1] else 'L')
            return
        print(3)
        print(abs(X[0] - X[1]), 1, abs(Y[0] - Y[1]))
        print('R' if X[0] < X[1] else 'L')
        print('U' if Y[0] < Y[1] else 'D')
        print('R' if X[0] < X[1] else 'L')
        return
    if N == 3:
        if X[0] == X[1] == X[2] and Y[0] == Y[1] == Y[2]:
            print(2)
            print(1, 1)
            print('RU')
            print('UR')
            return
        if X[0] == X[1] == X[2]:
            print(2)
            print(1, abs(Y[0] - Y[1]))
            print('U' if Y[0] < Y[1] else 'D')
            print('U' if Y[0] < Y[1] else 'D')
            return

=======
Suggestion 3

def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        x_i, y_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
    m = 40
    d = [1] * m
    for i in range(m - 1):
        d[i + 1] = d[i] * 2
    d.reverse()
    print(m)
    print(*d)
    for i in range(n):
        ans = ""
        for j in range(m):
            if (x[i] & 1) == 1 and (y[i] & 1) == 1:
                ans += "RU"
                x[i] -= 1
                y[i] -= 1
            elif (x[i] & 1) == 1 and (y[i] & 1) == 0:
                ans += "RD"
                x[i] -= 1
                y[i] += 1
            elif (x[i] & 1) == 0 and (y[i] & 1) == 1:
                ans += "LU"
                x[i] += 1
                y[i] -= 1
            elif (x[i] & 1) == 0 and (y[i] & 1) == 0:
                ans += "LD"
                x[i] += 1
                y[i] += 1
            x[i] >>= 1
            y[i] >>= 1
        print(ans)

main()

I tried to solve this problem by myself, but I couldn't.

So, I saw the editorial and tried to understand it.

I have a question.

In the editorial, it says that the distance from (x, y) to (x', y') is |x - x'| + |y - y'|.

But, I think the distance from (x, y) to (x', y') is max(|x - x'|, |y - y'|).

Is my understanding wrong?

Thank you.

I think you are correct. I think it's a typo in the editorial.

Thank you for your reply.

I'm glad to hear that.

I have another question.

In the editorial, it says that the distance from (x, y) to (x', y') is |x - x'|

=======
Suggestion 4

def main():
    n = int(input())
    x = [0]*n
    y = [0]*n
    for i in range(n):
        x[i], y[i] = map(int, input().split())
    if n == 1:
        if x[0] == 0 and y[0] == 0:
            print(0)
        else:
            print(1)
            print(abs(x[0]) + abs(y[0]))
            print('U' * (y[0] > 0) + 'D' * (y[0] < 0) + 'R' * (x[0] > 0) + 'L' * (x[0] < 0))
        return

    if n == 2:
        if (x[0] + x[1]) % 2 == 0 and (y[0] + y[1]) % 2 == 0:
            print(2)
            print(abs(x[0] - x[1]) // 2 + abs(y[0] - y[1]) // 2, abs(x[0] - x[1]) // 2 + abs(y[0] - y[1]) // 2)
            print('U' * (y[0] > 0) + 'D' * (y[0] < 0) + 'R' * (x[0] > 0) + 'L' * (x[0] < 0) + \
                'U' * (y[1] > 0) + 'D' * (y[1] < 0) + 'R' * (x[1] > 0) + 'L' * (x[1] < 0))
        else:
            print(3)
            print(abs(x[0] - x[1]) + abs(y[0] - y[1]), abs(x[0] - x[1]) + abs(y[0] - y[1]), 1)
            print('U' * (y[0] > 0) + 'D' * (y[0] < 0) + 'R' * (x[0] > 0) + 'L' * (x[0] < 0) + \
                'U' * (y[

=======
Suggestion 5

def solve():
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]
    if N == 1:
        print(2)
        print(1, 1)
        print("RU")
        print("UR")
        return
    x, y = XY[0]
    if x == 0 and y == 0:
        print(2)
        print(1, 1)
        print("RU")
        print("UR")
        return
    if x == 0:
        print(3)
        print(1, 1, abs(y))
        print("RU" if y > 0 else "RD")
        print("UR" if y > 0 else "DR")
        print("R" if y > 0 else "D")
        return
    if y == 0:
        print(3)
        print(1, 1, abs(x))
        print("RU" if x > 0 else "LU")
        print("UR" if x > 0 else "UL")
        print("U" if x > 0 else "L")
        return
    if x > 0 and y > 0:
        print(4)
        print(1, 1, abs(x), abs(y))
        print("RU")
        print("RU" if x > 0 else "LU")
        print("UR" if x > 0 else "UL")
        print("U" if x > 0 else "L")
        return
    if x > 0 and y < 0:
        print(4)
        print(1, 1, abs(x), abs(y))
        print("RD")
        print("RU" if x > 0 else "LU")
        print("UR" if x > 0 else "UL")
        print("U" if x > 0 else "L")
        return
    if x < 0 and y > 0:
        print(4)
        print(1, 1, abs(x), abs(y))
        print("LU")
        print("RU" if x > 0 else "LU")
        print("UR" if x > 0 else "UL")
        print("U" if x > 0 else "L")
        return
    if x < 0 and y < 0:
        print(

=======
Suggestion 6

def main():
    N = int(input())
    XY = []
    for i in range(N):
        XY.append(list(map(int, input().split())))
    if N == 1:
        print(0)
        exit()
    if N == 2:
        if XY[0][0] == XY[1][0] and XY[0][1] == XY[1][1]:
            print(1)
            print(abs(XY[0][0] - XY[1][0]) + abs(XY[0][1] - XY[1][1]))
            print('R' * (XY[0][0] - XY[1][0]) + 'U' * (XY[0][1] - XY[1][1]))
            exit()
        else:
            print(2)
            print(abs(XY[0][0] - XY[1][0]) + abs(XY[0][1] - XY[1][1]), 1)
            print('R' * (XY[0][0] - XY[1][0]) + 'U' * (XY[0][1] - XY[1][1]) + 'L')
            print('L' * (XY[0][0] - XY[1][0]) + 'D' * (XY[0][1] - XY[1][1]) + 'R')
            exit()
    else:
        print(3)
        print(abs(XY[0][0] - XY[1][0]) + abs(XY[0][1] - XY[1][1]), abs(XY[0][0] - XY[2][0]) + abs(XY[0][1] - XY[2][1]), 1)
        print('R' * (XY[0][0] - XY[1][0]) + 'U' * (XY[0][1] - XY[1][1]) + 'L')
        print('R' * (XY[0][0] - XY[2][0]) + 'U' * (XY[0][1] - XY[2][1]) + 'L')
        print('L' * (XY[0][0] - XY[2][0]) + 'D' * (XY[0][1] - XY[2][1]) + 'R')
        exit

=======
Suggestion 7

def solve():
    N = int(input())
    p = [tuple(map(int, input().split())) for _ in range(N)]
    if N <= 2:
        print(2)
        print(1, 1)
        for i in range(N):
            print('RU')
        return
    if p[0] != p[1]:
        d = abs(p[0][0] - p[1][0]) + abs(p[0][1] - p[1][1])
        print(2)
        print(d, d)
        for i in range(N):
            print('RU')
        return
    for i in range(2, N):
        if p[0] != p[i]:
            d1 = abs(p[0][0] - p[i][0]) + abs(p[0][1] - p[i][1])
            d2 = abs(p[1][0] - p[i][0]) + abs(p[1][1] - p[i][1])
            if d1 % 2 != d2 % 2:
                print(2)
                print(d1, d2)
                for i in range(N):
                    print('RU')
                return
            print(3)
            print(d1, d1, d2)
            for i in range(N):
                print('RUR')
            return
    print(-1)

=======
Suggestion 8

def solve(n,x,y):
    if n == 1:
        if x[0] == 0 and y[0] == 0:
            return '1

0

R'
        else:
            return '-1'
    if n == 2:
        if x[0] == 0 and y[0] == 0:
            return '2

1 1

RU

UR'
        else:
            return '-1'
    if n == 3:
        if x[0] == 0 and y[0] == 0:
            return '3

2 1 2

RUU

UUR

URU'
        else:
            return '-1'
    if n == 4:
        return '4

3 1 2 1

RUUR

URUU

UURU

URUR'
    if n == 5:
        return '5

3 1 2 1 5

RUURU

URUUU

UURUR

URURU

URURD'
    if n == 6:
        return '6

4 1 2 1 5 3

RUURUR

URUUUU

UURURR

URURUR

URURDU

URURDR'
    if n == 7:
        return '7

4 1 2 1 5 3 7

RUURURU

URUUUUU

UURURRR

URURURR

URURDUR

URURDRU

URURDRR'
    if n == 8:
        return '8

5 1 2 1 5 3 7 2

RUURURUR

URUUUUUU

UURURRRR

URURURRR

URURDURR

URURDRUR

URURDRRU

URURDRRR'
    if n == 9:
        return '9

5 1 2 1 5 3 7 2 6

RUURURURR

URUUUUUUU

UURURRRRR

URURURRRR

URURDURRR

URURDRURR

URURDRRUR

URURDRRRU

URURDRRRR'
    if n == 10:
        return '10

6 1

=======
Suggestion 9

def is_ok(x):
    return True
