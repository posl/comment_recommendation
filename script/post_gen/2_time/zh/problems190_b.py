Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n,s,d = map(int,input().split())
    for i in range(n):
        x,y = map(int,input().split())
        if x < s and y > d:
            print('Yes')
            return
    print('No')

=======
Suggestion 2

def solve():
    N,S,D = map(int,input().split())
    X,Y = [],[]
    for i in range(N):
        x,y = map(int,input().split())
        X.append(x)
        Y.append(y)
    for i in range(N):
        if X[i] < S and Y[i] > D:
            print('Yes')
            return
    print('No')
    return

=======
Suggestion 3

def main():
    N, S, D = map(int, input().split())
    X = []
    Y = []
    for i in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)
    for i in range(N):
        if X[i] < S and Y[i] > D:
            print('Yes')
            return
    print('No')

=======
Suggestion 4

def main():
    #读取数据
    n, s, d = map(int, input().split())
    x = []
    y = []
    for _ in range(n):
        x_i, y_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
    #判断是否可以造成伤害
    for i in range(n):
        if x[i] < s and y[i] > d:
            print('Yes')
            return
    print('No')

=======
Suggestion 5

def solve():
    N, S, D = map(int, input().split())
    XY = [list(map(int, input().split())) for _ in range(N)]
    for X, Y in XY:
        if X < S and Y > D:
            print('Yes')
            return
    print('No')

=======
Suggestion 6

def solve():
    n, s, d = map(int, input().split())
    for _ in range(n):
        x, y = map(int, input().split())
        if x < s and y > d:
            print('Yes')
            return
    print('No')

=======
Suggestion 7

def main():
    n,s,d = map(int,input().split())
    for i in range(n):
        x,y = map(int,input().split())
        if x < s and y > d:
            print("Yes")
            return
    print("No")

=======
Suggestion 8

def solve():
    N, S, D = map(int, input().split())
    X = []
    Y = []
    for i in range(N):
        x, y = map(int, input().split())
        X.append(x)
        Y.append(y)

    for i in range(N):
        if X[i] < S and Y[i] > D:
            print("Yes")
            return
    print("No")

=======
Suggestion 9

def main():
    n,s,d = map(int,input().split())
    for i in range(n):
        x,y = map(int,input().split())
        if x < s and y > d:
            return print("Yes")
    return print("No")
