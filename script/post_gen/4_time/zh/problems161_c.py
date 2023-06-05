Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())

    while True:
        if N < K:
            break
        N = N % K

    if N > K/2:
        N = K - N

    print(N)

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    while N >= K:
        N = N % K
        if N > K/2:
            N = abs(N - K)
    print(N)

=======
Suggestion 3

def main():
    n,k = map(int,input().split())
    if n >= k:
        n = n%k
    if n > k/2:
        n = k-n
    print(n)

=======
Suggestion 4

def main():
    n,k = map(int,input().split())
    print(min(n%k,k-n%k))

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    if N % K == 0:
        print(0)
    else:
        print(1)

=======
Suggestion 6

def main():
    n, k = map(int, input().split())
    print(min(n%k, k-n%k))
    return

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    while N >= K:
        N = N - K
    if N < K:
        if N < K - N:
            print(N)
        else:
            print(K - N)

=======
Suggestion 8

def solve(n, k):
    while True:
        if n < k:
            return min(n, abs(n-k))
        else:
            n %= k
    return n

=======
Suggestion 9

def gcd(a,b):
    while b:
        a,b=b,a%b
    return a

n,k=map(int,input().split())
print(min(n%k,k-n%k))

=======
Suggestion 10

def main():
    N,K = map(int,input().split())
    if N%K == 0:
        print(0)
    else:
        print(min(N%K,abs(N%K-K)))
