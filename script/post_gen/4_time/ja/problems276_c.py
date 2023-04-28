Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    p = list(map(int, input().split()))
    q = [0] * n
    for i in range(n):
        q[p[i]-1] = i+1
    print(*q)

=======
Suggestion 2

def main():
    n = int(input())
    p = list(map(int, input().split()))
    q = [0 for i in range(n)]
    for i in range(n):
        q[p[i]-1] = i+1
    print(*q)
main()

=======
Suggestion 3

def main():
    N = int(input())
    P = list(map(int,input().split()))
    Q = [0] * N
    for i in range(N):
        Q[P[i]-1] = i+1
    print(*Q)

=======
Suggestion 4

def main():
    N = int(input())
    P = [int(i) for i in input().split()]
    Q = [0] * N
    for i in range(N):
        Q[P[i]-1] = i+1
    print(*Q)

=======
Suggestion 5

def main():
    n = int(input())
    p = list(map(int,input().split()))
    q = []
    for i in range(n):
        q.append(0)
    for i in range(n):
        q[p[i]-1] = i+1
    print(" ".join(map(str,q)))

=======
Suggestion 6

def main():
    N = int(input())
    P = list(map(int, input().split()))
    P = [0] + P
    Q = [0] * (N + 1)
    for i in range(1, N + 1):
        Q[P[i]] = i
    print(*Q[1:])

=======
Suggestion 7

def calc(n, p):
    q = [0] * n
    for i in range(n):
        q[p[i] - 1] = i + 1
    return q

=======
Suggestion 8

def swap(li, a, b):
    tmp = li[a]
    li[a] = li[b]
    li[b] = tmp

=======
Suggestion 9

def main():
    n = int(input())
    p = list(map(int, input().split()))
    count = 0
    for i in range(n):
        count += p[i] * 10 ** i
    count -= 1
    q = list(map(int, str(count)))
    q.sort()
    q.reverse()
    for i in range(n):
        print(q[i], end=' ')
    print()
main()
