Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, k, a = map(int, input().split())
    if (k % n + a - 1) % n == 0:
        print(n)
    else:
        print((k % n + a - 1) % n)

=======
Suggestion 2

def main():
    n, k, a = map(int, input().split())
    if k % n == 0:
        print(a)
    else:
        print(a + k % n if a + k % n <= n else a + k % n - n)

=======
Suggestion 3

def main():
    N, K, A = map(int, input().split())
    if N >= K:
        if A <= K:
            print(A)
        else:
            print(A % K)
    else:
        if A <= K:
            print(A % N)
        else:
            print((A % K) % N)

=======
Suggestion 4

def main():
    N, K, A = map(int, input().split())
    if K <= N:
        print(K)
    else:
        print(K % N)

=======
Suggestion 5

def main():
    n,k,a = map(int,input().split())
    if n == a:
        print(k%n)
    else:
        if k%n == 0:
            print(n)
        else:
            print(k%n)

=======
Suggestion 6

def main():
    n, k, a = map(int, input().split())
    if k < n:
        print(k)
    else:
        print(k % n)

=======
Suggestion 7

def main():
    n, k, a = map(int, input().split())
    print((k - a) % n)

=======
Suggestion 8

def main():
    N, K, A = map(int, input().split())
    print(K%N)

=======
Suggestion 9

def main():
    n,k,a = map(int,input().split())
    print((k+n-a)%n+1)

=======
Suggestion 10

def main():
    # N,K,A = map(int,input().split())
    N,K,A = 3,3,2
    print(N,K,A)
