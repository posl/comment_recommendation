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
        print("error")

=======
Suggestion 2

def main():
    a, b = map(int, input().split())
    if a > 0 and b > 0:
        print("Alloy")
    elif a > 0 and b == 0:
        print("Gold")
    elif a == 0 and b > 0:
        print("Silver")

=======
Suggestion 3

def main():
    A, B = map(int, input().split())
    if A > 0 and B == 0:
        print('Gold')
    elif A == 0 and B > 0:
        print('Silver')
    else:
        print('Alloy')

=======
Suggestion 4

def main():
    a,b = map(int, input().split())
    if a > 0 and b > 0:
        print("Alloy")
    elif a > 0 and b == 0:
        print("Gold")
    elif a == 0 and b > 0:
        print("Silver")
    else:
        print("Error")

=======
Suggestion 5

def judge(a, b):
    if a > 0 and b == 0:
        return "Gold"
    elif a == 0 and b > 0:
        return "Silver"
    else:
        return "Alloy"

=======
Suggestion 6

def main():
    a,b = map(int, input().split())
    if a != 0 and b == 0:
        print("Gold")
    elif a == 0 and b != 0:
        print("Silver")
    else:
        print("Alloy")

=======
Suggestion 7

def main():
    a,b = map(int, input().split())

    if a > 0 and b == 0:
        print('Gold')
    elif a == 0 and b > 0:
        print('Silver')
    elif a > 0 and b > 0:
        print('Alloy')

=======
Suggestion 8

def judge(a,b):
    if a > 0 and b == 0:
        return 'Gold'
    elif a == 0 and b > 0:
        return 'Silver'
    elif a > 0 and b > 0:
        return 'Alloy'
    else:
        return 'Error'

=======
Suggestion 9

def main():
    A,B = map(int, input().split())
    if A == 0:
        print("Silver")
    elif B == 0:
        print("Gold")
    else:
        print("Alloy")

=======
Suggestion 10

def main():
    A,B = map(int,input().strip().split())
    if A > 0 and B == 0:
        print("Gold")
    elif A == 0 and B > 0:
        print("Silver")
    elif A > 0 and B > 0:
        print("Alloy")
    else:
        pass
