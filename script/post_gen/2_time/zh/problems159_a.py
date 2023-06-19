Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    print(N * (N - 1) // 2 + M * (M - 1) // 2)

=======
Suggestion 2

def solve(n,m):
    res = 0
    if n>0:
        res += n * (n-1) // 2
    if m>0:
        res += m * (m-1) // 2
    return res

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    print(n * (n - 1) // 2 + m * (m - 1) // 2)

=======
Suggestion 4

def main():
    n,m = map(int,input().split())
    print((n*(n-1)+m*(m-1))//2)

=======
Suggestion 5

def main():
    N,M = map(int,input().split())
    print((N*(N-1)+M*(M-1))//2)
