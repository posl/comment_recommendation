Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(n - 1):
        b[a[i] - 1] += 1
    for i in range(n):
        print(b[i])

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in A:
        B[i-1] += 1
    for i in B:
        print(i)

=======
Suggestion 3

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [0] * n
    for i in range(1, n):
        b[a[i] - 1] += 1
    for i in range(n):
        print(b[i])

=======
Suggestion 4

def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    B = [0] * N
    for i in range(1, N):
        B[A[i] - 1] += 1
    for i in range(N):
        print(B[i])

=======
Suggestion 5

def main():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(1, n+1):
        print(a.count(i))

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = [0] + a
    ans = [0] * n
    for i in range(1, n + 1):
        ans[a[i] - 1] += 1
    for i in ans:
        print(i)

main()

=======
Suggestion 7

def main():
    n = int(input())
    a = [0] * n
    for i in map(int, input().split()):
        a[i - 1] += 1
    for x in a:
        print(x)

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a = [0] + a
    for i in range(1, n+1):
        print(a.count(i))
