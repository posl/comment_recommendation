Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N - 1):
        B[A[i] - 1] += 1
    print(*B, sep='

')

=======
Suggestion 2

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = [0] * n
    for i in range(n - 1):
        ans[a[i] - 1] += 1
    for i in range(n):
        print(ans[i])

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in range(N-1):
        B[A[i]-1] += 1
    for i in range(N):
        print(B[i])

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(n-1):
        b[a[i]-1] += 1
    for i in range(n):
        print(b[i])

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = [0] * N
    for i in A:
        B[i - 1] += 1
    for i in B:
        print(i)

main()

import sys
from collections import deque

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    sub = [0] * N
    for i in range(N - 1):
        sub[A[i] - 1] += 1
    for i in range(N):
        print(sub[i])

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    subordinates = [0] * N
    for i in range(1, N):
        subordinates[A[i-1]-1] += 1
    for i in range(N):
        print(subordinates[i])

=======
Suggestion 8

def main():
    n = int(input())
    a = list(map(int, input().split()))
    sub = [0 for i in range(n)]
    for i in range(n-1):
        sub[a[i]-1] += 1
    for i in range(n):
        print(sub[i])

=======
Suggestion 9

def main():
    n = int(input())
    a = [0] + list(map(int, input().split()))
    ans = [0 for _ in range(n+1)]
    for i in range(2, n+1):
        ans[a[i]] += 1
    for i in range(1, n+1):
        print(ans[i])

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.insert(0, 0)
    B = [0] * (N + 1)

    for i in range(N):
        B[A[i + 1]] += 1

    for i in range(1, N + 1):
        print(B[i])
