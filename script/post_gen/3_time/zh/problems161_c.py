Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    while True:
        if n > abs(n-k):
            n = abs(n-k)
        else:
            print(n)
            break

=======
Suggestion 2

def main():
    N,K = map(int,input().split())
    if N%K == 0:
        print(0)
    else:
        print(1)

=======
Suggestion 3

def main():
    n, k = map(int, input().split())
    print(min(n%k, k-n%k))

=======
Suggestion 4

def main():
    n,k = map(int,input().split())
    while True:
        if n > k:
            n = n%k
        else:
            break
    print(min(n,abs(n-k)))

=======
Suggestion 5

def solve(n,k):
    while n>=k:
        n=n%k
        if n==0:
            return 0
        elif n>k/2:
            n=k-n
    return n

n,k=map(int,input().split())
print(solve(n,k))

=======
Suggestion 6

def min_value(n, k):
    if n == 0:
        return 0
    return min(n % k, k - n % k)

=======
Suggestion 7

def problem161_c():
    n, k = map(int, input().split())
    print(min(n % k, k - n % k))

problem161_c()

=======
Suggestion 8

def main():
    N,K = map(int,input().split())
    if N % K == 0:
        print(0)
    else:
        print(min(N % K,abs(K-(N % K))))

=======
Suggestion 9

def main():
    n, k = map(int, input().split())
    n = n % k
    print(min(n, abs(n-k)))
