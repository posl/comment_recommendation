Synthesizing 10/10 solutions

=======
Suggestion 1

def get_max_remainder_sum(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return (n * (n - 1)) // 2

=======
Suggestion 2

def problem139_d():
    n = int(input())
    if n == 1:
        print(0)
        return
    if n == 2:
        print(1)
        return
    if n % 2 == 0:
        print((n - 1) * (n // 2))
    else:
        print((n - 2) * (n // 2) + n - 1)

=======
Suggestion 3

def main():
    n = int(input())
    if n == 1:
        print(0)
        return
    if n == 2:
        print(1)
        return
    if n % 2 == 0:
        print(n * (n - 1) // 2)
    else:
        print((n - 1) * (n - 2) // 2 + n - 1)

=======
Suggestion 4

def max_sum(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    elif n%2 == 0:
        return n*(n-1)//2
    else:
        return n*(n-1)//2 + (n-1)//2

=======
Suggestion 5

def solve(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    if n == 3:
        return 3
    if n % 2 == 0:
        return n * (n - 1) // 2
    else:
        return n * (n - 1) // 2 - 1

print(solve(int(input())))

=======
Suggestion 6

def problems139_d():
    pass

=======
Suggestion 7

def main():
    n = int(input())
    if n == 1:
        print(0)
    elif n == 2:
        print(1)
    elif n == 3:
        print(4)
    else:
        print(n * (n - 1) * (n - 2) * (n - 3))

=======
Suggestion 8

def gcd(a,b):
    if a < b:
        a,b = b,a
    while b != 0:
        a,b = b,a%b
    return a

=======
Suggestion 9

def main():
    n = int(input())
    if n == 1:
        print(0)
    else:
        print(int(n*(n-1)/2))

=======
Suggestion 10

def main():
    n = int(input())
    print(int(n*(n-1)/2))
