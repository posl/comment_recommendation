Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, k = map(int, input().split())
    print(0 if n % k == 0 else 1)

=======
Suggestion 2

def main():
    n,k = map(int,input().split())
    if n%k == 0:
        print(0)
    else:
        print(1)

=======
Suggestion 3

def solve():
    N,K = map(int, input().split())
    print(0 if N%K == 0 else 1)

=======
Suggestion 4

def calc_min_diff(n, k):
    if k == 1:
        return 0
    else:
        return n - k
