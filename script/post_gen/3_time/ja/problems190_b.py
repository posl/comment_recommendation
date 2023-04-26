Synthesizing 9/10 solutions (Duplicates hidden)

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
            exit()
    print("No")

=======
Suggestion 2

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
    return

=======
Suggestion 3

def solve():
    N, S, D = map(int, input().split())
    for _ in range(N):
        X, Y = map(int, input().split())
        if X < S and Y > D:
            print('Yes')
            return
    print('No')

=======
Suggestion 4

def solve():
    N, S, D = map(int, input().split())
    for i in range(N):
        X, Y = map(int, input().split())
        if X < S and Y > D:
            print('Yes')
            return
    print('No')
    return

=======
Suggestion 5

def solve():
    N,S,D = map(int,input().split())
    for i in range(N):
        X,Y = map(int,input().split())
        if X < S and Y > D:
            print("Yes")
            return
    print("No")
    return

=======
Suggestion 6

def main():
    n,s,d = map(int,input().split())
    xy = [list(map(int,input().split())) for _ in range(n)]
    for x,y in xy:
        if x < s and y > d:
            print("Yes")
            exit()
    print("No")

=======
Suggestion 7

def solve():
    n,s,d = map(int, input().split())
    x = []
    y = []
    for i in range(n):
        x_i, y_i = map(int, input().split())
        x.append(x_i)
        y.append(y_i)

    for i in range(n):
        if x[i] < s and y[i] > d:
            print("Yes")
            return

    print("No")

=======
Suggestion 8

def get_input_data():
    n, s, d = map(int, input().split())
    xy = [list(map(int, input().split())) for _ in range(n)]
    return n, s, d, xy
