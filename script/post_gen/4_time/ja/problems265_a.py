Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    x, y, n = map(int, input().split())
    if n % 3 == 0:
        print(n // 3 * y)
    elif n % 3 == 1:
        print(n // 3 * y + x)
    else:
        print(n // 3 * y + x * 2)

=======
Suggestion 2

def main():
    x, y, n = map(int, input().split())
    ans = 0
    if n % 3 == 0:
        ans = (n // 3) * y
    elif n % 3 == 1:
        ans = (n // 3) * y + x
    else:
        ans = (n // 3) * y + x * 2
    print(ans)

=======
Suggestion 3

def main():
    x, y, n = map(int, input().split())
    ans = 10 ** 10
    for i in range(n + 1):
        for j in range(n + 1):
            if i + j == n:
                ans = min(ans, i * x + j * y)
    print(ans)

=======
Suggestion 4

def main():
    X, Y, N = map(int, input().split())
    ans = 0
    if N % 3 == 0:
        ans = N // 3 * Y
    else:
        ans = N // 3 * Y + (N % 3) * X
    print(ans)

=======
Suggestion 5

def main():
    x,y,n = map(int,input().split())
    ans = 1000
    for i in range(n+1):
        for j in range(n+1):
            if i + j == n:
                ans = min(ans,(x*i)+(y*j))
    print(ans)

=======
Suggestion 6

def get_input():
    x, y, n = map(int, input().split())
    return x, y, n

=======
Suggestion 7

def solve(X,Y,N):
    if N%3 == 0:
        return min(X*N//3,Y*N)
    elif N%3 == 1:
        return min(X*(N-1)//3+Y,X+N//3*Y)
    else:
        return min(X*(N-2)//3+2*Y,X+(N-2)//3*Y)

=======
Suggestion 8

def main():
    x,y,n = map(int,input().split())
    min = 1000000000
    for i in range(n+1):
        for j in range(n+1):
            if i+j == n:
                if x*i+y*j < min:
                    min = x*i+y*j
    print(min)

=======
Suggestion 9

def solve():
    x, y, n = map(int, input().split())
    ans = 10000000000
    for i in range(100):
        for j in range(100):
            if x*i + 3*j*y == n:
                ans = min(ans, i*x+j*y)
    print(ans)

=======
Suggestion 10

def main():
    x, y, n = map(int, input().split())
    print(int((n + 2) * x - (n - 2) * y))
