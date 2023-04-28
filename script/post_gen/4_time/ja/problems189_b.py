Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, X = map(int, input().split())
    V = []
    P = []
    for i in range(N):
        v, p = map(int, input().split())
        V.append(v)
        P.append(p)
    
    alc = 0
    for i in range(N):
        alc += V[i] * P[i] / 100
        if alc > X:
            print(i+1)
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
    alc = 0
    for i in range(N):
        alc += V[i] * P[i] / 100
        if alc > X:
            print(i + 1)
            exit()
    print(-1)

=======
Suggestion 3

def solve():
    N, X = map(int, input().split())
    V = []
    P = []
    for i in range(N):
        v, p = map(int, input().split())
        V.append(v)
        P.append(p)
    alc = 0
    for i in range(N):
        alc += V[i] * P[i] / 100
        if alc > X:
            print(i + 1)
            return
    print(-1)

=======
Suggestion 4

def main():
    n, x = map(int, input().split())
    v = []
    p = []
    for i in range(n):
        vi, pi = map(int, input().split())
        v.append(vi)
        p.append(pi)
    total = 0
    for i in range(n):
        total += v[i] * p[i]
        if total > x * 100:
            print(i + 1)
            return
    print(-1)

=======
Suggestion 5

def main():
    n, x = map(int, input().split())
    v = []
    p = []
    for i in range(n):
        vi, pi = map(int, input().split())
        v.append(vi)
        p.append(pi)

    sum = 0
    for i in range(n):
        sum += v[i] * p[i]
        if sum > x * 100:
            print(i + 1)
            return
    print(-1)

=======
Suggestion 6

def main():
    n, x = map(int, input().split())
    v = []
    p = []
    for i in range(n):
        v_i, p_i = map(int, input().split())
        v.append(v_i)
        p.append(p_i)
    alc = 0
    for i in range(n):
        alc += v[i] * p[i]
        if alc > x * 100:
            print(i + 1)
            return
    print(-1)
    return

=======
Suggestion 7

def main():
    n, x = map(int, input().split())
    v = []
    p = []
    for _ in range(n):
        a, b = map(int, input().split())
        v.append(a)
        p.append(b)
    total = 0
    for i in range(n):
        total += v[i] * p[i]
        if total > x * 100:
            print(i + 1)
            return
    print(-1)

main()

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

    alc = 0
    for i in range(n):
        alc += v[i] * p[i]
        if alc > x * 100:
            print(i + 1)
            return

    print(-1)

=======
Suggestion 9

def main():
    N, X = map(int, input().split())
    ans = -1
    for i in range(1, N+1):
        v, p = map(int, input().split())
        X -= v * p / 100
        if X < 0:
            ans = i
            break
    print(ans)

=======
Suggestion 10

def main():
    N,X = map(int,input().split())
    VPs = [list(map(int,input().split())) for _ in range(N)]
    alc = 0
    for i in range(N):
        alc += VPs[i][0] * VPs[i][1] / 100
        if alc > X:
            print(i+1)
            return
    print(-1)
