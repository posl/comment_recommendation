Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n,x = map(int,input().split())
    v = [0] * n
    p = [0] * n
    for i in range(n):
        v[i],p[i] = map(int,input().split())

    alc = 0
    for i in range(n):
        alc += v[i] * (p[i] / 100)
        if alc > x:
            print(i+1)
            return

    print(-1)

main()

=======
Suggestion 2

def get_int():
    return int(input())

=======
Suggestion 3

def main():
    n, x = map(int, input().split())
    x *= 100
    sum = 0
    for i in range(n):
        v, p = map(int, input().split())
        sum += v * p
        if sum > x:
            print(i + 1)
            return
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
        sum += V[i]*P[i]
        if sum > X*100:
            print(i+1)
            return
    print(-1)
    return

=======
Suggestion 5

def main():
    N,X = map(int,input().split())
    V = []
    P = []
    for i in range(N):
        v,p = map(int,input().split())
        V.append(v)
        P.append(p)
    V = [V[i]*P[i]/100 for i in range(N)]
    V = [sum(V[:i+1]) for i in range(N)]
    if V[-1] <= X:
        print(-1)
    else:
        for i in range(N):
            if V[i] > X:
                print(i+1)
                break

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
    #print(V)
    #print(P)
    sum = 0
    for i in range(N):
        sum += V[i] * P[i] / 100
        if sum > X:
            print(i + 1)
            exit()
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
    total = 0
    for i in range(N):
        total += V[i] * P[i]
        if total > X * 100:
            print(i + 1)
            return
    print(-1)

=======
Suggestion 8

def main():
    n,x = map(int,input().split())
    v = []
    p = []
    for i in range(n):
        vi,pi = map(int,input().split())
        v.append(vi)
        p.append(pi)
    sum = 0
    for i in range(n):
        sum += v[i]*p[i]
        if sum > x*100:
            print(i+1)
            break
    else:
        print(-1)

=======
Suggestion 9

def main():
    n,x=map(int,input().split())
    v=[0]*n
    p=[0]*n
    for i in range(n):
        v[i],p[i]=map(int,input().split())
    s=0
    for i in range(n):
        s+=v[i]*p[i]
        if s>x*100:
            print(i+1)
            break
    else:
        print(-1)

=======
Suggestion 10

def main():
    N,X = map(int,input().split())
    V = []
    P = []
    for i in range(N):
        v,p = map(int,input().split())
        V.append(v)
        P.append(p)
    total = 0
    for i in range(N):
        total += V[i] * P[i] / 100
        if total > X:
            print(i+1)
            exit()
    print(-1)
