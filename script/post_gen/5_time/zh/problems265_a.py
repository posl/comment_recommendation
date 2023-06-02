Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    x, y, n = map(int, input().split())
    ans = 0
    if n % 3 == 0:
        ans = int(n / 3) * y
    elif n % 3 == 1:
        ans = int(n / 3) * y + x
    else:
        ans = int(n / 3) * y + 2 * x
    print(ans)

=======
Suggestion 2

def main():
    x, y, n = map(int, input().split())
    cnt = 0
    for i in range(1, n+1):
        if i % 3 == 0:
            cnt += y
        else:
            cnt += x
    print(cnt)

=======
Suggestion 3

def buy_apple(x,y,n):
    if x > y:
        return y*n
    else:
        if n%3 == 0:
            return x*n/3
        else:
            return (n/3)*x + (n%3)*y

=======
Suggestion 4

def main():
    x, y, n = map(int, input().split())
    print(((n + 2) // 3) * x if x * 3 <= y * 2 else (n // 2) * y + (n % 2) * x)

=======
Suggestion 5

def main():
    x,y,n = map(int,input().split())
    print((n//3)*y + (n%3)*x)

=======
Suggestion 6

def buy_apple(x,y,n):
    if n%3 == 0:
        return min(n/3*y,n/3*2*x)
    elif n%3 == 1:
        return min((n-1)/3*y + x,(n-1)/3*2*x + y)
    else:
        return min((n-2)/3*y + 2*x,(n-2)/3*2*x + 2*y)

=======
Suggestion 7

def main():
    x,y,n = map(int,input().split())
    result = 0
    if n%3 == 0:
        result = (y//3)*n
    elif n%3 == 1:
        result = (y//3)*(n-1)+x
    elif n%3 == 2:
        result = (y//3)*(n-2)+x*2
    print(result)

=======
Suggestion 8

def solve(x,y,n):
    if n % 3 == 0:
        return (y / 3) * n
    else:
        return ((y / 3) * (n / 3)) + (x * (n % 3))

=======
Suggestion 9

def main():
    x,y,n = map(int,input().split())
    print(x*(n//y)+x*(n%y>y//2))

=======
Suggestion 10

def main():
    x, y, n = map(int, input().split())
    if n % 3 == 0:
        print(int((n / 3) * y))
    elif n % 3 == 1:
        print(int((n / 3) * y + x))
    else:
        print(int((n / 3) * y + x * 2))
