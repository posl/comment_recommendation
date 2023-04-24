Synthesizing 10/10 solutions

=======
Suggestion 1

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
            print("Yes")
            return
    print("No")
main()

=======
Suggestion 2

def solve():
    n, s, d = map(int, input().split())
    for _ in range(n):
        x, y = map(int, input().split())
        if x < s and y > d:
            print("Yes")
            return
    print("No")

=======
Suggestion 3

def solve():
    N, S, D = map(int, input().split())
    for _ in range(N):
        X, Y = map(int, input().split())
        if X < S and Y > D:
            print("Yes")
            return
    print("No")

=======
Suggestion 4

def solve():
    n, s, d = map(int, input().split())
    for i in range(n):
        x, y = map(int, input().split())
        if x < s and y > d:
            print("Yes")
            return
    print("No")
    return

=======
Suggestion 5

def solve():
    N, S, D = map(int, input().split())
    X = [0] * N
    Y = [0] * N
    for i in range(N):
        X[i], Y[i] = map(int, input().split())
    for i in range(N):
        if X[i] < S and Y[i] > D:
            print("Yes")
            return
    print("No")
    return

=======
Suggestion 6

def solve():
    N, S, D = map(int, input().split())
    for i in range(N):
        X, Y = map(int, input().split())
        if X < S and D < Y:
            print("Yes")
            return
    print("No")

=======
Suggestion 7

def main():
    n, s, d = map(int, input().split())
    xy = [list(map(int, input().split())) for _ in range(n)]
    for x, y in xy:
        if x < s and y > d:
            print('Yes')
            return
    print('No')

=======
Suggestion 8

def main():
    N, S, D = map(int, input().split())
    XY = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        if XY[i][0] < S and XY[i][1] > D:
            print("Yes")
            return
    print("No")
    return

=======
Suggestion 9

def main():
    n, s, d = map(int, input().split())
    x, y = [], []
    for _ in range(n):
        x_i, y_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)
    for i in range(n):
        if x[i] < s and y[i] > d:
            print("Yes")
            return
    print("No")

=======
Suggestion 10

def check():
    N,S,D = map(int, input().split())
    ret = "No"
    for i in range(N):
        X,Y = map(int, input().split())
        if X < S and Y > D:
            ret = "Yes"
    print(ret)
