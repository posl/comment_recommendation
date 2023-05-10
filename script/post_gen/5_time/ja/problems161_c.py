Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())

    if N > K:
        N = N % K

    if N > abs(N-K):
        N = abs(N-K)

    print(N)

main()

=======
Suggestion 2

def main():
    N,K = map(int,input().split())
    ans = N%K
    ans = min(ans,abs(ans-K))
    print(ans)

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    ans = N
    while True:
        if ans > abs(ans-K):
            ans = abs(ans-K)
        else:
            break
    print(ans)

=======
Suggestion 4

def main():
    n, k = map(int, input().split())
    print(n % k if n % k < k - n % k else k - n % k)

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    ans = n % k
    if ans > k:
        ans = k - ans
    print(ans)

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    print(N%K if N>K else min(N, abs(N-K)))

=======
Suggestion 7

def main():
    n, k = map(int, input().split())
    while n >= k:
        n = n % k
        n = abs(n-k)
    print(n)

=======
Suggestion 8

def main():
    n, k = map(int, input().split())
    print(n % k if n % k <= k // 2 else k - n % k)

=======
Suggestion 9

def main():
    N, K = map(int, input().split())
    print(min(N % K, K - N % K))

=======
Suggestion 10

def solve():
    N, K = map(int, input().split())
    ans = N % K
    ans = min(ans, K - ans)
    print(ans)
