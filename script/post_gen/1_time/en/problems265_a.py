Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    x, y, n = map(int, input().split())
    if n % 3 == 0:
        print(int((n / 3) * y))
    elif n % 3 == 1:
        print(int((n // 3) * y + x))
    else:
        print(int((n // 3) * y + 2 * x))

=======
Suggestion 2

def solve(x, y, n):
    if n % 3 == 0:
        return n / 3 * y
    elif n % 3 == 1:
        return (n - 1) / 3 * y + x
    else:
        return (n - 2) / 3 * y + 2 * x

=======
Suggestion 3

def main():
    x, y, n = map(int, input().split())
    if n % 3 == 0:
        print(x * (n // 3))
    elif n % 3 == 1:
        print(min(x + y, y * (n // 3) + x))
    else:
        print(min(x * (n // 3 + 1), y * (n // 3 + 1) - x))

main()

=======
Suggestion 4

def buy_apple(x, y, n):
    if n % 3 == 0:
        return (n // 3) * y
    elif n % 3 == 1:
        return (n // 3) * y + x
    else:
        return (n // 3) * y + (n % 3) * x

=======
Suggestion 5

def main():
    X, Y, N = map(int, input().split())
    if N%3 == 0:
        print(Y*(N/3))
    elif N%3 == 1:
        print(Y*(N//3)+X)
    elif N%3 == 2:
        print(Y*(N//3)+2*X)
    else:
        print('error')

=======
Suggestion 6

def main():
    x, y, n = map(int, input().split())
    print((n//3)*y + (n%3)*x)

=======
Suggestion 7

def main():
    x,y,n = map(int, input().split())
    #print(x,y,n)
    if n % 3 == 0:
        print((n/3)*y)
    elif n % 3 == 1:
        print((n//3)*y+x)
    elif n % 3 == 2:
        print((n//3)*y+x*2)

=======
Suggestion 8

def main():
    x, y, n = map(int, input().split())
    print(min(x*(n//3*3), x*(n//3*3+3)-y*(n-(n//3*3))))

=======
Suggestion 9

def main():
    x, y, n = map(int, input().split())

    # 1. Buy one apple for X yen (the currency in Japan).
    # 2. Buy three apples for Y yen.

    # How much yen do you need to pay to obtain exactly N apples?  

    # 1. Buy one apple for X yen (the currency in Japan).
    # 2. Buy three apples for Y yen.

    # How much yen do you need to pay to obtain exactly N apples?  
    # x, y, n = 10, 25, 10
    # x, y, n = 10, 40, 10
    # x, y, n = 100, 100, 2
    # x, y, n = 100, 100, 100

    # 1. Buy one apple for X yen (the currency in Japan).
    # 2. Buy three apples for Y yen.

    # How much yen do you need to pay to obtain exactly N apples?  
    # x, y, n = 10, 25, 10
    # x, y, n = 10, 40, 10
    # x, y, n = 100, 100, 2
    # x, y, n = 100, 100, 100

    # 1. Buy one apple for X yen (the currency in Japan).
    # 2. Buy three apples for Y yen.

    # How much yen do you need to pay to obtain exactly N apples?  
    # x, y, n = 10, 25, 10
    # x, y, n = 10, 40, 10
    # x, y, n = 100, 100, 2
    # x, y, n = 100, 100, 100

    # 1. Buy one apple for X yen (the currency in Japan).
    # 2. Buy three apples for Y yen.

    # How much yen do you need to pay to obtain exactly N apples?  
    # x, y, n = 10, 25, 10
    # x, y, n = 10, 40, 10
    # x, y, n = 100, 100, 2

=======
Suggestion 10

def get_input():
    return map(int, input().split())
