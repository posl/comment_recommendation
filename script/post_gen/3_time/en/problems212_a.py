Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A, B = map(int, input().split())
    if A > 0 and B == 0:
        print('Gold')
    elif A == 0 and B > 0:
        print('Silver')
    else:
        print('Alloy')

=======
Suggestion 2

def main():
    a, b = map(int, input().split())
    if a > 0 and b > 0:
        print('Alloy')
    elif a > 0 and b == 0:
        print('Gold')
    elif a == 0 and b > 0:
        print('Silver')
    else:
        print('Alloy')

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    if a == 0 and b != 0:
        print("Silver")
    elif a != 0 and b == 0:
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
    A, B = map(int, input().split())
    if (A > 0 and B == 0):
        print("Gold")
    elif (A == 0 and B > 0):
        print("Silver")
    else:
        print("Alloy")

=======
Suggestion 6

def main():
    # Read the input
    A, B = map(int, input().split())
    # Check the conditions
    if A > 0 and B == 0:
        print("Gold")
    elif A == 0 and B > 0:
        print("Silver")
    else:
        print("Alloy")

main()
