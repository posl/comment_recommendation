Synthesizing 10/10 solutions

=======
Suggestion 1

def check(n):
    if n >= -2**31 and n <= 2**31-1:
        return True
    else:
        return False

n = int(input())

=======
Suggestion 2

def main():
    N = int(input())
    if N >= -2**31 and N <= 2**31-1:
        print('是')
    else:
        print('否')
main()

=======
Suggestion 3

def is_between(a, b, c):
    if a <= b and b <= c:
        print("是")
    else:
        print("否")

a = int(input())
is_between(-2147483648, a, 2147483647)

=======
Suggestion 4

def is_between(n):
    if -2**31 <= n and n <= 2**31-1:
        print('是')
    else:
        print('否')

n = int(input())
is_between(n)

=======
Suggestion 5

def main():
    n=int(input())
    if n>=-2**31 and n<=2**31-1:
        print('是')
    else:
        print('否')

=======
Suggestion 6

def main():
    N = int(input())
    if N >= -2 ** 31 and N <= 2 ** 31 - 1:
        print("是")
    else:
        print("否")

=======
Suggestion 7

def is_between(n):
    if n > -2**31 and n < 2**31 - 1:
        print("是")
    else:
        print("否")

=======
Suggestion 8

def main():
    n = int(input())
    if -2**31 <= n <= 2**31-1:
        print("是")
    else:
        print("否")

=======
Suggestion 9

def main():
    n = int(input())
    if n >= -2**31 and n <= 2**31-1:
        print("是")
    else:
        print("否")

=======
Suggestion 10

def f(n):
    if -2**31<=n<=2**31-1:
        print("是")
    else:
        print("否")

n = int(input())
f(n)
