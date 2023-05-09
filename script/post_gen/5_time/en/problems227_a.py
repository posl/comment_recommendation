Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, k, a = map(int, input().split())
    if k % n == 0:
        print(0)
    else:
        print(1)

=======
Suggestion 2

def main():
    n, k, a = map(int, input().split())
    print((k-n+a)//(n-1)+1 if (k-n+a)%(n-1) else (k-n+a)//(n-1))

=======
Suggestion 3

def main():
    n, k, a = map(int, input().split())
    if k <= n:
        print(k)
    else:
        print(k%n)

=======
Suggestion 4

def main():
    # input
    N, K, A = map(int, input().split())

    # compute

    # output
    if K < N:
        print(K)
    else:
        print(K % N)

=======
Suggestion 5

def main():
    n, k, a = map(int, input().split())
    if k <= n:
        print(k)
    else:
        print(n - (k % n))

=======
Suggestion 6

def main():
    n, k, a = map(int, input().split())
    if k <= n:
        print(k)
    else:
        k -= n
        print(n - k % n if k % n != 0 else n)

=======
Suggestion 7

def main():
    N,K,A = map(int, input().split())
    if K <= N:
        print(K)
    else:
        K = K - N
        print(N - (K % N))

=======
Suggestion 8

def main():
    n,k,a = map(int, input().split())
    if k <= (n-a):
        print(a+k)
    else:
        print(k-(n-a))

=======
Suggestion 9

def main():
    N, K, A = map(int, input().split())
    print((K//N + (K%N >= A))*N - (K%N < A)*(N-A))

=======
Suggestion 10

def main():
    n,k,a = map(int, input().split())
    print((k//n) + (k%n >= a))
