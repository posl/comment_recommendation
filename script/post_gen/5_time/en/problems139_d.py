Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def solve(N: int):
    ans = 0
    for i in range(1, N+1):
        ans += i - 1
    return ans

=======
Suggestion 2

def main():
    n = int(input())
    print(n * (n - 1) // 2)

=======
Suggestion 3

def main():
    N = int(input())
    print(N*(N-1)//2)

=======
Suggestion 4

def solve():
    n = int(input())
    if n == 1:
        print(0)
    else:
        print(sum(range(1, n)))

solve()

=======
Suggestion 5

def calc(n):
    a = n // 2
    b = n % 2
    return a * (a + 1) + b

n = int(input())
print(calc(n))

=======
Suggestion 6

def solve(N: int):
    return sum(range(1, N))
