Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

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
Suggestion 2

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
            print(i+1)
            return

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
    S = 0
    for i in range(N):
        S += V[i] * P[i]
        if S > X * 100:
            print(i + 1)
            return
    print(-1)

=======
Suggestion 4

def main():
    N, X = map(int, input().split())
    V = [0] * N
    P = [0] * N
    for i in range(N):
        V[i], P[i] = map(int, input().split())
    ans = -1
    for i in range(N):
        if V[i] * P[i] / 100 > X:
            ans = i + 1
            break
        else:
            X -= V[i] * P[i] / 100
    print(ans)

=======
Suggestion 5

def main():
    N, X = map(int, input().split())
    V = [0] * N
    P = [0] * N
    for i in range(N):
        V[i], P[i] = map(int, input().split())
    
    total = 0
    for i in range(N):
        total += V[i] * P[i] // 100
        if total > X:
            print(i + 1)
            return
    print(-1)

=======
Suggestion 6

def main():
    N, X = map(int, input().split())
    for i in range(N):
        V, P = map(int, input().split())
        X -= V * (P / 100)
        if X < 0:
            print(i + 1)
            return
    print(-1)

=======
Suggestion 7

def main():
    N, X = map(int, input().split())
    for i in range(1, N+1):
        V, P = map(int, input().split())
        X -= V*P/100
        if X < 0:
            print(i)
            return
    print(-1)

=======
Suggestion 8

def main():
    n, x = map(int,input().split())
    for i in range(n):
        v, p = map(int,input().split())
        x -= v * p / 100
        if x < 0:
            print(i+1)
            break
    else:
        print(-1)

=======
Suggestion 9

def main():
    N, X = map(int, input().split())
    alcohols = []
    for i in range(N):
        alcohols.append(list(map(int, input().split())))
    alcohol = 0
    for i in range(N):
        alcohol += alcohols[i][0] * alcohols[i][1] * 0.01
        if alcohol > X:
            print(i + 1)
            break
    else:
        print(-1)
