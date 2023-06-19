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
        sum += V[i] * P[i]
        if sum > X * 100:
            print(i+1)
            return
    print(-1)

=======
Suggestion 2

def main():
    n, x = map(int, input().split())
    v = []
    p = []
    for _ in range(n):
        v_, p_ = map(int, input().split())
        v.append(v_)
        p.append(p_)
    alc = 0
    for i in range(n):
        alc = alc + v[i] * p[i]
        if alc > x * 100:
            print(i + 1)
            exit()
    print(-1)

=======
Suggestion 3

def main():
    n,x = map(int,input().split())
    v = []
    p = []
    for i in range(n):
        a,b = map(int,input().split())
        v.append(a)
        p.append(b)
    sum = 0
    for i in range(n):
        sum += v[i] * p[i] / 100
        if sum > x:
            print(i+1)
            return
    print(-1)
    return

=======
Suggestion 4

def get_ints():
    return [int(x) for x in input().split()]

=======
Suggestion 5

def main():
    n, x = map(int, input().split())
    x *= 100
    cnt = 0
    for i in range(n):
        v, p = map(int, input().split())
        cnt += v * p
        if cnt > x:
            print(i + 1)
            return
    print(-1)

=======
Suggestion 6

def solve():
    n, x = map(int, input().split())
    p = 0
    for i in range(n):
        v, p = map(int, input().split())
        x -= v * p
        if x < 0:
            print(i + 1)
            return
    print(-1)

solve()

=======
Suggestion 7

def solve():
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
Suggestion 8

def main():
    n, x = map(int, input().split())
    sum = 0
    for i in range(n):
        v, p = map(int, input().split())
        sum += v * p
        if sum > x * 100:
            print(i + 1)
            exit()
    print(-1)

=======
Suggestion 9

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
Suggestion 10

def main():
    #读入数据
    n,x = map(int,input().split())
    v = []
    p = []
    for _ in range(n):
        v_i,p_i = map(int,input().split())
        v.append(v_i)
        p.append(p_i)
    #计算酒精含量
    alcohol = 0
    for i in range(n):
        alcohol += v[i]*p[i]
        if alcohol > x*100:
            print(i+1)
            return
    print(-1)
