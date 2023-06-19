Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    x, y, n = map(int, input().split())
    print((n//3)*y + (n%3)*x)

=======
Suggestion 2

def buy_apple(x,y,n):
    if n%3 == 0:
        return (n/3)*y
    elif n%3 == 1:
        return (n/3)*y+x
    else:
        return (n/3)*y+2*x

=======
Suggestion 3

def solve():
    X,Y,N = map(int,input().split())
    if N % 3 == 0:
        print(int(N/3)*Y)
    elif N % 3 == 1:
        print(int(N/3)*Y+X)
    else:
        print(int(N/3)*Y+2*X)

=======
Suggestion 4

def solve():
    x,y,n = map(int,input().split())
    result = 0
    for i in range(1,n+1):
        if i%3 == 0:
            result += x
        else:
            result += y
    print(result)

=======
Suggestion 5

def main():
    x,y,n = map(int,input().split())
    if n%3 == 0:
        print(int(n/3)*y)
    elif n%3 == 1:
        print(int(n/3)*y+x)
    else:
        print(int(n/3)*y+2*x)

=======
Suggestion 6

def main():
    x,y,n = map(int,input().split())
    if n%3==0:
        print((n//3)*y)
    elif n%3==1:
        print((n//3)*y+x)
    else:
        print((n//3)*y+x*2)

=======
Suggestion 7

def get_input():
    x, y, n = map(int, input().split())
    return x, y, n

=======
Suggestion 8

def solve():
    x,y,n = map(int,input().split())
    ans = 0
    for i in range(1,n+1):
        if i % 3 == 0:
            ans += x
        else:
            ans += y
    print(ans)

=======
Suggestion 9

def solve(x, y, n):
    ans = 0
    while n > 0:
        if n >= 3:
            if x * 3 > y:
                ans += y
                n -= 3
            else:
                ans += x
                n -= 1
        else:
            ans += x
            n -= 1
    return ans

x, y, n = map(int, input().split())
print(solve(x, y, n))

=======
Suggestion 10

def main():
    x,y,n = map(int,input().split())
    if n%3 == 0:
        print((n//3)*y)
    elif n%3 == 1:
        print((n//3)*y+x)
    else:
        print((n//3)*y+y)
