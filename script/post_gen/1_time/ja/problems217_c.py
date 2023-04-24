Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    p = list(map(int, input().split()))
    q = [0]*n
    for i in range(n):
        q[p[i]-1] = i+1
    print(*q)

=======
Suggestion 2

def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = [0] * N
    for i in range(N):
        Q[P[i]-1] = i+1
    print(*Q)

=======
Suggestion 3

def main():
    n = int(input())
    p = list(map(int, input().split()))
    q = [0] * n
    for i in range(n):
        q[p[i]-1] = i+1
    print(" ".join(map(str, q)))

=======
Suggestion 4

def solve():
    n = int(input())
    p = list(map(int, input().split()))
    q = [0] * n
    for i in range(n):
        q[p[i]-1] = i+1
    print(*q)

=======
Suggestion 5

def main():
    N = int(input())
    P = list(map(int,input().split()))
    Q = [0]*N
    for i in range(N):
        Q[P[i]-1] = i+1
    print(' '.join(map(str,Q)))

=======
Suggestion 6

def main():
    n = int(input())
    p = list(map(int, input().split()))

    q = [0] * n
    for i in range(n):
        q[p[i]-1] = i+1

    print(' '.join(map(str, q)))

=======
Suggestion 7

def solve(n, p):
    q = [0] * n
    for i in range(n):
        q[p[i] - 1] = i + 1
    return q
