Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N,K = map(int, input().split())
    print(0 if N%K == 0 else 1)

=======
Suggestion 2

def get_min_diff(n, k):
    if k == 1:
        return 0
    else:
        return n - k

=======
Suggestion 3

def main():
    n, k = map(int, input().split())
    print(0 if n % k == 0 else 1)

=======
Suggestion 4

def main():
    n,k=map(int,input().split())
    if n%k==0:
        print(0)
    else:
        print(1)

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

def problems105_a():
    n,k = map(int,input().split())
    if(n%k == 0):
        print(0)
    else:
        print(1)

=======
Suggestion 7

def main():
    n,k = map(int,input().split())
    if n%k == 0:
        print(0)
    else:
        print(1)

main()
