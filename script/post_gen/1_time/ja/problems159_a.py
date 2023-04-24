Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n, m = map(int, input().split())
    print(n * (n - 1) // 2 + m * (m - 1) // 2)

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    print((n * (n - 1) // 2) + (m * (m - 1) // 2))

=======
Suggestion 3

def main():
    N, M = map(int, input().split())
    print(N * (N - 1) // 2 + M * (M - 1) // 2)

=======
Suggestion 4

def main():
    n,m = map(int,input().split())
    if n == 0 or m == 0:
        print(0)
        return
    if n == 1 and m == 1:
        print(0)
        return
    if n == 1:
        print(m)
        return
    if m == 1:
        print(n)
        return
    print(n*m-n-m+1)
    return

=======
Suggestion 5

def main():
    N, M = map(int, input().split())
    print((N*(N-1)//2)+(M*(M-1)//2))

=======
Suggestion 6

def main():
    # input
    N, M = map(int, input().split())

    # compute
    ans = N * (N - 1) // 2
    ans += M * (M - 1) // 2

    # output
    print(ans)

=======
Suggestion 7

def solve():
    N,M = map(int,input().split())
    print(N*(N-1)//2+M*(M-1)//2)

=======
Suggestion 8

def solve():
    N, M = map(int, input().split())
    print(N*M)
