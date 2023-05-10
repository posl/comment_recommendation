Synthesizing 10/10 solutions

=======
Suggestion 1

def solve():
    X,Y,N = map(int,input().split())
    ans = 0
    if N % 3 == 0:
        ans = (N // 3) * Y
    elif N % 3 == 1:
        ans = (N // 3) * Y + X
    else:
        ans = (N // 3) * Y + Y
    print(ans)

=======
Suggestion 2

def main():
    x, y, n = map(int, input().split())
    ans = 0
    for i in range(1, n+1):
        if i % 3 == 0:
            ans += x
        else:
            ans += y
    print(ans)

=======
Suggestion 3

def main():
    X, Y, N = map(int, input().split())
    ans = 0
    ans += (N // 3) * min(3 * X, Y)
    ans += (N % 3) * X
    print(ans)

=======
Suggestion 4

def main():
    x, y, n = map(int, input().split())
    ans = 100000
    for i in range(n+1):
        for j in range(n+1):
            if i + j == n:
                ans = min(ans, x*i + y*j)
    print(ans)

=======
Suggestion 5

def main():
    x,y,n = map(int,input().split())
    ans = 10000000000000
    for i in range(0,n+1):
        ans = min(ans,((n-i)*x)+(i*3*y))
    print(ans)

=======
Suggestion 6

def get_input_lines():
    while True:
        line = input()
        if line:
            yield line
        else:
            break

=======
Suggestion 7

def main():
    x, y, n = map(int, input().split())
    ans = 0
    for i in range(1, n+1):
        if i % 3 == 0:
            ans += x
        else:
            ans += y
    print(ans)
main()

=======
Suggestion 8

def calc(x,y,n):
    if n%3 == 0:
        return n/3 * y
    else:
        return (n/3 * y) + (n%3 * x)

=======
Suggestion 9

def main():
    # input
    X, Y, N = map(int, input().split())
    # compute
    ans = 0
    for i in range(1, N+1):
        if i % 3 == 0:
            ans += X
        else:
            ans += Y
    # output
    print(ans)

=======
Suggestion 10

def solve(x, y, n):
    if n % 3 == 0:
        return n // 3 * y
    else:
        return (n // 3 + 1) * y - x
