Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def main():
    L = int(input())
    N = 1
    M = 0
    while L > 0:
        N += 1
        L //= 2
        M += 1
    print(N, M)
    for i in range(1, N):
        print(i, i + 1, 0)
        print(i, i + 1, 2 ** (i - 1))
    L = int(input())
    for i in range(M - 1):
        if L & (1 << i):
            print(i + 1, i + 2, 2 ** i)
    return

=======
Suggestion 3

def main():
    L = int(input())
    N = 2
    M = 2
    print(N, M)
    print(1, 2, 0)
    print(1, 2, L)

=======
Suggestion 4

def solve():
    l = int(input())
    n = l + 1
    m = l * (l + 1) // 2
    print(n, m)
    for i in range(1, l + 1):
        print(i, i + 1, 0)
    for i in range(1, l):
        print(i, i + 1, l - i)

=======
Suggestion 5

def main():
    L = int(input())
    N = 0
    M = 0
    print(N, M)
    print(1, 2, 0)
    print(2, 3, 0)
    print(3, 4, 0)
    print(1, 5, 0)
    print(2, 6, 0)
    print(3, 7, 0)
    print(4, 8, 0)
    print(5, 6, 1)
    print(6, 7, 1)
    print(7, 8, 1)
