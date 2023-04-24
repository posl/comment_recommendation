Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.reverse()
    ans = 0
    for i in range(n-1):
        if a[i] <= a[i+1]:
            continue
        ans += a[i] - a[i+1]
        a[i+1] = a[i]
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.reverse()
    ans = 0
    for i in range(N - 1):
        if A[i] <= A[i + 1]:
            continue
        else:
            ans += A[i] - A[i + 1]
            A[i + 1] = A[i]
    print(ans)

=======
Suggestion 3

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if i == 0:
            ans += A[i]
        else:
            if A[i] > A[i-1]:
                ans += A[i] - A[i-1]
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += max(0, A[i] - i)
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [0] + A
    dp = [0] * (N + 1)
    for i in range(1, N + 1):
        dp[i] = max(dp[i - 1], A[i])
    ans = 0
    for i in range(1, N + 1):
        ans += dp[i] - A[i]
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    A = [int(x) for x in input().split()]
    A.reverse()
    ans = 0
    for i in range(N-1):
        if A[i] <= A[i+1]:
            ans += A[i+1] - A[i]
        else:
            ans += A[i+1]
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        ans += max(0, A[i] - (N - 1 - i))
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = [0] + A
    count = 0
    for i in range(N, 0, -1):
        if A[i] <= A[i-1]:
            count += A[i-1] - A[i] + 1
            A[i-1] = A[i] - 1
    print(count)

main()

This is a solution for the following problem.

=======
Suggestion 9

def main():
    N = int(input())
    A = list(map(int, input().split()))
    height = 0
    for i in range(N):
        if A[i] > A[i-1]:
            height += A[i] - A[i-1]
    print(height)

=======
Suggestion 10

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.reverse()
    max_height = 0
    for i in range(n):
        if a[i] < max_height:
            print("No")
            return
        if a[i] > max_height:
            max_height = a[i]
            a[i] -= 1
    print("Yes")
