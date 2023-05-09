Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    x, y, n = map(int, input().split())
    if n % 3 == 0:
        print(n // 3 * y)
    elif n % 3 == 1:
        print((n // 3 - 1) * y + x)
    else:
        print((n // 3) * y + x * 2)

=======
Suggestion 2

def main():
    x, y, n = map(int, input().split())

    if n % 3 == 0:
        print((n // 3) * y)
    elif n % 3 == 1:
        print(((n // 3) * y) + x)
    elif n % 3 == 2:
        print(((n // 3) * y) + (2 * x))

=======
Suggestion 3

def main():
    x, y, n = map(int, input().split())
    if n % 3 == 0:
        print((y // 3) * n)
    elif n % 3 == 1:
        print((y // 3) * n + x)
    else:
        print((y // 3) * n + (y // 3) + x)

=======
Suggestion 4

def main():
    x, y, n = map(int, input().split())
    cost = 0
    for i in range(1, n+1):
        if i % 3 == 0:
            cost += y
        else:
            cost += x
    print(cost)

=======
Suggestion 5

def main():
    x, y, n = map(int, input().split())
    if n % 3 == 0:
        print(int((n // 3) * y))
    elif n % 3 == 1:
        print(int((n // 3) * y + x))
    else:
        print(int((n // 3) * y + 2 * x))

=======
Suggestion 6

def main():
    X, Y, N = map(int, input().split())
    if N % 3 == 0:
        print(int(N/3) * Y)
    elif N % 3 == 1:
        print(int(N/3) * Y + X)
    elif N % 3 == 2:
        print(int(N/3) * Y + 2*X)

=======
Suggestion 7

def main():
    X, Y, N = map(int, input().split())
    cnt = 0
    for i in range(1, N+1):
        if i % 3 == 0:
            cnt += Y
        else:
            cnt += X
    print(cnt)
main()

=======
Suggestion 8

def solve():
    x,y,n = map(int, input().split())
    ans = 0
    if n%3 == 0:
        ans = n//3*y
    elif n%3 == 1:
        ans = n//3*y + x
    else:
        ans = n//3*y + 2*x
    print(ans)

=======
Suggestion 9

def main():
    x, y, n = map(int, input().split())
    cost = 10000000000
    for i in range(n+1):
        for j in range(n+1):
            if i + j == n:
                cost = min(cost, i*x + j*y)
    print(cost)
