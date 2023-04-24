Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, m, x, t, d = map(int, input().split())
    for i in range(x):
        t -= d
    for i in range(x, n):
        t += d
    print(t)

=======
Suggestion 2

def main():
    N, M, X, T, D = map(int, input().split())
    for i in range(X, M):
        T += D
    print(T)

=======
Suggestion 3

def main():
    N, M, X, T, D = map(int, input().split())
    if M < X:
        for i in range(M, X):
            T -= D
    elif M > X:
        for i in range(X, M):
            T += D
    print(T)

=======
Suggestion 4

def calc_height(N, M, X, T, D):
    height = T
    for i in range(1, X):
        height -= D
    for i in range(X, N):
        height += D
    return height

=======
Suggestion 5

def calc_height(n, m, x, t, d):
    height = t
    for i in range(1, m):
        height += d
    for i in range(m, n):
        height += d
        if i == x:
            continue
    return height

=======
Suggestion 6

def main():
    N,M,X,T,D = map(int,input().split())
    height = X * D + 1
    for i in range(X+1,N+1):
        height += D
        if i == M:
            break
    print(height)

=======
Suggestion 7

def solve():
    N,M,X,T,D = map(int,input().split())

    for i in range(X):
        T += D
    for i in range(X,N):
        T -= D
    print(T)

=======
Suggestion 8

def calc_height(n, m, x, t, d):
    if m <= x:
        result = t + (m-1)*d
        for i in range(m, x):
            result += d
        return result
    else:
        result = t + (x-1)*d
        for i in range(x, m):
            result -= d
        return result

=======
Suggestion 9

def calc_height(year, start_year, start_height, grow_height):
    if year == start_year:
        return start_height
    elif year < start_year:
        return 0
    else:
        return calc_height(year-1, start_year, start_height, grow_height) + grow_height
