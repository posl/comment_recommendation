Synthesizing 10/10 solutions (Duplicates hidden)

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
    total = 0
    for i in range(N):
        total += V[i] * P[i]
        if total > X * 100:
            print(i + 1)
            return
    print(-1)
    return

main()

=======
Suggestion 2

def main():
    n,x = map(int, input().split())
    v = []
    p = []
    for i in range(n):
        v_i,p_i = map(int, input().split())
        v.append(v_i)
        p.append(p_i)
    sum = 0
    for i in range(n):
        sum += v[i]*p[i]
        if sum > x*100:
            print(i+1)
            break
    else:
        print(-1)

=======
Suggestion 3

def main():
    n,x = map(int,input().split())
    v = []
    p = []
    for i in range(n):
        v_i,p_i = map(int,input().split())
        v.append(v_i)
        p.append(p_i)
    alcohol = 0
    for i in range(n):
        alcohol += v[i]*p[i]/100
        if alcohol > x:
            print(i+1)
            break
    else:
        print(-1)

=======
Suggestion 4

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
Suggestion 5

def main():
    n,x = map(int,input().split())
    v = []
    p = []
    for i in range(n):
        a,b = map(int,input().split())
        v.append(a)
        p.append(b)
    s = 0
    for i in range(n):
        s += v[i]*p[i]
        if s > x*100:
            print(i+1)
            return
    print(-1)
    return

=======
Suggestion 6

def main():
    n,x = map(int,input().split())
    v = []
    p = []
    for i in range(n):
        v_,p_ = map(int,input().split())
        v.append(v_)
        p.append(p_)
    sum = 0
    for i in range(n):
        sum += v[i]*p[i]
        if sum > x*100:
            print(i+1)
            exit()
    print(-1)

=======
Suggestion 7

def main():
    N,X = map(int,input().split())
    V = []
    P = []
    for i in range(N):
        v,p = map(int,input().split())
        V.append(v)
        P.append(p)
    alcohol = 0
    for i in range(N):
        alcohol += V[i]*P[i]/100
        if alcohol > X:
            print(i+1)
            return
    print(-1)

=======
Suggestion 8

def solve():
    n,x = map(int,input().strip().split())
    v,p = [],[]
    for i in range(n):
        v_i,p_i = map(int,input().strip().split())
        v.append(v_i)
        p.append(p_i)
    sum = 0
    for i in range(n):
        sum += v[i]*p[i]/100
        if sum > x:
            print(i+1)
            return
    print(-1)

=======
Suggestion 9

def solve():
    N, X = map(int, input().split())
    X = X * 100
    count = 0
    for i in range(N):
        v, p = map(int, input().split())
        count += v * p
        if count > X:
            print(i + 1)
            return
    print(-1)
