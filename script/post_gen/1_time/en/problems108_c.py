Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    ans = 0
    if K % 2 == 0:
        for i in range(1, N+1):
            if i % K == 0:
                ans += 1
        ans = ans ** 3
    else:
        for i in range(1, N+1):
            if i % K == 0:
                ans += 1
        ans = ans ** 3
        for i in range(1, N+1):
            if (i + K // 2) % K == 0:
                ans += 1
        ans = ans ** 3
    print(ans)

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    if k % 2 == 0:
        print((n // k) ** 3 + ((n + k // 2) // k) ** 3)
    else:
        print((n // k) ** 3)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    ans = 0
    if K%2 == 1:
        ans = (N//K)**3
    else:
        ans = (N//K)**3 + ((N+K//2)//K)**3
    print(ans)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    ans = 0
    if K % 2 == 0:
        ans += (N // K) ** 3
        if N % K >= K // 2:
            ans += (N // K + 1) ** 3
    else:
        ans += (N // K) ** 3
    print(ans)

main()

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    ans = 0
    if K % 2 == 0:
        ans += (N//K)**3
        if N % K >= K//2:
            ans += (N//K+1)**3
    else:
        ans += (N//K)**3
    print(ans)

=======
Suggestion 6

def main():
    n,k = map(int, input().split())
    ans = 0
    if k%2 == 0:
        ans += (n//k)**3
        if n%k >= k//2:
            ans += (n//k+1)**3
    else:
        ans += (n//k)**3
    print(ans)

=======
Suggestion 7

def check(n, k):
    if k % 2 == 0:
        return n // k * n // k * n // k + (n // k + 1) * (n // k + 1) * (n // k + 1)
    else:
        return n // k * n // k * n // k

n, k = map(int, input().split())
print(check(n, k))

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    if K % 2 == 0:
        n = N // K
        if N % K >= K // 2:
            print((n + 1) ** 3 + n ** 3)
        else:
            print((n + 1) ** 3 + (n - 1) ** 3)
    else:
        n = N // K
        print(n ** 3)

=======
Suggestion 9

def main():
    n,k = map(int, input().split())
    if k%2 == 0:
        count = int(n/k)**3
        if k <= n:
            count += int((n-k//2)/k)**3
    else:
        count = int(n/k)**3
    print(count)

=======
Suggestion 10

def get_input():
    return map(int, input().rstrip().split())
