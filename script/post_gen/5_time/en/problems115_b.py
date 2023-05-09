Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    prices = []
    for i in range(n):
        prices.append(int(input()))
    prices.sort(reverse=True)
    prices[0] = int(prices[0] / 2)
    print(sum(prices))

=======
Suggestion 2

def main():
    N = int(input())
    p = [int(input()) for i in range(N)]
    p.sort()
    p[-1] = p[-1] // 2
    print(sum(p))

=======
Suggestion 3

def main():
    n = int(input())
    p = [int(input()) for _ in range(n)]
    print(sum(p) - max(p) // 2)

=======
Suggestion 4

def main():
    n = int(input())
    p = [int(input()) for i in range(n)]
    p.sort()
    print(int(sum(p[:-1]) + p[-1] / 2))

=======
Suggestion 5

def main():
    n = int(input())
    p = [int(input()) for i in range(n)]
    print(sum(p) - max(p) + max(p) // 2)

=======
Suggestion 6

def solve():
    N = int(input())
    items = [int(input()) for i in range(N)]
    items.sort()
    items[-1] = items[-1] // 2
    print(sum(items))

=======
Suggestion 7

def solve():
    n = int(input())
    p = [int(input()) for _ in range(n)]
    p.sort(reverse=True)
    return sum(p) - p[0]//2

print(solve())

=======
Suggestion 8

def main():
    N = int(input())
    p = [int(input()) for i in range(N)]
    p.sort()
    print(int(sum(p) - p[N - 1] / 2))

=======
Suggestion 9

def main():
    n = int(input())
    p = [int(input()) for _ in range(n)]
    max_p = max(p)
    total = sum(p)
    print((total - max_p) + (max_p // 2))
