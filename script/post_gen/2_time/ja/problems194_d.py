Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    ans = 0
    for i in range(1,n):
        ans += n/(n-i)
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    ans = 0
    for i in range(1, N):
        ans += (N / i)
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    a = 0
    for i in range(1, n):
        a += n/(n-i)
    print(a)

=======
Suggestion 4

def main():
    n = int(input())
    print((n * (n - 1)) / (2 * (n - 1)) + 1)

main()

=======
Suggestion 5

def main():
    N = int(input())
    print((N * (N - 1)) / (2 * N - 2))

=======
Suggestion 6

def main():
    n = int(input())
    print((n * (n-1)) / (2 * (n-1)) + 1)

=======
Suggestion 7

def main():
    N = int(input())
    # print(N)
    ans = 0.0
    for i in range(1,N):
        ans += N/(N-i)
    print(ans)

=======
Suggestion 8

def main():
    n = int(input())
    print((n-1)*2/n)

=======
Suggestion 9

def solve():
    n = int(input())
    print((n-1)*2/n)

=======
Suggestion 10

def main():
    n = int(input())
    print((n/(n-1))*n)
