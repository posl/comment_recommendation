Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def calc(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return n * (n - 1) // 2

n = int(input())
print(calc(n))

=======
Suggestion 2

def main():
    N = int(input())
    ans = N * (N - 1) // 2
    print(ans)

=======
Suggestion 3

def solve():
    N = int(input())
    ans = 0
    for i in range(1, N+1):
        ans += i-1
    print(ans)

=======
Suggestion 4

def calc(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n % 2 == 0:
        return (n // 2) * (n - 1)
    else:
        return n * ((n - 1) // 2)

=======
Suggestion 5

def main():
    N = int(input())
    print((N*(N-1))//2)

=======
Suggestion 6

def main():
    N = int(input())
    print(N * (N - 1) // 2)

=======
Suggestion 7

def main():
    n = int(input())
    print((n - 1) * n // 2)

=======
Suggestion 8

def solve():
    n = int(input())
    print((n-1)*n//2)

=======
Suggestion 9

def main():
    N = int(input())
    print((N*(N-1)//2))
