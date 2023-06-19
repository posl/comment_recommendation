Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def birthday(N,M,X,T,D):
    height = T
    for i in range(X,M):
        height += D
    return height

=======
Suggestion 2

def main():
    N,M,X,T,D = map(int,input().split())

    for i in range(1,N+1):
        if i == M:
            print(X)
            break
        elif i < X:
            X += D
        else:
            X += D

=======
Suggestion 3

def main():
    N,M,X,T,D = map(int,input().split())
    if M == 0:
        print(T)
        return
    if M == X:
        print(T)
        return
    if M == N:
        print(T + (N-X)*D)
        return
    if X > M:
        print(T + (X-M)*D)
        return
    if X < M:
        print(T + (M-X)*D)
        return

=======
Suggestion 4

def main():
    n, m, x, t, d = map(int, input().split())
    height = t
    for i in range(x, m):
        height += d
    for i in range(m, n):
        height += d
    print(height)

=======
Suggestion 5

def main():
    # 读取数据
    N, M, X, T, D = map(int, input().split())
    # 求和
    sum = T
    for i in range(X, M):
        sum += D
    print(sum)

=======
Suggestion 6

def main():
    N, M, X, T, D = map(int, input().split())
    for i in range(M):
        if X <= i:
            T += D
    print(T)

=======
Suggestion 7

def main():
    N,M,X,T,D = map(int, input().split())
    height = T
    for i in range(1, N):
        if i == M:
            break
        if i >= X:
            height += D
    print(height)

=======
Suggestion 8

def main():
    n, m, x, t, d = map(int, input().split())
    for i in range(1, n+1):
        if i == m:
            print(t)
            break
        if i < x:
            t += d
        else:
            t -= d

=======
Suggestion 9

def birthday():
    N,M,X,T,D = map(int, input().split())
    height = T
    for i in range(1, X):
        height += D
    for i in range(X, M):
        height += D
    print(height)
