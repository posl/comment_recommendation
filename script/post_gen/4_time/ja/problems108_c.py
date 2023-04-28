Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    # input
    N, K = map(int, input().split())

    # compute
    ans = 0
    for a in range(1, N+1):
        if a % K == 0:
            ans += N
        else:
            tmp = N // K
            if (a + K//2) % K == 0:
                ans += tmp**3
            else:
                ans += tmp**3 * 2

    # output
    print(ans)

=======
Suggestion 2

def solve():
    N, K = map(int, input().split())
    ans = 0
    if K % 2 == 0:
        ans = (N // K) ** 3
        if N >= K // 2:
            ans += ((N - K // 2) // K + 1) ** 3
    else:
        ans = (N // K) ** 3
    print(ans)

=======
Suggestion 3

def solve():
    N, K = map(int, input().split())
    ans = 0
    if K % 2 == 0:
        ans = (N//K)**3 + (N//(K//2) - N//K)**3
    else:
        ans = (N//K)**3
    print(ans)

=======
Suggestion 4

def solve():
    N, K = map(int, input().split())
    if K % 2 == 0:
        a = N // K
        b = N // (K // 2) - a
        print(a**3 + b**3)
    else:
        a = N // K
        print(a**3)

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    ans = 0
    for a in range(1, N+1):
        if a%K == 0:
            ans += (N//K)**3
        elif a%K == K//2:
            ans += (N//K+1)**3
    print(ans)

=======
Suggestion 6

def main():
    n, k = map(int, input().split())
    if k % 2 == 0:
        count = n // k
        count = count ** 3
        count += (n // (k // 2) - count) ** 3
    else:
        count = n // k
        count = count ** 3
    print(count)

=======
Suggestion 7

def calc(n, k):
    if k % 2 == 0:
        a = n // k
        b = n // (k // 2) - a
        c = n // (k // 2) - a
        return a ** 3 + b ** 3 + c ** 3
    else:
        a = n // k
        b = n // (k // 2) - a
        c = n // (k // 2) - a
        d = n // (k // 2 + 1) - a
        return a ** 3 + b ** 3 + c ** 3 + d ** 3

n, k = map(int, input().split())
print(calc(n, k))

=======
Suggestion 8

def main():
    n,k = map(int,input().split())
    ans = 0
    for a in range(1,n+1):
        if a%k == 0:
            ans += n//k
        elif a%k <= k//2:
            ans += n//k
        else:
            ans += n//k + 1
    print(ans**3)

=======
Suggestion 9

def main():
    N,K = map(int,input().split())
    ans = 0
    if K%2 == 0:
        ans += (N//K)**3
        if (N+K//2)%K < K:
            ans += (N+K//2)//K
        print(ans)
    else:
        print((N//K)**3)

=======
Suggestion 10

def calc(n,k):
    if k%2==0:
        tmp = n//k
        return tmp**3 + (n+k//2)//k**3
    else:
        tmp = n//k
        return tmp**3

n,k = map(int,input().split())
ans = calc(n,k)
print(ans)
