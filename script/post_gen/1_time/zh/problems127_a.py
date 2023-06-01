Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a,b = map(int,input().split())
    if a >= 13:
        print(b)
    elif a >= 6 and a <= 12:
        print(int(b/2))
    else:
        print(0)

=======
Suggestion 2

def main():
    A, B = map(int, input().split())
    if A >= 13:
        print(B)
    elif A >= 6:
        print(B // 2)
    else:
        print(0)

=======
Suggestion 3

def problems127_a():
    a,b = map(int,input().split())
    if a >= 13:
        print(b)
    elif a >= 6 and a <= 12:
        print(int(b/2))
    else:
        print(0)

=======
Suggestion 4

def solve():
    a,b = map(int,input().split())
    if a >= 13:
        print(b)
    elif a >= 6:
        print(b//2)
    else:
        print(0)
solve()

=======
Suggestion 5

def get_fee(age):
    if age >= 13:
        return 100
    elif age >= 6:
        return 50
    else:
        return 0

=======
Suggestion 6

def problem127_a():
    age, price = map(int, input().split())
    if age >= 13:
        print(price)
    elif age >= 6 and age <= 12:
        print(price // 2)
    else:
        print(0)

=======
Suggestion 7

def calcPrice(age, price):
    if age >= 13:
        return price
    elif age >= 6 and age <= 12:
        return price / 2
    else:
        return 0

=======
Suggestion 8

def main():
    A, B = map(int, input().split())
    if A >= 13:
        print(B)
    elif 6 <= A <= 12:
        print(B // 2)
    else:
        print(0)
