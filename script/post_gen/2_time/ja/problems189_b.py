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

=======
Suggestion 3

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
            print(i+1)
            return
    print(-1)

=======
Suggestion 5

def main():
    N, X = map(int, input().split())
    V = [0] * N
    P = [0] * N
    for i in range(N):
        V[i], P[i] = map(int, input().split())
    #print(N, X)
    #print(V)
    #print(P)
    #print(V[0])
    #print(P[0])
    #print(V[0] * P[0] / 100)
    #print(V[1])
    #print(P[1])
    #print(V[1] * P[1] / 100)
    #print(V[2])
    #print(P[2])
    #print(V[2] * P[2] / 100)
    #print(V[3])
    #print(P[3])
    #print(V[3] * P[3] / 100)
    #print(V[4])
    #print(P[4])
    #print(V[4] * P[4] / 100)
    #print(V[5])
    #print(P[5])
    #print(V[5] * P[5] / 100)
    #print(V[6])
    #print(P[6])
    #print(V[6] * P[6] / 100)
    #print(V[7])
    #print(P[7])
    #print(V[7] * P[7] / 100)
    #print(V[8])
    #print(P[8])
    #print(V[8] * P[8] / 100)
    #print(V[9])
    #print(P[9])
    #print(V[9] * P[9] / 100)
    #print(V[10])
    #print(P[10])
    #print(V[10] * P[10] / 100)
    #print(V[11])
    #print(P[11])
    #print(V[11] * P[11] / 100)
    #print(V[12])
    #print(P[12])
    #print(V[12] * P[12] / 100)
    #print(V[13])
    #print(P[13])
    #print(V[13] * P[13] / 100)
    #print(V[14])
    #

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
    A = 0
    for i in range(N):
        V, P = map(int, input().split())
        A += V * P
        if A > X * 100:
            print(i + 1)
            break
    else:
        print(-1)

=======
Suggestion 8

def main():
    N, X = map(int, input().split())
    ans = -1
    for i in range(N):
        V, P = map(int, input().split())
        X -= V*P/100
        if X < 0:
            ans = i + 1
            break
    print(ans)

=======
Suggestion 9

def main():
    N, X = map(int, input().split())
    ans = -1
    for i in range(N):
        v, p = map(int, input().split())
        X -= v * p / 100
        if X < 0:
            ans = i + 1
            break
    print(ans)
