Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, M = map(int, input().split())
    print(N * (N - 1) // 2 + M * (M - 1) // 2)

=======
Suggestion 2

def main():
    n, m = map(int, input().split())
    if n == 0:
        print(m)
    elif m == 0:
        print(n)
    else:
        print((n * (n - 1) // 2) + (m * (m - 1) // 2))

=======
Suggestion 3

def main():
    n,m = map(int,input().split())
    if n == 0:
        print(m)
    elif m == 0:
        print(n)
    else:
        print(n*m)

=======
Suggestion 4

def main():
    # read input
    N, M = map(int, input().split())
    # calculate
    if N == 0:
        print(M)
    elif M == 0:
        print(N)
    else:
        print(N * M)
