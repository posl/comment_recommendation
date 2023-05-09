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
    # print(N, X, V, P)
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
    N, X = map(int, input().split())
    V = []
    P = []
    for i in range(N):
        v, p = map(int, input().split())
        V.append(v)
        P.append(p)
    V_total = 0
    for i in range(N):
        V_total += V[i] * P[i]
        if V_total > X * 100:
            print(i + 1)
            break
    else:
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

    alc = 0
    for i in range(N):
        alc += V[i] * P[i] / 100
        if alc > X:
            print(i + 1)
            exit()

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

    x = 0
    for i in range(N):
        x += V[i] * (P[i] / 100)
        if x > X:
            print(i+1)
            return

    print(-1)

main()

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
        sum = sum + V[i] * P[i]
        if sum > X * 100:
            print(i + 1)
            return
    print(-1)

=======
Suggestion 6

def main():
    N, X = map(int, input().split())
    V = [0] * N
    P = [0] * N
    for i in range(N):
        V[i], P[i] = map(int, input().split())

    alc = 0
    for i in range(N):
        alc += V[i] * P[i]
        if alc > X * 100:
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
        a, b = map(int, input().split())
        v.append(a)
        p.append(b)
    sum = 0
    for i in range(n):
        sum += v[i] * p[i]
        if sum > x * 100:
            print(i + 1)
            return
    print(-1)

=======
Suggestion 8

def solve(n, x, v, p):
    sum = 0
    for i in range(n):
        sum += v[i] * p[i]
        if sum > x * 100:
            return i + 1
    return -1

=======
Suggestion 9

def main():
    n, x = [int(i) for i in input().split()]
    v = []
    p = []
    for i in range(n):
        a, b = [int(i) for i in input().split()]
        v.append(a)
        p.append(b)
    total = 0
    for i in range(n):
        total += v[i] * p[i]
        if total > x * 100:
            print(i + 1)
            return
    print(-1)

=======
Suggestion 10

def get_ints(): return map(int, input().strip().split())
