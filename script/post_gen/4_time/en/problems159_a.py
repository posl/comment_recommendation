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
    if n == 0 or m == 0:
        print(0)
    elif n == 1 and m == 1:
        print(0)
    elif n == 1 or m == 1:
        print(max(n, m) - 2)
    else:
        print((n - 2) * (m - 2))

=======
Suggestion 3

def main():
    n, m = map(int, input().split())
    if n == 0 or m == 0:
        print(0)
    elif n == 1 and m == 1:
        print(0)
    else:
        print(n * m - 1)

=======
Suggestion 4

def main():
    N, M = map(int, input().split())
    print(N*(N-1)//2 + M*(M-1)//2)

=======
Suggestion 5

def main():
    n, m = map(int, input().split())
    if n == 0 or m == 0:
        print(0)
    else:
        print(n * m)

=======
Suggestion 6

def main():
    n, m = map(int, input().split())
    print(n*(n-1)//2 + m*(m-1)//2)

main()

=======
Suggestion 7

def solve():
    n, m = map(int, input().split())
    print((n*(n-1)+m*(m-1))//2)
