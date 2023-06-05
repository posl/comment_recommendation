Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N,X = map(int, input().split())
    V = []
    P = []
    for i in range(N):
        v,p = map(int, input().split())
        V.append(v)
        P.append(p)
    sum = 0
    for i in range(N):
        sum += V[i]*P[i]
        if sum > X*100:
            print(i+1)
            return
    print(-1)
    return

=======
Suggestion 2

def main():
    n, x = map(int, input().split())
    v = []
    p = []
    for i in range(n):
        a, b = map(int, input().split())
        v.append(a)
        p.append(b)
    sum = 0
    for i in range(n):
        sum += v[i] * p[i] / 100
        if sum > x:
            print(i + 1)
            break
    if sum <= x:
        print(-1)

=======
Suggestion 3

def main():
    N, X = map(int, input().split())
    V = []
    P = []
    for i in range(N):
        v, p = map(int, input().split())
        V.append(v)
        P.append(p)
    sum = 0
    for i in range(N):
        sum += V[i] * P[i] / 100
        if sum > X:
            print(i + 1)
            return
    print(-1)

=======
Suggestion 4

def main():
    n,x = map(int, input().split())
    v = []
    p = []
    for i in range(n):
        a,b = map(int, input().split())
        v.append(a)
        p.append(b)
    sum = 0
    for i in range(n):
        sum += v[i]*p[i]/100
        if sum > x:
            print(i+1)
            return
    print(-1)
    return

=======
Suggestion 5

def main():
    n, x = map(int, input().split())
    x *= 100
    v, p = [], []
    for _ in range(n):
        v_, p_ = map(int, input().split())
        v.append(v_)
        p.append(p_)
    s = 0
    for i in range(n):
        s += v[i] * p[i]
        if s > x:
            print(i + 1)
            return
    print(-1)

=======
Suggestion 6

def main():
    N, X = map(int, input().split())
    V = []
    P = []
    for i in range(N):
        v, p = map(int, input().split())
        V.append(v)
        P.append(p)
    alcohol = 0
    for i in range(N):
        alcohol += V[i] * P[i] / 100
        if alcohol > X:
            print(i+1)
            return
    print(-1)

=======
Suggestion 7

def main():
    N, X = map(int, input().split())
    V = []
    P = []
    for i in range(N):
        v, p = map(int, input().split())
        V.append(v)
        P.append(p)
    X = X * 1000
    alcohol = 0
    for i in range(N):
        alcohol += V[i] * P[i]
        if alcohol > X:
            print(i + 1)
            exit()
    print(-1)

=======
Suggestion 8

def main():
    n, x = map(int, input().split())
    x *= 100
    v = 0
    for i in range(n):
        a, b = map(int, input().split())
        v += a * b
        if v > x:
            print(i+1)
            return
    print(-1)

=======
Suggestion 9

def main():
    n, x = map(int, input().split())
    v = []
    p = []
    for i in range(n):
        a, b = map(int, input().split())
        v.append(a)
        p.append(b)
    s = 0
    for i in range(n):
        s += v[i] * p[i] / 100
        if s > x:
            print(i + 1)
            break
    else:
        print(-1)

=======
Suggestion 10

def solve():
    N,X = map(int,input().split())
    V = []
    P = []
    for i in range(N):
        v,p = map(int,input().split())
        V.append(v)
        P.append(p)
    sum = 0
    for i in range(N):
        sum += V[i] * P[i]
        if sum > X * 100:
            print(i+1)
            return
    print(-1)
