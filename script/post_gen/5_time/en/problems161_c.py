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

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

N,K = map(int,input().split())
print(min(N%K,K-N%K))

=======
Suggestion 3

def main():
    n, k = [int(i) for i in input().split()]
    while n >= k:
        n = n % k
        if n == 0:
            print(0)
            return
    print(min(n, abs(n-k)))

=======
Suggestion 4

def main():
    n, k = map(int, input().split())
    print(min(n % k, abs(n % k - k)))

=======
Suggestion 5

def main():
    n, k = map(int, input().split())
    ans = 0
    while n >= k:
        n = n % k
        ans = n
    print(min(ans, abs(ans-k)))

=======
Suggestion 6

def main():
    N, K = map(int, input().split())
    print(min(N % K, K - (N % K)))

=======
Suggestion 7

def main():
    N, K = map(int, input().split())

    if N == 0:
        print(0)
        return

    N = N % K
    print(min(N, K-N))

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    if N < K:
        print(N)
    else:
        print(N % K)

=======
Suggestion 9

def main():
    n, k = map(int, input().split())
    print(min(n%k, k-n%k))

main()
