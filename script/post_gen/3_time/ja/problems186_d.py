Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N-1):
        for j in range(i+1,N):
            ans += abs(A[i] - A[j])
    print(ans)

=======
Suggestion 2

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        ans += A[i] * (2 * i - N + 1)
    print(ans)

=======
Suggestion 3

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        ans += A[i] * (N - i - 1) - A[i] * i
    print(ans * 2)

=======
Suggestion 4

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        ans += A[i] * i - sum(A[:i])
        ans -= A[i] * (N - i - 1) - sum(A[i + 1:])
    print(ans)
    return 0

=======
Suggestion 5

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        ans += A[i] * (i - (N - i - 1))
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    s = 0
    for i in range(n-1):
        s += (a[i+1] - a[i]) * (i+1) * (n-i-1)
    print(s)

=======
Suggestion 7

def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    if N % 2 == 0:
        ans = 2 * sum(A[N//2:]) - 2 * sum(A[:N//2]) - A[N//2] + A[N//2-1]
    else:
        ans = 2 * sum(A[N//2+1:]) - 2 * sum(A[:N//2]) + max(A[N//2] - A[N//2-1], A[N//2+1] - A[N//2])
    print(ans)

=======
Suggestion 8

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = sum(a[i] * (2 * i - n + 1) for i in range(n))
    print(ans)

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    ans = 0
    for i in range(N):
        ans += (2*(i+1)-N-1)*A[i]
    print(ans)

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))

    A.sort()
    #print(A)
    ans = 0
    for i in range(N):
        ans += A[i] * (i+1) - A[i] * (N-i-1)
    print(ans)
main()
