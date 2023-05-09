Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solve(n):
    ans = 0
    for i in range(1,n):
        ans += n/i
    return ans

n = int(input())
print(solve(n))

=======
Suggestion 2

def solve():
    N = int(input())
    print((N * (N - 1)) / (2 * (N - 1)) + 1)

=======
Suggestion 3

def main():
    N = int(input())
    print((N * (N-1)) / (2 * (N-1)))

=======
Suggestion 4

def main():
    N = int(input())
    print((N * (N - 1)) / (N - 1))

=======
Suggestion 5

def main():
    N = int(input())
    print((N*(N-1))/2/(N-1) + 1)

=======
Suggestion 6

def main():
    n = int(input().strip())
    print(n * (n - 1) / (2 * (n - 1)) + 1.0)

=======
Suggestion 7

def main():
    N = int(input())
    print((N-1)*2/N)

=======
Suggestion 8

def main():
    N = int(input())
    print((N-1)*N/2/N+1)

=======
Suggestion 9

def main():
    N = int(input())
    print((N-1)*N/2 + 1)
