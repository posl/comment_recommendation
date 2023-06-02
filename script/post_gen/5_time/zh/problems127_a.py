Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    A,B = map(int,input().split())
    if A>=13:
        print(B)
    elif A>=6 and A<=12:
        print(int(B/2))
    else:
        print(0)

=======
Suggestion 2

def calcFee(age,fee):
    if age >= 13:
        return fee
    elif age >= 6:
        return fee/2
    else:
        return 0

=======
Suggestion 3

def cal_fee(age, fee):
    if age > 12:
        return fee
    elif age > 5 and age <= 12:
        return fee // 2
    else:
        return 0

=======
Suggestion 4

def calcFee(age, fee):
    if age >= 13:
        return fee
    elif age >= 6 and age <= 12:
        return fee / 2
    else:
        return 0

=======
Suggestion 5

def problem127_a():
    a, b = map(int, input().split())
    if a <= 5:
        print(0)
    elif a <= 12:
        print(b//2)
    else:
        print(b)

=======
Suggestion 6

def main():
    a, b = map(int, input().split())
    if a >= 13:
        print(b)
    elif a >= 6:
        print(b // 2)
    else:
        print(0)

=======
Suggestion 7

def get_price(age, price):
    if age >= 13:
        return price
    elif age >= 6 and age <= 12:
        return price / 2
    else:
        return 0

=======
Suggestion 8

def problem127_a(A,B):
    if A >= 13:
        print(B)
    elif A >= 6:
        print(B/2)
    else:
        print(0)

=======
Suggestion 9

def main():
    A,B = map(int,input().split())
    if A >= 13:
        print(B)
    elif 6 <= A <= 12:
        print(int(B/2))
    else:
        print(0)

=======
Suggestion 10

def problem127_a():
    a,b = map(int,input().split())
    if a >= 13:
        print(b)
    elif 6 <= a <= 12:
        print(b//2)
    else:
        print(0)
