Synthesizing 10/10 solutions

=======
Suggestion 1

def get_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

=======
Suggestion 2

def solve():
    n = int(input())
    x = []
    y = []
    p = []
    for i in range(n):
        x_i, y_i, p_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
        p.append(p_i)
    print(n)

=======
Suggestion 3

def get_input():
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(input().split(' '))
    return n, arr

=======
Suggestion 4

def solve():
    N = int(input())
    xyp = []
    for i in range(N):
        xyp.append(list(map(int, input().split())))
    #print(xyp)
    xyp.sort(key=lambda x: x[2])
    #print(xyp)
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if xyp[i][2] * ans >= abs(xyp[i][0] - xyp[j][0]) + abs(xyp[i][1] - xyp[j][1]):
                ans += 1
                break
    print(ans)

=======
Suggestion 5

def main():
    pass

=======
Suggestion 6

def getMinJumpCount():
    return 0

=======
Suggestion 7

def main():
    N = int(input())
    x = []
    y = []
    P = []
    for i in range(N):
        x_i, y_i, P_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
        P.append(P_i)
    print(N)
    print(x)
    print(y)
    print(P)

=======
Suggestion 8

def main():
    N = int(input())
    pos = []
    for i in range(N):
        x, y, p = map(int, input().split())
        pos.append([x, y, p])

    # print(pos)

    # 计算两点之间的距离
    def distance(x1, y1, x2, y2):
        return abs(x1 - x2) + abs(y1 - y2)

    # 计算两点之间的距离是否可以跳跃
    def can_jump(x1, y1, p1, x2, y2):
        return p1 >= distance(x1, y1, x2, y2)

    # 计算两点之间的距离是否可以跳跃
    def can_jump2(x1, y1, p1, x2, y2, p2):
        return p1 * p2 >= distance(x1, y1, x2, y2)

    # 计算两点之间的距离是否可以跳跃
    def can_jump3(x1, y1, p1, x2, y2, p2):
        return p1 * p2 >= distance(x1, y1, x2, y2) * distance(x1, y1, x2, y2)

    # 计算两点之间的距离是否可以跳跃
    def can_jump4(x1, y1, p1, x2, y2, p2):
        return p1 * p2 * p2 >= distance(x1, y1, x2, y2) * distance(x1, y1, x2, y2)

    # 计算两点之间的距离是否可以跳跃
    def can_jump5(x1, y1, p1, x2, y2, p2):
        return p1 * p2 * p2 >= distance(x1, y1, x2, y2) * distance(x1, y1, x2, y2) * distance(x1, y1, x2, y2)

    # 计算两点之间的距离是否可以跳跃
    def can_jump

=======
Suggestion 9

def main():
    N = int(input())
    X = []
    Y = []
    P = []
    for i in range(N):
        x,y,p = map(int,input().split())
        X.append(x)
        Y.append(y)
        P.append(p)
    #print(X)
    #print(Y)
    #print(P)
    #print(N)

    #print(X[0])
    #print(Y[0])
    #print(P[0])

    #print(X[1])
    #print(Y[1])
    #print(P[1])

    #print(X[2])
    #print(Y[2])
    #print(P[2])

    #print(X[3])
    #print(Y[3])
    #print(P[3])

    #print(X[4])
    #print(Y[4])
    #print(P[4])

    #print(X[5])
    #print(Y[5])
    #print(P[5])

    #print(X[6])
    #print(Y[6])
    #print(P[6])

    #print(X[7])
    #print(Y[7])
    #print(P[7])

    #print(X[8])
    #print(Y[8])
    #print(P[8])

    #print(X[9])
    #print(Y[9])
    #print(P[9])

    #print(X[10])
    #print(Y[10])
    #print(P[10])

    #print(X[11])
    #print(Y[11])
    #print(P[11])

    #print(X[12])
    #print(Y[12])
    #print(P[12])

    #print(X[13])
    #print(Y[13])
    #print(P[13])

    #print(X[14])
    #print(Y[14])
    #print(P[14])

    #print(X[15])
    #print(Y[15])
    #print(P[15])

    #print(X[16])
    #print(Y[16])
    #print(P[16])

    #print(X[17])
    #print(Y[17])
    #print(P[17])

    #print(X[18])
    #print(Y[18])
    #print(P[18])

    #print(X[19])
    #print(Y[19])
    #print(P[19])

    #print(X[20])

=======
Suggestion 10

def main():
    n = int(input())
    x = []
    y = []
    p = []
    for i in range(n):
        a, b, c = map(int, input().split())
        x.append(a)
        y.append(b)
        p.append(c)
    s = 0
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if p[i]*s >= abs(x[i]-x[j])+abs(y[i]-y[j]):
                break
        else:
            s += 1
    print(s)
