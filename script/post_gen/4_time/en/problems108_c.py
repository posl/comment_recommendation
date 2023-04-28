Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    if K % 2 == 0:
        print((N // K) ** 3 + ((N + K // 2) // K) ** 3)
    else:
        print((N // K) ** 3)

=======
Suggestion 2

def main():
    n, k = map(int, input().split())
    if k % 2 == 0:
        a = n // k
        b = (n + k // 2) // k
        print(a ** 3 + b ** 3)
    else:
        a = n // k
        print(a ** 3)

=======
Suggestion 3

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

=======
Suggestion 4

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

N, K = map(int, input().split())

ans = 0
for i in range(1, N+1):
    if i % K == 0:
        ans += N // K
    elif i % K * 2 == K:
        ans += N // K + 1
    else:
        ans += N // K + 1 - (N % K - i % K) // gcd(K, N % K)

print(ans)

=======
Suggestion 5

def solve(n, k):
    if k % 2 == 0:
        a = n // k
        b = (n + k // 2) // k
        return a * a * a + b * b * b
    else:
        a = n // k
        return a * a * a

=======
Suggestion 6

def main():
    n, k = map(int, input().split())
    ans = 0
    for i in range(1, n+1):
        if i%k == 0:
            ans += n//k
        elif i%k == k//2:
            ans += n//k + 1
    print(ans**3)

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    if K % 2 == 0:
        print(int((N//K)**3 + ((N+(K//2))//K)**3))
    else:
        print(int((N//K)**3))

=======
Suggestion 8

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

n,k = map(int, input().split())

=======
Suggestion 9

def main():
    n, k = map(int, input().split())
    count = 0
    if k % 2 == 0:
        count += (n//k)**3
        if n%k >= k//2:
            count += (n//k+1)**3
    else:
        count += (n//k)**3
    print(count)

main()

=======
Suggestion 10

def get_input():
    n, k = map(int, input().split())
    return n, k
