Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    x,y,n = map(int,input().split())
    if n%3 == 0:
        print(int(n/3*y))
    elif n%3 == 1:
        print(int((n-1)/3*y+x))
    else:
        print(int((n-2)/3*y+2*x))

=======
Suggestion 2

def problem265_a():
    x, y, n = map(int, input().split())
    if n % 3 == 0:
        print(int(y * n / 3))
    elif n % 3 == 1:
        print(int(y * (n - 1) / 3 + x))
    else:
        print(int(y * (n - 2) / 3 + 2 * x))

problem265_a()

=======
Suggestion 3

def solve():
    X, Y, N = map(int, input().split())
    ans = 0
    for i in range(1, N + 1):
        if i % 3 == 0:
            ans += Y
        else:
            ans += X
    print(ans)

solve()

=======
Suggestion 4

def main():
    X,Y,N = map(int, input().split())
    print(X*(N//Y) + (N%Y)*X//Y)
    #print(X*(N//Y) + (N%Y)*X//Y)
    #print(X*(N//Y) + (N%Y)*X//Y)
    #print(X*(N//Y) + (N%Y)*X//Y)
    #print(X*(N//Y) + (N%Y)*X//Y)
    #print(X*(N//Y) + (N%Y)*X//Y)
    #print(X*(N//Y) + (N%Y)*X//Y)
    #print(X*(N//Y) + (N%Y)*X//Y)
    #print(X*(N//Y) + (N%Y)*X//Y)
    #print(X*(N//Y) + (N%Y)*X//Y)

=======
Suggestion 5

def main():
    x, y, n = map(int, input().split())
    if n % 3 == 0:
        print(n // 3 * y)
    else:
        if n % 3 == 1:
            print((n // 3 * y) + x)
        else:
            print((n // 3 * y) + y)

=======
Suggestion 6

def buy_apple(x, y, n):
    if n % 3 == 0:
        return y * (n // 3)
    else:
        return y * (n // 3) + x * (n % 3)

=======
Suggestion 7

def main():
    x, y, n = map(int, input().split())
    if n % 3 == 0:
        print(x * n // 3)
    elif n % 3 == 1:
        print(min(x * (n - 1) // 3 + y, y * (n + 2) // 3))
    else:
        print(min(x * (n + 2) // 3, y * (n - 1) // 3 + x))

=======
Suggestion 8

def get_minimum_cost(x, y, n):
    if x == y:
        return x * n
    if n % 3 == 0:
        return n / 3 * y
    elif n % 3 == 1:
        return (n / 3 + 1) * y
    else:
        return (n / 3 + 1) * y

=======
Suggestion 9

def problem265_a(x, y, n):
    if x == y:
        return x * n
    elif x > y:
        return y * n
    else:
        return x * n + (n // 3) * (y - x)

=======
Suggestion 10

def main():
    x, y, n = map(int, input().split())
    if n % 3 == 0:
        print((n // 3) * y)
    elif n % 3 == 1:
        print((n // 3) * y + x)
    else:
        print((n // 3) * y + 2 * x)
