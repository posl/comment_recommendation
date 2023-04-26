Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    ans = n % k
    ans = min(ans, k - ans)
    print(ans)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    while N >= K:
        N = N % K
        if N > K / 2:
            N = K - N
    print(N)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    print(min(N%K, K-N%K))

=======
Suggestion 4

def main():
    n, k = map(int, input().split())
    print(min(n%k, k-n%k))

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    print(n % k if n % k < k else abs(n % k - k))

=======
Suggestion 6

def main():
    n,k = map(int, input().split())
    ans = n % k
    ans = min(ans, abs(ans-k))
    print(ans)

=======
Suggestion 7

def main():
    n,k = map(int, input().split())
    n = n % k
    print(min(n, k-n))

=======
Suggestion 8

def main():
    n,k = map(int, input().split())
    n %= k
    print(min(n, abs(n-k)))

=======
Suggestion 9

def solve(n, k):
    return min(n % k, k - (n % k))
