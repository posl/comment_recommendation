Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    X, Y, N = map(int, input().split())
    if N % 3 == 0:
        print((N // 3) * Y)
    elif N % 3 == 1:
        print(((N // 3) * Y) + X)
    else:
        print(((N // 3) * Y) + (2 * X))

=======
Suggestion 2

def main():
    X, Y, N = map(int, input().split())
    if N % 3 == 0:
        print((N//3) * Y)
    elif N % 3 == 1:
        print((N//3) * Y + X)
    else:
        print((N//3) * Y + X*2)

=======
Suggestion 3

def main():
    X, Y, N = map(int, input().split())
    if N % 3 == 0:
        print((N // 3)*Y)
    elif N % 3 == 1:
        print((N//3)*Y + X)
    else:
        print((N//3)*Y + 2*X)

=======
Suggestion 4

def solve():
    x, y, n = map(int, input().split())
    cost = 0
    for i in range(1, n + 1):
        if i % 3 == 0:
            cost += y
        else:
            cost += x
    print(cost)

solve()

=======
Suggestion 5

def solve():
    X, Y, N = map(int, input().split())
    if N % 3 == 0:
        print(int(N / 3) * Y)
    elif N % 3 == 1:
        print(int(N / 3) * Y + X)
    elif N % 3 == 2:
        print(int(N / 3) * Y + 2 * X)

=======
Suggestion 6

def main():
    x, y, n = map(int, input().split())
    print(min((n//3)*y + (n%3)*x, (n//3+1)*y))

=======
Suggestion 7

def min_price(x, y, n):
    if n % 3 == 0:
        return n // 3 * y
    elif n % 3 == 1:
        return (n // 3) * y + x
    else:
        return (n // 3 + 1) * y

=======
Suggestion 8

def solve():
    x, y, n = map(int, input().split())
    ans = 0
    for i in range(n+1):
        ans = max(ans, (n-i)*x + i*y)
    print(ans)

=======
Suggestion 9

def main():
    x, y, n = map(int, input().split())
    min_cost = 1000
    for i in range(1, n+1):
        for j in range(0, n+1):
            if i + 3*j == n:
                cost = x*i + y*j
                if cost < min_cost:
                    min_cost = cost
    print(min_cost)

=======
Suggestion 10

def main():
    # Read from Standard Input
    x, y, n = map(int, input().split())
    # Solve the problem
    ans = 0
    if n % 3 == 0:
        ans = (n // 3) * y
    elif n % 3 == 1:
        ans = ((n - 1) // 3) * y + x
    elif n % 3 == 2:
        ans = ((n - 2) // 3) * y + 2 * x
    # Print the answer to Standard Output
    print(ans)
