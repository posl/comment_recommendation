Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def f(x,y):
    if x==0 and y==0:
        return '0'
    if x>0 and y==0:
        return 'R'
    if x<0 and y==0:
        return 'L'
    if x==0 and y>0:
        return 'U'
    if x==0 and y<0:
        return 'D'

    if x>0 and y>0:
        return 'RU'
    if x>0 and y<0:
        return 'RD'
    if x<0 and y>0:
        return 'LU'
    if x<0 and y<0:
        return 'LD'

=======
Suggestion 2

def main():
    return 0

=======
Suggestion 3

def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        tmp = input().split()
        x.append(int(tmp[0]))
        y.append(int(tmp[1]))

    if n==1:
        print(0)
        print('')
        print('')

    elif n==2:
        if x[0]==x[1] or y[0]==y[1]:
            print(1)
            print(1)
            if x[0]<x[1]:
                print('R')
            elif x[0]>x[1]:
                print('L')
            elif y[0]<y[1]:
                print('U')
            elif y[0]>y[1]:
                print('D')
        else:
            print(-1)

    elif n==3:
        if x[0]==x[1]==x[2] or y[0]==y[1]==y[2]:
            print(2)
            print(1,1)
            if x[0]<x[1]:
                print('R')
            elif x[0]>x[1]:
                print('L')
            elif y[0]<y[1]:
                print('U')
            elif y[0]>y[1]:
                print('D')
            for i in range(1,3):
                if x[i]<x[(i+1)%3]:
                    print('R')
                elif x[i]>x[(i+1)%3]:
                    print('L')
                elif y[i]<y[(i+1)%3]:
                    print('U')
                elif y[i]>y[(i+1)%3]:
                    print('D')
        else:
            print(-1)

    else:
        print(-1)

=======
Suggestion 4

def main():
    pass

=======
Suggestion 5

def main():
    N = int(input())
    X = []
    Y = []
    for i in range(N):
        x, y = list(map(int, input().split()))
        X.append(x)
        Y.append(y)

    # print(X)
    # print(Y)

    # 1. 两点之间的距离
    def distance(x1, y1, x2, y2):
        return abs(x1 - x2) + abs(y1 - y2)

    # 2. 两点之间的距离是否为偶数
    def is_even(x1, y1, x2, y2):
        return distance(x1, y1, x2, y2) % 2 == 0

    # 3. 两点之间的距离是否为奇数
    def is_odd(x1, y1, x2, y2):
        return distance(x1, y1, x2, y2) % 2 == 1

    # 4. 两点之间的距离是否为2的倍数
    def is_multiple_of_2(x1, y1, x2, y2):
        return distance(x1, y1, x2, y2) % 2 == 0

    # 5. 两点之间的距离是否为3的倍数
    def is_multiple_of_3(x1, y1, x2, y2):
        return distance(x1, y1, x2, y2) % 3 == 0

    # 6. 两点之间的距离是否为4的倍数
    def is_multiple_of_4(x1, y1, x2, y2):
        return distance(x1, y1, x2, y2) % 4 == 0

    # 7. 两点之间的距离是否为5的倍数
    def is_multiple_of_5(x1, y1, x2, y2):
        return distance(x1, y1, x2, y2) % 5 == 0

    # 8. 两点之间的距离是否为6的倍数
    def is_multiple

=======
Suggestion 6

def solve():
    N = int(input())
    points = []
    for _ in range(N):
        x, y = map(int, input().split())
        points.append((x, y))
    if N == 1:
        print(-1)
        return
    if N == 2:
        print(2)
        print('1 1')
        print('LR')
        print('RL')
        return
    if N == 3:
        print(2)
        print('1 2')
        print('RL')
        print('UU')
        print('DR')
        return
    print(5)
    print('3 1 4 1 5')
    print('LRDUL')
    print('RDULR')
    print('DULRD')
    return

=======
Suggestion 7

def main():
    N = int(input())
    XY = [list(map(int, input().split())) for _ in range(N)]
    XY.sort()
    X = [x for x, _ in XY]
    Y = [y for _, y in XY]
    if N == 1:
        print(-1)
        return
    if N == 2:
        if X[0] == X[1] or Y[0] == Y[1]:
            print(-1)
            return
        print(2)
        print(1, 1)
        print('RL')
        print('UD')
        return
    for i in range(N - 1):
        if X[i] == X[i + 1] or Y[i] == Y[i + 1]:
            print(-1)
            return
    print(N + 1)
    print(1, 1, 4, 1, 5)
    print('R' * (N - 2) + 'LU')
    print('R' * (N - 2) + 'LD')
    print('L' * (N - 2) + 'RU')
    print('L' * (N - 2) + 'RD')
    print('U' * (N - 2) + 'RD')
    print('U' * (N - 2) + 'LD')
    print('D' * (N - 2) + 'RU')
    print('D' * (N - 2) + 'LU')

=======
Suggestion 8

def solve():
    N = int(input())
    X, Y = [0] * N, [0] * N
    for i in range(N):
        X[i], Y[i] = map(int, input().split())
    if N == 1:
        print(0)
        print()
        print()
        return
    if N == 2:
        if X[0] == X[1] or Y[0] == Y[1]:
            print(0)
            print()
            print()
        else:
            print(-1)
        return
    for i in range(N):
        for j in range(i + 1, N):
            if X[i] == X[j] and Y[i] == Y[j]:
                print(-1)
                return
    ans = 100
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                x0, y0 = X[i], Y[i]
                x1, y1 = X[j], Y[j]
                x2, y2 = X[k], Y[k]
                if x0 == x1:
                    if x1 == x2:
                        continue
                    if y0 == y1:
                        continue
                    if y1 == y2:
                        continue
                    if x0 < x1 < x2 or x0 > x1 > x2:
                        continue
                    if y1 < y0 < y2 or y1 > y0 > y2:
                        continue
                    if abs(x1 - x2) + abs(y0 - y1) + abs(y1 - y2) <= ans:
                        ans = abs(x1 - x2) + abs(y0 - y1) + abs(y1 - y2)
                        m = 3
                        d = [abs(x1 - x2), abs(y0 - y1), abs(y1 - y2)]
                        w = ['R', 'U', 'D']
                elif y0 == y1:
                    if y1 == y2:
                        continue
                    if x0 == x1:
                        continue
                    if x1 == x2:
                        continue
                    if x1 < x0 < x2 or x1 > x0 > x2:
                        continue
                    if y0 < y1 < y2 or y0 >
