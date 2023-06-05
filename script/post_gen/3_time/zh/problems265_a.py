Synthesizing 10/10 solutions

=======
Suggestion 1

def f(x,y,n):
    min = 100000000
    for i in range(0,n+1):
        for j in range(0,n+1):
            if i*3+j*1==n:
                if min>(x*i+y*j):
                    min = x*i+y*j
    return min

=======
Suggestion 2

def buy_apple(x,y,n):
    if x*3 <= y:
        return x*n
    else:
        if n%3 == 0:
            return y*(n/3)
        else:
            return y*(n/3)+x*(n%3)

=======
Suggestion 3

def buy_apple(x, y, n):
    # 用x买
    if n % 3 == 0:
        return x * n // 3
    else:
        # 用y买
        if n % 3 == 1:
            return min(x*(n-1)//3 + y, x*(n-2)//3 + 2*y)
        else:
            return min(x*(n-2)//3 + 2*y, x*(n-1)//3 + y)

=======
Suggestion 4

def main():
    X,Y,N = map(int,input().split())
    if X == Y:
        print(X*N)
    elif X > Y:
        print(Y*N)
    else:
        if N%3 == 0:
            print(int((N/3)*Y))
        elif N%3 == 1:
            print(int((N/3)*Y+X))
        else:
            print(int((N/3)*Y+Y))

=======
Suggestion 5

def main():
    x, y, n = map(int, input().split())
    if n % 3 == 0:
        print(n // 3 * y)
    elif n % 3 == 1:
        print(n // 3 * y + x)
    elif n % 3 == 2:
        print(n // 3 * y + 2 * x)

=======
Suggestion 6

def main():
    x,y,n = map(int,input().split())
    if n%3==0:
        print((n//3)*y)
    elif n%3==1:
        print((n//3)*y+x)
    else:
        print((n//3)*y+2*x)

=======
Suggestion 7

def main():
    x, y, n = map(int, input().split())
    ans = n // 3 * y
    if n % 3 == 1:
        ans += x
    elif n % 3 == 2:
        ans += y
    print(ans)

=======
Suggestion 8

def main():
    x,y,n=map(int,input().split())
    if n%3==0:
        print(int(n/3)*y)
    elif n%3==1:
        print(int(n/3)*y+x)
    elif n%3==2:
        print(int(n/3)*y+x*2)
main()

=======
Suggestion 9

def main():
    x,y,n = map(int,input().split())
    if n % 3 == 0:
        print(y * (n // 3))
    elif n % 3 == 1:
        print(y * (n // 3) + x)
    else:
        print(y * (n // 3) + x * 2)

=======
Suggestion 10

def main():
    x, y, n = map(int, input().split())
    print(int((n+y-1)/y*x))
