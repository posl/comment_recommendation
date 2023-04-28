Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    x, y, n = map(int, input().split())
    if n % 3 == 0:
        print(int((n / 3) * y))
    elif n % 3 == 1:
        print(int((n / 3) * y + x))
    else:
        print(int((n / 3) * y + 2 * x))

=======
Suggestion 2

def main():
    x, y, n = map(int, input().split())
    ans = 0
    for i in range(1, n+1):
        if i % 3 == 0:
            ans += y
        else:
            ans += x
    print(ans)

=======
Suggestion 3

def main():
    x,y,n = map(int,input().split())
    if n%3 == 0:
        print((n//3)*y)
    elif n%3 == 1:
        print((n//3)*y + x)
    else:
        print((n//3)*y + 2*x)

=======
Suggestion 4

def main():
    x, y, n = map(int, input().split())
    print(min(n * x, (n // 3) * y + (n % 3) * x))

=======
Suggestion 5

def buy_apple(X, Y, N):
    if N % 3 == 0:
        return int(N / 3) * Y
    else:
        return int(N / 3) * Y + (N % 3) * X

=======
Suggestion 6

def main():
    x, y, n = map(int, input().split())
    print((n//3)*y + (n%3)*x)

=======
Suggestion 7

def main():
  X,Y,N = map(int,input().split())
  if N%3==0:
    print(N/3*Y)
  elif N%3==1:
    print((N-1)/3*Y+X)
  else:
    print((N-2)/3*Y+2*X)

=======
Suggestion 8

def main():
    # input
    x, y, n = map(int, input().split())

    # compute

    # output
    print()

=======
Suggestion 9

def main():
    X,Y,N = map(int, input().split())
    if N%X==0:
        print((N//X)*Y)
    else:
        print(((N//X)+1)*Y)

=======
Suggestion 10

def buy_apples(x,y,n):
    if n % 3 == 0:
        return min(x*n, n/3*y)
    else:
        return min(x*n, (n/3+1)*y)
