Synthesizing 10/10 solutions

=======
Suggestion 1

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
            break
    else:
        print(-1)

=======
Suggestion 2

def main():
    n, x = map(int, input().split())
    v = []
    p = []
    for i in range(n):
        v_p = list(map(int, input().split()))
        v.append(v_p[0])
        p.append(v_p[1])
    sum = 0
    for i in range(n):
        sum += v[i] * p[i] / 100
        if sum > x:
            print(i + 1)
            return
    print(-1)

=======
Suggestion 3

def main():
    n, x = map(int, input().split())
    alc = 0
    for i in range(n):
        v, p = map(int, input().split())
        alc += v * p
        if alc > x * 100:
            print(i + 1)
            return
    print(-1)

=======
Suggestion 4

def main():
    n, x = map(int, input().split())
    v = []
    p = []
    for _ in range(n):
        vi, pi = map(int, input().split())
        v.append(vi)
        p.append(pi)

    ans = -1
    alc = 0
    for i in range(n):
        alc += v[i] * p[i]
        if alc > x * 100:
            ans = i+1
            break

    print(ans)

=======
Suggestion 5

def main():
    n, x = map(int, input().split())
    v = [0] * n
    p = [0] * n

    for i in range(n):
        v[i], p[i] = map(int, input().split())

    a = 0
    for i in range(n):
        a += v[i] * p[i]
        if a > x * 100:
            print(i + 1)
            return

    print(-1)

=======
Suggestion 6

def main():
    N, X = map(int, input().split())
    V, P = [], []
    for _ in range(N):
        v, p = map(int, input().split())
        V.append(v)
        P.append(p)
    a = 0
    for i in range(N):
        a += V[i] * P[i]
        if a > X * 100:
            print(i + 1)
            return
    print(-1)

=======
Suggestion 7

def calculate():
    N,X = map(int, input().split())
    V = []
    P = []
    for i in range(N):
        v,p = map(int, input().split())
        V.append(v)
        P.append(p)
    alc = 0
    for i in range(N):
        alc += V[i]*P[i]/100
        if alc > X:
            print(i+1)
            return
    print(-1)
    return

=======
Suggestion 8

def main():
    n, x = map(int, input().split())
    v_p = [list(map(int, input().split())) for i in range(n)]
    alcohol = 0
    for i in range(n):
        alcohol += v_p[i][0] * v_p[i][1] / 100
        if alcohol > x:
            print(i+1)
            exit()
    print(-1)

=======
Suggestion 9

def main():
    n,x = map(int,input().split())
    v = []
    p = []
    for i in range(n):
        v_i,p_i = map(int,input().split())
        v.append(v_i)
        p.append(p_i)
    sum = 0
    for i in range(n):
        sum += v[i]*p[i]
        if sum > x*100:
            print(i+1)
            return
    print(-1)
    return

=======
Suggestion 10

def main():
    n, x = map(int, input().split())
    v_p = [list(map(int, input().split())) for _ in range(n)]
    alc = 0
    for i in range(n):
        alc += v_p[i][0] * v_p[i][1] / 100
        if alc > x:
            print(i + 1)
            exit()
    print(-1)
