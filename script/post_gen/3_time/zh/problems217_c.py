Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    p = list(map(int, input().split()))
    q = [0] * n
    for i in range(n):
        q[p[i] - 1] = i + 1
    print(' '.join(map(str, q)))

=======
Suggestion 2

def main():
    N = int(input())
    P = [int(p) for p in input().split()]
    Q = [0] * N
    for i in range(N):
        Q[P[i] - 1] = i + 1
    print(" ".join(str(q) for q in Q))

=======
Suggestion 3

def main():
    n = int(input())
    p = list(map(int, input().split()))
    q = [0 for i in range(n)]
    for i in range(n):
        q[p[i]-1] = i+1
    print(*q)

=======
Suggestion 4

def main():
    n = int(input())
    p = list(map(int, input().split()))
    q = [0] * n
    for i in range(n):
        q[p[i] - 1] = i + 1
    print(" ".join(map(str, q)))

=======
Suggestion 5

def main():
    n = int(input())
    p = [int(i) for i in input().split()]
    q = [0]*n
    for i in range(n):
        q[p[i]-1] = i+1
    print(*q)

=======
Suggestion 6

def main():
    N = int(input())
    P = input().split()
    Q = [0] * N
    for i in range(N):
        Q[int(P[i])-1] = str(i+1)
    print(' '.join(Q))

=======
Suggestion 7

def solve():
    N = int(input())
    P = list(map(int, input().split()))
    Q = [0] * N

    for i in range(N):
        Q[P[i]-1] = i+1

    print(' '.join(map(str, Q)))

=======
Suggestion 8

def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = [0] * N
    for i in range(N):
        Q[P[i] - 1] = i + 1
    for i in range(N):
        print(Q[i], end=' ')

=======
Suggestion 9

def main():
    N = int(input())
    p = [int(x) for x in input().split()]
    q = [0]*N
    for i in range(N):
        q[p[i]-1] = i+1
    for i in range(N):
        print(q[i], end=" ")
    print()
