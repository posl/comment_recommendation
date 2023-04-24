Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n, k, a = map(int, input().split())
    if (k - a) % (n - 1) == 0:
        print(n)
    else:
        print((k - a) % (n - 1) + a)

=======
Suggestion 2

def main():
    n, k, a = map(int, input().split())
    if k <= n:
        print(k)
    else:
        if (k - n) % (n - 1) == 0:
            print(n)
        else:
            print((k - n) % (n - 1) + 1)

=======
Suggestion 3

def main():
    N, K, A = map(int, input().split())
    if K > N:
        K = K % N
    if (A + K) > N:
        print(K - (N - A))
    else:
        print(A + K)

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

def problem227_a():
    n, k, a = map(int, input().split())
    if k <= n:
        print(k)
    else:
        print(k%n)

=======
Suggestion 6

def last_card():
    N, K, A = map(int, input().split())
    if N == K:
        print(1)
    elif (K-A)%(N-A) == 0:
        print(N)
    else:
        print((K-A)%(N-A))
last_card()

=======
Suggestion 7

def main():
    n,k,a = map(int, input().split())
    if k <= n:
        print(k)
    else:
        print(n-k%n+a)

=======
Suggestion 8

def main():
    N,K,A = map(int,input().split())
    if K <= N:
        print(K)
    elif K > N:
        print(N - (K - N))

=======
Suggestion 9

def main():
    n,k,a = map(int, input().split())
    cards = k//n
    if k%n >= a:
        cards += 1
    print(cards)

=======
Suggestion 10

def last_card(N,K,A):
    if N <= K:
        return 1
    else:
        if (N % K) == 0:
            return 0
        else:
            return 1
