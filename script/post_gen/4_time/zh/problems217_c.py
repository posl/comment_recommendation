Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    p = list(map(int, input().split()))

    q = [0] * N
    for i in range(N):
        q[p[i] - 1] = i + 1

    for i in range(N):
        print(q[i], end=" ")
    print()

=======
Suggestion 2

def main():
    n = int(input())
    p = list(map(int, input().split()))
    q = [0]*n
    for i in range(n):
        q[p[i]-1] = i+1
    print(*q)

=======
Suggestion 3

def solve():
    N = int(input())
    P = list(map(int,input().split()))
    Q = [0]*N
    for i in range(N):
        Q[P[i]-1] = i+1
    print(*Q)

=======
Suggestion 4

def main():
    n = int(input())
    p = input().split()
    q = [0] * n
    for i in range(n):
        q[int(p[i])-1] = i+1
    print(' '.join(map(str, q)))

=======
Suggestion 5

def main():
    n = int(input())
    p = [int(i) for i in input().split()]
    q = [0]*n
    for i in range(n):
        q[p[i]-1] = i+1
    for i in range(n):
        print(q[i],end=' ')
    print()

=======
Suggestion 6

def main():
    N = int(input())
    p = list(map(int, input().split()))
    q = [0]*N
    for i in range(N):
        q[p[i]-1] = i+1
    print(' '.join(map(str, q)))

=======
Suggestion 7

def main():
    N = int(input())
    p = list(map(int, input().split()))
    q = [0] * N
    for i in range(N):
        q[p[i]-1] = i + 1
    print(*q)

=======
Suggestion 8

def main():
    n = int(input())
    p = list(map(int, input().split()))

    q = [0] * n
    for i in range(n):
        q[p[i] - 1] = i + 1

    print(' '.join(map(str, q)))
