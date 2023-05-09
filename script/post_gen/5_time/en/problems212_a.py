Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    if a > 0 and b == 0:
        print('Gold')
    elif a == 0 and b > 0:
        print('Silver')
    else:
        print('Alloy')

=======
Suggestion 2

def main():
    a, b = map(int, input().split())
    if a > 0 and b > 0:
        print("Alloy")
    elif a > 0 and b == 0:
        print("Gold")
    else:
        print("Silver")

=======
Suggestion 3

def main():
    A, B = map(int, input().split())
    if 0 < A and 0 < B:
        print("Alloy")
    elif 0 < A and B == 0:
        print("Gold")
    elif A == 0 and 0 < B:
        print("Silver")
    else:
        print("Error")

=======
Suggestion 4

def main():
    a,b = map(int, input().split())
    if a == 0:
        print("Silver")
    elif b == 0:
        print("Gold")
    else:
        print("Alloy")

=======
Suggestion 5

def main():
    A,B = map(int, input().split())
    if A == 0:
        print("Silver")
    elif B == 0:
        print("Gold")
    else:
        print("Alloy")

=======
Suggestion 6

def main():
    A, B = map(int, input().split())
    if (0 < A and 0 == B):
        print("Gold")
    elif (0 == A and 0 < B):
        print("Silver")
    else:
        print("Alloy")

=======
Suggestion 7

def main():
    data = input()
    data = data.split()
    if (int(data[0]) > 0 and int(data[1]) == 0):
        print("Gold")
    elif (int(data[0]) == 0 and int(data[1]) > 0):
        print("Silver")
    else:
        print("Alloy")

=======
Suggestion 8

def main():
    # Take input from stdin
    a, b = map(int, input().split())

    # Check for the conditions
    if 0 < a and b == 0:
        print("Gold")
    elif a == 0 and 0 < b:
        print("Silver")
    else:
        print("Alloy")
