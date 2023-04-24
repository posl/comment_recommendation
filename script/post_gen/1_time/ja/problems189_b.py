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
    sum = 0
    for i in range(N):
        sum = sum + V[i] * P[i]
        if sum > X * 100:
            print(i + 1)
            return
    print(-1)
    return

=======
Suggestion 2

def main():
    N, X = map(int, input().split())
    V = [0] * N
    P = [0] * N
    for i in range(N):
        V[i], P[i] = map(int, input().split())
    sum = 0
    for i in range(N):
        sum += V[i] * P[i]
        if sum > X * 100:
            print(i + 1)
            exit()
    print(-1)

=======
Suggestion 3

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
        sum += v[i] * p[i]
        if sum > x * 100:
            print(i + 1)
            exit()
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

    alc = 0
    for i in range(n):
        alc += v[i] * p[i] / 100
        if alc > x:
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
        v_i, p_i = map(int, input().split())
        v.append(v_i)
        p.append(p_i)
    alc = 0
    for i in range(n):
        alc += v[i] * p[i] / 100
        if alc > x:
            print(i + 1)
            return
    print(-1)

=======
Suggestion 6

def main():
    n, x = map(int, input().split())
    v, p = [], []
    for i in range(n):
        a, b = map(int, input().split())
        v.append(a)
        p.append(b)
    alc = 0
    for i in range(n):
        alc += v[i] * p[i] / 100
        if alc > x:
            print(i + 1)
            return
    print(-1)
    return

=======
Suggestion 7

def solve():
    N, X = map(int, input().split())
    ans = -1
    for i in range(N):
        V, P = map(int, input().split())
        X -= V * P
        if X < 0 and ans == -1:
            ans = i + 1
    print(ans)

=======
Suggestion 8

def main():
    n, x = map(int, input().split())
    v = []
    p = []

    for i in range(n):
        v_i, p_i = map(int, input().split())
        v.append(v_i)
        p.append(p_i)

    sum = 0
    for i in range(n):
        sum += v[i] * p[i]
        if sum > x * 100:
            print(i+1)
            return
    print(-1)

=======
Suggestion 9

def main():
    N,X = map(int,input().split())
    V = []
    P = []
    for i in range(N):
        v,p = map(int,input().split())
        V.append(v)
        P.append(p)
    alc = 0
    for i in range(N):
        alc += V[i]*P[i]/100
        if alc > X:
            print(i+1)
            break
    else:
        print(-1)

=======
Suggestion 10

def main():
    n,x = map(int,input().split())
    v_p = [list(map(int,input().split())) for _ in range(n)]
    v_p = [[v,p] for v,p in sorted(v_p,key=lambda x:x[1],reverse=True)]
    v_p = [[v,p] for v,p in sorted(v_p,key=lambda x:x[0]*x[1],reverse=True)]
    v_p = [[v,p] for v,p in sorted(v_p,key=lambda x:x[1],reverse=True)]
    sum = 0
    for i in range(n):
        v = v_p[i][0]
        p = v_p[i][1]
        sum += v*p
        if sum > x*100:
            print(i+1)
            return
    print(-1)
