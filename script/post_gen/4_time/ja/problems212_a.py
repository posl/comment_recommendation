Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    if a > 0 and b == 0:
        print("Gold")
    elif a == 0 and b > 0:
        print("Silver")
    elif a > 0 and b > 0:
        print("Alloy")
    else:
        print("Error")

=======
Suggestion 2

def main():
    A, B = map(int, input().split())
    if A > 0 and B == 0:
        print('Gold')
    elif A == 0 and B > 0:
        print('Silver')
    elif A > 0 and B > 0:
        print('Alloy')
    else:
        print('Error')

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    if a == 0:
        print("Silver")
    elif b == 0:
        print("Gold")
    else:
        print("Alloy")

=======
Suggestion 4

def main():
    A,B = map(int,input().split())
    if A > 0 and B == 0:
        print("Gold")
    elif A == 0 and B > 0:
        print("Silver")
    else:
        print("Alloy")

=======
Suggestion 5

def main():
    a, b = map(int, input().split())
    if a > 0 and b > 0:
        print('Alloy')
    elif a > 0:
        print('Gold')
    else:
        print('Silver')

=======
Suggestion 6

def main():
    A,B = map(int,input().split())
    if A > 0 and B == 0:
        print('Gold')
    elif A == 0 and B > 0:
        print('Silver')
    elif A > 0 and B > 0:
        print('Alloy')

=======
Suggestion 7

def main():
    a,b = map(int,input().split())
    if a>0 and b==0:
        print("Gold")
    elif a==0 and b>0:
        print("Silver")
    else:
        print("Alloy")

=======
Suggestion 8

def problems212_a():
    a, b = map(int, input().split())
    if 0 < a and b == 0:
        print("Gold")
    elif a == 0 and 0 < b:
        print("Silver")
    else:
        print("Alloy")

=======
Suggestion 9

def main():
    a,b = map(int,input().split())
    if a > 0 and b > 0:
        print("Alloy")
    elif a > 0 and b == 0:
        print("Gold")
    else:
        print("Silver")

=======
Suggestion 10

def check(a, b):
    if a > 0 and b == 0:
        return "Gold"
    elif a == 0 and b > 0:
        return "Silver"
    elif a > 0 and b > 0:
        return "Alloy"
