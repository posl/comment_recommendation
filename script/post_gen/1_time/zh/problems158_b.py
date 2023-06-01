Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N, A, B = map(int, input().split())
    print(N // (A+B) * A + min(N % (A+B), A))

=======
Suggestion 2

def ball(n,a,b):
    if a+b == 0:
        return 0
    elif a+b == 1:
        if a == 1:
            return 0
        else:
            return 1
    elif n <= a:
        return 0
    elif n <= a+b:
        return 1
    else:
        return ball(n-a-b,a,b)

=======
Suggestion 3

def main():
    n,a,b = map(int,input().split())
    print((n // (a+b)) * a + min(n % (a+b),a))

=======
Suggestion 4

def main():
    n, a, b = map(int, input().split())
    if a == 0:
        print(0)
    else:
        print((n // (a + b)) * a + min(n % (a + b), a))

=======
Suggestion 5

def f(n, a, b):
    if n == 0:
        return 0
    elif n == 1:
        return a
    elif n == 2:
        return a + b
    else:
        return f(n - 1, a, b) + f(n - 2, a, b)

=======
Suggestion 6

def problem158_b():
    n, a, b = map(int, input().split())
    print(min(n, a + b))
    return

problem158_b()

=======
Suggestion 7

def cal_balls(n, a, b):
    if n == 0:
        return 0
    if n == 1:
        return a
    if n == 2:
        return a + b
    return cal_balls(n - 1, a, b) + cal_balls(n - 2, a, b)

=======
Suggestion 8

def main():
    n, a, b = map(int, input().split())
    print(n // (a + b) * a + min(n % (a + b), a))

=======
Suggestion 9

def main():
    n,a,b = map(int,input().split())
    if a == 0:
        print(0)
    elif n <= a+b:
        print(a)
    else:
        print(a*(n//(a+b)) + min(a,n%(a+b)))

=======
Suggestion 10

def countBalls(N, A, B):
    if A == 0 and B == 0:
        return 0
    if A == 0:
        return 0
    if B == 0:
        return N
    if A + B == 1:
        return 1
    if A + B == 2:
        return 1
    if A + B == 3:
        return 2
    if A + B == 4:
        return 2
    if A + B == 5:
        return 3
    if A + B == 6:
        return 3
    if A + B == 7:
        return 4
    if A + B == 8:
        return 4
    if A + B == 9:
        return 5
    if A + B == 10:
        return 5
    if A + B == 11:
        return 6
    if A + B == 12:
        return 6
    if A + B == 13:
        return 7
    if A + B == 14:
        return 7
    if A + B == 15:
        return 8
    if A + B == 16:
        return 8
    if A + B == 17:
        return 9
    if A + B == 18:
        return 9
    if A + B == 19:
        return 10
    if A + B == 20:
        return 10
    if A + B == 21:
        return 11
    if A + B == 22:
        return 11
    if A + B == 23:
        return 12
    if A + B == 24:
        return 12
    if A + B == 25:
        return 13
    if A + B == 26:
        return 13
    if A + B == 27:
        return 14
    if A + B == 28:
        return 14
    if A + B == 29:
        return 15
    if A + B == 30:
        return 15
    if A + B == 31:
        return 16
    if A + B == 32:
        return 16
    if A
