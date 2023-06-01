Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(n):
        b[a[i] - 1] = i + 1
    print(*b)

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(n):
        b[a[i]-1] = i + 1
    print(' '.join(map(str, b)))

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    r = []
    for i in range(n):
        r.insert(a[i] - 1, i + 1)
    print(' '.join(map(str, r)))

=======
Suggestion 4

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [0] * n
    for i in range(n):
        b[a[i] - 1] = i + 1
    print(' '.join([str(x) for x in b]))

=======
Suggestion 5

def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    order = [0 for _ in range(n)]
    for i in range(n):
        order[a_list[i] - 1] = i + 1
    print(' '.join(map(str, order)))

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(n):
        b[a[i] - 1] = i + 1
    for i in range(n):
        print(b[i], end=" ")

=======
Suggestion 7

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N):
        B[A[i]-1] = i+1
    print(*B)

=======
Suggestion 8

def order(n, a):
    b = [0] * n
    for i in range(n):
        b[a[i] - 1] = i + 1
    return b
