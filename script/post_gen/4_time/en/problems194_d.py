Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    ans = 0
    for i in range(1, N):
        ans += N / (N - i)
    print(ans)

=======
Suggestion 2

def main():
    n = int(input())
    res = 0
    for i in range(1,n):
        res += n/(n-i)
    print(res)

=======
Suggestion 3

def main():
    N = int(input())
    print((N * (N - 1)) / (2 * (N - 1)))

=======
Suggestion 4

def main():
    n = int(input())
    print((n * (n-1)) / (2 * (n-1)) + 1)

=======
Suggestion 5

def main():
    N = int(input())
    print((N*(N-1))/2/(N-1)+1)

=======
Suggestion 6

def main():
    N = int(input())
    print((N-1)*(1+sum([1/i for i in range(2,N+1)])))

=======
Suggestion 7

def main():
    N = int(input())
    print(2*(N-1)/N)

=======
Suggestion 8

def main():
    N = int(input())
    print((N-1)*N/2/N+1)

=======
Suggestion 9

def main():
    N = int(input())
    print((N*2)/3)

=======
Suggestion 10

def solve(n):
    return sum([i*(1/n) for i in range(1,n+1)])
