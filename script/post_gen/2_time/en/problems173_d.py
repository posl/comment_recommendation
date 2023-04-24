Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(1, N):
        ans += A[i] * (N - i)
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N-1):
        ans += A[i] * (N-i-1)
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    sum = 0
    for i in range(n-2):
        sum += a[i]
    print(sum)

=======
Suggestion 4

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        ans += a[i] * (n - 2 * i - 1)
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()

    if N % 2 == 0:
        print(sum(A[N//2:]) - sum(A[:N//2]))
    else:
        print(sum(A[N//2+1:]) - sum(A[:N//2]))

=======
Suggestion 6

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    if N == 2:
        print(A[0])
        return
    ans = A[0] + A[1]
    for i in range(2, N):
        ans += A[i] * (i // 2)
    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        ans += a[i] * (i - 1)
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    print(sum(A[0:N-1]) + A[N-1]//2)

=======
Suggestion 9

def main():
    N = int(input())
    A = [int(i) for i in input().split()]
    A.sort()
    print(sum(A[0:N-1]))

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    print(A[N-2])
