Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    if n % k == 0:
        print(0)
    else:
        print(1)

=======
Suggestion 2

def main():
    n,k = map(int,input().split())
    print(0 if n%k == 0 else 1)

=======
Suggestion 3

def main():
    n,k=map(int,input().split())
    print(n%k)

=======
Suggestion 4

def problems105_a():
    n,k = map(int,input().split())
    print(0 if n%k==0 else 1)

=======
Suggestion 5

def problems105_a():
    N,K = map(int, input().split())
    print(N%K)

=======
Suggestion 6

def min_diff(N, K):
    if K == 1:
        return 0
    else:
        return N - K

=======
Suggestion 7

def main():
    n, k = map(int, input().split())
    ans = 0
    if n % k != 0:
        ans = 1
    print(ans)

=======
Suggestion 8

def main():
    N, K = map(int, input().split())
    print(0 if N % K == 0 else 1)
