Synthesizing 10/10 solutions

=======
Suggestion 1

def solve(a, b):
    if a >= 13:
        return b
    elif a >= 6:
        return b//2
    else:
        return 0

a, b = map(int, input().split())
print(solve(a, b))

=======
Suggestion 2

def problem127_a():
    a,b = map(int,input().split())
    if a >= 13:
        print(b)
    elif a >= 6 and a <= 12:
        print(b//2)
    else:
        print(0)

=======
Suggestion 3

def func(a,b):
    if a >= 13:
        return b
    elif 6 <= a <= 12:
        return b//2
    else:
        return 0

a,b = map(int,input().split())
print(func(a,b))

=======
Suggestion 4

def cost(A, B):
    if A >= 13:
        return B
    elif A >= 6:
        return B // 2
    else:
        return 0

=======
Suggestion 5

def problem127_a():
    A, B = map(int, input().split())
    if A >= 13:
        print(B)
    elif A >= 6:
        print(int(B/2))
    else:
        print(0)

=======
Suggestion 6

def main():
    a,b = map(int,input().split())
    if a >= 13:
        print(b)
    elif a >= 6:
        print(int(b/2))
    else:
        print(0)

=======
Suggestion 7

def get_price(age, price):
    if age >= 13:
        return price
    elif age >= 6:
        return int(price / 2)
    else:
        return 0

=======
Suggestion 8

def ride_ferris_wheel(age, fee):
    if age >= 13:
        return fee
    elif age >= 6 and age <= 12:
        return fee / 2
    else:
        return 0

=======
Suggestion 9

def main():
    a, b = map(int, input().split())
    if a >= 13:
        print(b)
    elif a >= 6:
        print(b//2)
    else:
        print(0)

=======
Suggestion 10

def main():
    A,B = map(int,input().split())
    if A >= 13:
        print(B)
    elif A >= 6 and A <= 12:
        print(B//2)
    else:
        print(0)
