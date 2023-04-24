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
    for i in range(1, N):
        B[A[i-1]-1] += 1
    for i in range(N):
        print(B[i])

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N - 1):
        B[A[i] - 1] += 1
    for i in range(N):
        print(B[i])

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(1, n):
        b[a[i-1]-1] += 1
    for i in range(n):
        print(b[i])

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0] * N
    for i in range(N-1):
        ans[A[i]-1] += 1
    for i in ans:
        print(i)

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = [0] * N
    for a in A:
        ans[a-1] += 1
    for a in ans:
        print(a)

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    m = [0] * n
    for i in a:
        m[i-1] += 1
    for i in m:
        print(i)
