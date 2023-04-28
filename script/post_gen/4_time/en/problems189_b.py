Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, x = map(int, input().split())
    for i in range(n):
        v, p = map(int, input().split())
        x -= v * p / 100
        if x < 0:
            print(i + 1)
            return
    print(-1)
    return

=======
Suggestion 2

def main():
    N, X = map(int, input().split())
    for i in range(N):
        V, P = map(int, input().split())
        X -= V * P / 100
        if X < 0:
            print(i+1)
            return
    print(-1)

main()

I am a Japanese student.

I am studying programming for the first time.

I am studying Python.

I am studying at the University of Tokyo.

=======
Suggestion 3

def main():
    N, X = map(int, input().split())
    for i in range(N):
        V, P = map(int, input().split())
        X -= V * P / 100
        if X < 0:
            print(i+1)
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

    s = 0
    for i in range(N):
        s += V[i] * P[i] / 100
        if s > X:
            print(i + 1)
            return

    print(-1)

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
    alcohol = 0
    for i in range(N):
        alcohol += (V[i] * P[i])
        if alcohol > X * 100:
            print(i+1)
            return
    print(-1)
    return

=======
Suggestion 6

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
            return

    print(-1)

=======
Suggestion 7

def main():
    N, X = map(int, input().split())
    V, P = [], []
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
    #input
    N, X = map(int, input().split())
    VPs = [list(map(int, input().split())) for _ in range(N)]
    #compute
    ans = -1
    for i in range(N):
        if X < VPs[i][0]*VPs[i][1]/100:
            ans = i+1
            break
    #output
    print(ans)
