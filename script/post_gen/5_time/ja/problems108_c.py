Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solve():
    N,K = map(int,input().split())
    ans = 0
    if K%2==0:
        for i in range(1,N+1):
            if i%K==0:
                ans += N//K
            elif i%K==K//2:
                ans += N//K
        print(ans**3)
    else:
        for i in range(1,N+1):
            if i%K==0:
                ans += N//K
        print(ans**3)

=======
Suggestion 2

def main():
    N,K = map(int,input().split())
    ans = 0
    if K%2 == 0:
        ans = (N//K)**3
        if N%K >= K//2:
            ans += (N//K+1)**3
    else:
        ans = (N//K)**3
    print(ans)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    if K % 2 == 0:
        K2 = K // 2
        print((N // K2) ** 3 + ((N + K2) // K2) ** 3)
    else:
        print((N // K) ** 3)

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    ans = 0
    if K % 2 == 0:
        ans += (N // K) ** 3
        if N >= K // 2:
            ans += ((N - K // 2) // K + 1) ** 3
    else:
        ans += (N // K) ** 3
    print(ans)

=======
Suggestion 5

def main():
    n,k = map(int,input().split())
    ans = 0
    if k % 2 == 0:
        ans = int(n/k)**3
        if k/2 <= n:
            ans += int((n-k/2)/k+1)**3
    else:
        ans = int(n/k)**3
    print(ans)

=======
Suggestion 6

def main():
    n,k = map(int,input().split())
    ans = 0
    if k%2 == 0:
        ans = (n//k)**3
        if n%k >= k//2:
            ans += ((n%k)-(k//2))**3
    else:
        ans = (n//k)**3
    print(ans)

=======
Suggestion 7

def main():
    N,K = map(int,input().split())
    ans = 0
    if K % 2 == 0:
        ans = (N // K) ** 3
        if N % K >= K // 2:
            ans += ((N % K) // (K // 2)) ** 3
    else:
        ans = (N // K) ** 3
    print(ans)

=======
Suggestion 8

def main():
    N, K = map(int, input().split())

    ans = 0
    if K % 2 == 0:
        ans = (N // K) ** 3 + ((N + K // 2) // K) ** 3
    else:
        ans = (N // K) ** 3

    print(ans)
    return

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    ans = 0
    if K % 2 == 0:
        ans = (N // K) ** 3 + ((N + K // 2) // K) ** 3
    else:
        ans = (N // K) ** 3
    print(ans)
