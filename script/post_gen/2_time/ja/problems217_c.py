Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = [0] * N
    for i in range(N):
        Q[P[i] - 1] = i + 1
    print(*Q)

=======
Suggestion 2

def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = [0] * N
    for i, p in enumerate(P):
        Q[p - 1] = i + 1
    print(*Q)

=======
Suggestion 3

def main():
    n = int(input())
    p = list(map(int,input().split()))
    q = [0]*n
    for i in range(n):
        q[p[i]-1] = i+1
    print(*q)

=======
Suggestion 4

def main():
    N = int(input())
    P = [int(i) for i in input().split()]

    Q = [0] * N

    for i in range(N):
        Q[P[i] - 1] = i + 1

    print(*Q)

=======
Suggestion 5

def solve():
    # N = int(input())
    # P = list(map(int, input().split()))
    N = 5
    P = [5, 3, 2, 4, 1]
    Q = [0] * N
    for i in range(N):
        Q[P[i]-1] = i + 1
    print(Q)

solve()
