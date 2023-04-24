Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, X = map(int, input().split())
    for i in range(N):
        V, P = map(int, input().split())
        X -= V * P / 100
        if X < 0:
            print(i + 1)
            return
    print(-1)

=======
Suggestion 2

def main():
    N, X = map(int, input().split())
    V = []
    P = []
    for i in range(N):
        v, p = map(int, input().split())
        V.append(v)
        P.append(p)
    ans = -1
    for i in range(N):
        X -= V[i]*P[i]/100
        if X < 0:
            ans = i+1
            break
    print(ans)

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
    alcohol = 0
    for i in range(N):
        alcohol += V[i] * P[i] / 100
        if alcohol > X:
            print(i+1)
            return
    print(-1)

=======
Suggestion 4

def main():
    N, X = map(int, input().split())
    for i in range(N):
        v, p = map(int, input().split())
        X -= v * p / 100
        if X < 0:
            return i + 1
    return -1

print(main())

=======
Suggestion 5

def main():
    N, X = map(int, input().split())
    V, P = [], []
    for i in range(N):
        v, p = map(int, input().split())
        V.append(v)
        P.append(p)
    for i in range(N):
        X -= V[i]*P[i]/100
        if X < 0:
            print(i+1)
            return
    print(-1)
    return

=======
Suggestion 6

def main():
    N, X = map(int, input().split())
    for i in range(1, N+1):
        V, P = map(int, input().split())
        X -= V * P / 100
        if X < 0:
            print(i)
            return
    print(-1)

=======
Suggestion 7

def main():
    n, x = map(int, input().split())
    v, p = [], []
    for i in range(n):
        v_i, p_i = map(int, input().split())
        v.append(v_i)
        p.append(p_i)
    for i in range(n):
        x -= v[i] * p[i] / 100
        if x < 0:
            print(i + 1)
            return
    print(-1)

=======
Suggestion 8

def main():
    n, x = map(int, input().split())
    v = []
    p = []
    for i in range(n):
        v_, p_ = map(int, input().split())
        v.append(v_)
        p.append(p_)
    vol = 0
    for i in range(n):
        vol += v[i] * p[i] / 100
        if vol > x:
            print(i + 1)
            return
    print(-1)

=======
Suggestion 9

def main():
    N, X = map(int, input().split())
    for i in range(1, N+1):
        V, P = map(int, input().split())
        X -= V * P/100
        if X < 0:
            print(i)
            exit()
    print(-1)

=======
Suggestion 10

def get_input():
    N, X = map(int, input().split())
    V = []
    P = []
    for _ in range(N):
        v, p = map(int, input().split())
        V.append(v)
        P.append(p)
    return N, X, V, P
