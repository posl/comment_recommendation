Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N-1):
        ans += min(A[i], A[i+1])
    ans += A[0]
    ans += A[-1]
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if i == 0:
            ans += A[i]
        else:
            ans += min(A[i], A[i-1])
    ans += A[N-1]
    print(ans)

=======
Suggestion 3

def problems173_d():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    result = 0
    for i in range(1, N):
        result += A[i // 2]
    print(result)

=======
Suggestion 4

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    result = 0
    for i in range(1, N):
        result += A[i//2]
    print(result)

=======
Suggestion 5

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    ans = 0
    for i in range(N-2):
        ans += A[i//2]
    print(ans)

=======
Suggestion 6

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.append(a[0])
    a.append(a[1])
    total = 0
    for i in range(1, n+1):
        total += abs(a[i] - a[i-1])
    for i in range(1, n+1):
        print(total - abs(a[i] - a[i-1]) - abs(a[i] - a[i+1]) + abs(a[i-1] - a[i+1]))

=======
Suggestion 7

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(1, n):
        ans += a[i] * (i - (n - i))
    print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    a.sort(reverse=True)
    total = 0
    for i in range(2, n):
        total += a[i // 2]
    print(total)

=======
Suggestion 9

def solve():
    N = int(input())
    A = list(map(int,input().split()))
    sum = 0
    for i in range(1,N):
        sum += min(A[i-1],A[i])
    print(sum+max(A[0],A[N-1]))

=======
Suggestion 10

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.insert(0, 0)
    A.append(0)

    #print(N)
    #print(A)

    # dp[i]: i番目までのプレイヤーが到着した時点での、最大の快適度
    dp = [0]*(N+2)

    for i in range(1, N+2):
        dp[i] = max(dp[i-1], dp[i-2] + abs(A[i] - A[i-2]))

    print(dp[N+1])

main()
