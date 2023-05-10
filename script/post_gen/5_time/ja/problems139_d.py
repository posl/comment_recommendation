Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    print(int(n*(n-1)/2))
main()

=======
Suggestion 2

def main():
    n = int(input())
    print((n*(n-1))//2)
    return

=======
Suggestion 3

def main():
    N = int(input())
    if N == 1:
        print(0)
    else:
        print(N * (N - 1) // 2)

=======
Suggestion 4

def solve():
    n = int(input())
    print((n*(n-1))//2)

=======
Suggestion 5

def main():
    n = int(input())
    print(n*(n-1)//2)

=======
Suggestion 6

def solve():
    N = int(input())
    ans = 0

    if N == 1:
        print(0)
        return

    if N % 2 == 0:
        ans = N // 2 * (N - 1)
    else:
        ans = (N - 1) // 2 * N

    print(ans)

=======
Suggestion 7

def main():
    n = int(input())
    print((n*(n-1))//2)

=======
Suggestion 8

def solve():
    n = int(input())
    print(n*(n-1)//2)
    return 0

=======
Suggestion 9

def main():
    N = int(input())
    print(N*(N-1)//2)
