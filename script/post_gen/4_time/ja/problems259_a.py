Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, M, X, T, D = map(int, input().split())
    for i in range(X, N):
        T += D
    for i in range(M, X):
        T -= D
    print(T)

=======
Suggestion 2

def main():
    N, M, X, T, D = map(int, input().split())
    H = T
    for i in range(1, X):
        H -= D
    for i in range(X, M):
        H += D
    print(H)

=======
Suggestion 3

def main():
    n, m, x, t, d = map(int, input().split())

    height = t
    for i in range(1, x):
        height -= d

    for i in range(x, n):
        height += d

    print(height)

=======
Suggestion 4

def main():
    N, M, X, T, D = map(int, input().split())
    for i in range(X):
        T += D
    for i in range(N-X):
        T -= D
    print(T)

=======
Suggestion 5

def calc_height(m, x, t, d):
    height = t
    for i in range(x, m):
        height += d
    return height

n, m, x, t, d = map(int, input().split())
print(calc_height(m, x, t, d))

=======
Suggestion 6

def main():
    n, m, x, t, d = map(int, input().split())
    for i in range(x):
        t -= d
    for i in range(m - x):
        t -= 1
    print(t)

=======
Suggestion 7

def get_input():
    n, m, x, t, d = map(int, input().split())
    return n, m, x, t, d

=======
Suggestion 8

def main():
    N,M,X,T,D = map(int, input().split())
    for i in range(M,X):
        T += D
    print(T)

=======
Suggestion 9

def main():
    n,m,x,t,d = map(int,input().split())
    if m >= x:
        for i in range(m-x):
            t += d
    else:
        for i in range(x-m):
            t -= d
    print(t)

=======
Suggestion 10

def calcHeight(n, m, x, t, d):
    # 0歳からx歳までの伸びた身長
    h = 0
    for i in range(1, x + 1):
        h = h + d

    # x歳からn歳までの身長
    for i in range(x + 1, n + 1):
        h = h + t

    # m歳の身長を求める
    if m <= x:
        for i in range(1, m):
            h = h - d
    else:
        for i in range(x + 1, m):
            h = h - t

    return h
