Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    p = [int(input()) for _ in range(n)]
    p.sort(reverse=True)
    ans = p[0] // 2
    for i in range(1, n):
        ans += p[i]
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    P = [int(input()) for _ in range(N)]
    P.sort(reverse=True)
    total = 0
    for i in range(N):
        if i == 0:
            total += P[i] // 2
        else:
            total += P[i]
    print(total)

=======
Suggestion 3

def main():
    N = int(input())
    p = [int(input()) for i in range(N)]
    p.sort(reverse=True)
    sum = 0
    for i in range(N):
        if i == 0:
            sum += p[i] // 2
        else:
            sum += p[i]
    print(sum)

=======
Suggestion 4

def main():
    N = int(input())
    p = []
    for i in range(N):
        p.append(int(input()))
    p.sort(reverse=True)
    result = 0
    for i in range(N):
        if i == 0:
            result += p[i] / 2
        else:
            result += p[i]
    print(int(result))

=======
Suggestion 5

def main():
    N = int(input())
    p = [int(input()) for _ in range(N)]
    p.sort(reverse=True)
    p[0] //= 2
    print(sum(p))

=======
Suggestion 6

def main():
    N = int(input())
    p = []
    for i in range(N):
        p.append(int(input()))
    p.sort()
    for i in range(N-1):
        p[i] /= 2
    print(int(sum(p)))

=======
Suggestion 7

def main():
    n = int(input())
    p = []
    for i in range(n):
        p.append(int(input()))
    p.sort()
    p.reverse()
    ans = p[0] // 2
    for i in range(1, n):
        ans += p[i]
    print(ans)

=======
Suggestion 8

def main():
    N = int(input())
    p = [int(input()) for i in range(N)]
    p.sort()
    ans = sum(p[0:N-1]) + p[N-1] // 2
    print(ans)

=======
Suggestion 9

def  main():
    N = int(input())
    p = []
    for i in range(N):
        p.append(int(input()))
    p.sort(reverse=True)
    ans = 0
    for i in range(N):
        if i % 2 == 1:
            ans += p[i]
        else:
            ans += p[i] / 2
    print(int(ans))

=======
Suggestion 10

def main():
    n = int(input())
    prices = []
    for i in range(n):
        prices.append(int(input()))
    prices.sort()
    prices.pop()
    prices[0] = prices[0] / 2
    print(int(sum(prices)))

main()

import sys
