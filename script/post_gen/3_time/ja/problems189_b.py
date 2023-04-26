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
        alc += V[i] * P[i]
        if alc > X * 100:
            print(i + 1)
            return
    print(-1)

=======
Suggestion 2

def main():
    n, x = map(int, input().split())
    sum = 0
    for i in range(n):
        v, p = map(int, input().split())
        sum += v * p
        if sum > x * 100:
            print(i + 1)
            return
    print(-1)

=======
Suggestion 3

def main():
    n, x = map(int, input().split())
    v = [0] * n
    p = [0] * n
    for i in range(n):
        v[i], p[i] = map(int, input().split())
    ans = -1
    alc = 0
    for i in range(n):
        alc += v[i] * p[i]
        if alc > x * 100:
            ans = i + 1
            break
    print(ans)

=======
Suggestion 4

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
Suggestion 5

def main():
    n, x = map(int, input().split())
    v = []
    p = []
    for i in range(n):
        a, b = map(int, input().split())
        v.append(a)
        p.append(b)
    al = 0
    for i in range(n):
        al += v[i] * p[i]
        if al > x * 100:
            print(i + 1)
            break
    else:
        print(-1)

=======
Suggestion 6

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
Suggestion 7

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
Suggestion 8

def solve(n, x, v, p):
    alc = 0
    for i in range(n):
        alc += v[i] * p[i] / 100
        if alc > x:
            return i + 1
    return -1

=======
Suggestion 9

def main():
    n,x = map(int, input().split())
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
            print(i + 1)
            return
    print(-1)

=======
Suggestion 10

def main():
    # input
    n, x = map(int, input().split())
    #print(n, x)
    v = []
    p = []
    for i in range(n):
        v_tmp, p_tmp = map(int, input().split())
        v.append(v_tmp)
        p.append(p_tmp)
    #print(v)
    #print(p)

    # compute
    alc = 0
    for i in range(n):
        alc += v[i] * p[i] / 100
        if alc > x:
            print(i+1)
            exit()
    print(-1)
