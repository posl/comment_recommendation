Synthesizing 9/10 solutions

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
    #print(N, S, D)
    #print(X)
    #print(Y)
    for i in range(N):
        if X[i] < S and Y[i] > D:
            print("Yes")
            return
    print("No")

=======
Suggestion 2

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
solve()

=======
Suggestion 3

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
Suggestion 4

def solve():
    N, S, D = map(int, input().split())
    for i in range(N):
        X, Y = map(int, input().split())
        if X < S and Y > D:
            print("Yes")
            return
    print("No")
    return

=======
Suggestion 5

def solve():
    N, S, D = map(int, input().split())
    X, Y = [], []
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
Suggestion 6

def main():
    N,S,D = map(int, input().split())
    X = []
    Y = []
    for i in range(N):
        x,y = map(int, input().split())
        X.append(x)
        Y.append(y)
    for i in range(N):
        if X[i] < S and Y[i] > D:
            print('Yes')
            exit()
    print('No')

=======
Suggestion 7

def main():
    n, s, d = map(int, input().split())
    xy = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        if xy[i][0] < s and xy[i][1] > d:
            print('Yes')
            return
    print('No')
main()

=======
Suggestion 8

def main():
    n, s, d = map(int, input().split())
    x = []
    y = []
    for i in range(n):
        tmp_x, tmp_y = map(int, input().split())
        x.append(tmp_x)
        y.append(tmp_y)
    for i in range(n):
        if x[i] < s and y[i] > d:
            print("Yes")
            return
    print("No")
    return

=======
Suggestion 9

def solve():
    n,s,d = map(int,input().split())
    magic = []
    for i in range(n):
        magic.append(list(map(int,input().split())))
    for i in range(n):
        if magic[i][0] < s and magic[i][1] > d:
            print("Yes")
            return
    print("No")
    return
