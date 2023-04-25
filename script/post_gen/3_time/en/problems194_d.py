Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    ans = 0
    for i in range(1, N + 1):
        ans += i * (1 / N) ** i
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
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        ans += (N/i)
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    ans = N
    for i in range(1, N):
        ans += i * (N / i)
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    print(sum([i * (1 / N) ** i for i in range(1, N + 1)]))

=======
Suggestion 6

def main():
    N = int(input())
    print(N + (N - 1) / 2)

=======
Suggestion 7

def main():
    N = int(input())
    print((N - 1) + 1 / N * (N - 1))

=======
Suggestion 8

def main():
    n = int(input())
    print(n + sum([1/i for i in range(2, n)]))

=======
Suggestion 9

def main():
    N = int(input())
    print(N*(N+1)/2/N)

=======
Suggestion 10

def main():
    N = int(input())
    print(2 * N - 1 + 1 / N)
