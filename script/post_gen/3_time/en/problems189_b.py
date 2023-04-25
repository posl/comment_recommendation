Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, X = map(int, input().split())
    for i in range(N):
        V, P = map(int, input().split())
        X -= V * P / 100
        if X < 0:
            print(i + 1)
            exit()
    print(-1)

=======
Suggestion 2

def main():
    N, X = map(int, input().split())
    for i in range(N):
        V, P = map(int, input().split())
        X -= V * P / 100
        if X < 0:
            print(i + 1)
            return
    print(-1)

main()

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
    alcohol = 0
    for i in range(N):
        alcohol += V[i] * P[i] / 100
        if alcohol > X:
            print(i+1)
            return
    print(-1)
    return

=======
Suggestion 4

def main():
    N, X = map(int, input().split())
    V = [0] * N
    P = [0] * N
    for i in range(N):
        V[i], P[i] = map(int, input().split())
    alcohol = 0
    for i in range(N):
        alcohol += V[i] * P[i] / 100
        if alcohol > X:
            print(i + 1)
            return
    print(-1)
    return

=======
Suggestion 5

def main():
    N, X = map(int, input().split())
    V = [0] * N
    P = [0] * N
    for i in range(N):
        V[i], P[i] = map(int, input().split())
    alcohol = 0
    for i in range(N):
        alcohol += V[i] * P[i]
        if alcohol > X * 100:
            print(i + 1)
            break
    else:
        print(-1)

=======
Suggestion 6

def main():
    N, X = map(int, input().split())
    V = [0] * N
    P = [0] * N
    for i in range(N):
        V[i], P[i] = map(int, input().split())
    for i in range(N):
        X -= V[i] * P[i] / 100
        if X < 0:
            print(i + 1)
            return
    print(-1)

=======
Suggestion 7

def main():
    N, X = map(int, input().split())
    for i in range(N):
        v, p = map(int, input().split())
        X -= v * p / 100
        if X < 0:
            print(i + 1)
            return
    print(-1)

=======
Suggestion 8

def main():
    N, X = map(int, input().split())
    V, P = [], []
    for _ in range(N):
        v, p = map(int, input().split())
        V.append(v)
        P.append(p)
    total = 0
    for i in range(N):
        total += V[i] * P[i] / 100
        if total > X:
            print(i+1)
            return
    print(-1)
main()

=======
Suggestion 9

def main():
    n,x = map(int,input().split())
    for i in range(n):
        v,p = map(int,input().split())
        x -= v*p/100
        if x < 0:
            print(i+1)
            return
    print(-1)

=======
Suggestion 10

def main():
    N,X = map(int,input().split())
    V = [0]*N
    P = [0]*N
    for i in range(N):
        V[i],P[i] = map(int,input().split())

    alcohol = 0
    for i in range(N):
        alcohol += V[i]*P[i]
        if alcohol > X*100:
            print(i+1)
            return

    print(-1)
