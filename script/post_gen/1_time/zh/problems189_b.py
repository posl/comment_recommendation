Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N,X = map(int,input().split())
    V = []
    P = []
    for i in range(N):
        v,p = map(int,input().split())
        V.append(v)
        P.append(p)
    sum = 0
    for i in range(N):
        sum += V[i]*P[i]
        if sum > X*100:
            print(i+1)
            break
    else:
        print(-1)

=======
Suggestion 2

def main():
    n,x = map(int,input().split())
    v = []
    p = []
    for _ in range(n):
        v_i,p_i = map(int,input().split())
        v.append(v_i)
        p.append(p_i)
    sum = 0
    for i in range(n):
        sum += v[i]*p[i]
        if sum > x*100:
            print(i+1)
            exit()
    print(-1)

=======
Suggestion 3

def main():
    n,x = map(int,input().split())
    for i in range(n):
        v,p = map(int,input().split())
        x -= v * p / 100
        if x < 0:
            print(i+1)
            return
    print(-1)

=======
Suggestion 4

def get_input():
    n, x = map(int, input().split())
    v_p = []
    for i in range(n):
        v_p.append(list(map(int, input().split())))
    return n, x, v_p

=======
Suggestion 5

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
        sum += V[i]*P[i]
        if sum > X*100:
            print(i+1)
            return
    print(-1)

=======
Suggestion 6

def main():
    n, x = map(int, input().split())
    x *= 100
    for i in range(n):
        v, p = map(int, input().split())
        x -= v * p
        if x < 0:
            print(i + 1)
            return
    print(-1)

=======
Suggestion 7

def main():
    N, X = map(int, input().split())
    V = [0] * N
    P = [0] * N
    for i in range(N):
        V[i], P[i] = map(int, input().split())
    alc = 0
    for i in range(N):
        alc += V[i] * P[i] / 100
        if alc > X:
            print(i + 1)
            exit()
    print(-1)

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
        sum += v[i] * p[i] / 100
        if sum > x:
            print(i + 1)
            return
    print(-1)

=======
Suggestion 9

def main():
    n,x = map(int, input().split())
    v = []
    p = []
    for i in range(n):
        V, P = map(int, input().split())
        v.append(V)
        p.append(P)
    alcohol = 0
    for i in range(n):
        alcohol += v[i] * p[i] / 100
        if alcohol > x:
            print(i + 1)
            return
    print(-1)
    return

=======
Suggestion 10

def main():
    n, x = map(int, input().split())
    v = []
    p = []
    for i in range(n):
        v_temp, p_temp = map(int, input().split())
        v.append(v_temp)
        p.append(p_temp)
    sum = 0
    for i in range(n):
        sum += v[i] * p[i]
        if sum > x * 100:
            print(i + 1)
            return
    print(-1)
    return

main()
