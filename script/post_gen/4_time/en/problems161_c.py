Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, K = map(int, input().split())
    if N % K == 0:
        print(0)
    else:
        print(min(N % K, abs(N % K - K)))

main()

=======
Suggestion 2

def main():
    N, K = map(int, input().split())
    if N % K == 0:
        print(0)
    else:
        print(min(N % K, abs(N % K - K)))

=======
Suggestion 3

def main():
    N, K = map(int, input().split())
    if N % K == 0:
        print(0)
    else:
        print(min(N % K, K - (N % K)))

=======
Suggestion 4

def main():
    N, K = map(int, input().split())
    if N % K == 0:
        print(0)
    else:
        print(1)

=======
Suggestion 5

def main():
    N, K = map(int, input().split())
    ans = N % K
    ans = min(ans, abs(ans - K))
    print(ans)

=======
Suggestion 6

def main():
    N, K = [int(i) for i in input().split()]
    if N % K == 0:
        print(0)
    else:
        print(1)

=======
Suggestion 7

def main():
    N, K = map(int, input().split())
    if K == 1:
        print(0)
    else:
        print(min(N % K, K - N % K))

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    ans = N % K
    print(min(ans, abs(ans - K)))

=======
Suggestion 9

def f(n,k):
    if n%k==0:
        return 0
    else:
        return min(n%k,k-n%k)

n,k=map(int,input().split())
print(f(n,k))

=======
Suggestion 10

def main():
    n, k = map(int, input().split())
    mod = n % k
    print(min(mod, k - mod))
