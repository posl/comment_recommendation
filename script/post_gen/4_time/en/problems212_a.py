Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    if a > 0 and b == 0:
        print("Gold")
    elif a == 0 and b > 0:
        print("Silver")
    else:
        print("Alloy")

=======
Suggestion 2

def main():
    a, b = map(int, input().split())
    if a == 0:
        print('Silver')
    elif b == 0:
        print('Gold')
    else:
        print('Alloy')

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    if a > 0 and b == 0:
        print("Gold")
    elif a == 0 and b > 0:
        print("Silver")
    elif a > 0 and b > 0:
        print("Alloy")

=======
Suggestion 4

def main():
    a,b = map(int, input().split())
    if a > 0 and b > 0:
        print('Alloy')
    elif a > 0:
        print('Gold')
    else:
        print('Silver')

=======
Suggestion 5

def problem():
    a, b = map(int, input().split())
    if a > 0 and b == 0:
        print("Gold")
    elif a == 0 and b > 0:
        print("Silver")
    else:
        print("Alloy")

problem()

=======
Suggestion 6

def main():
    a,b = map(int,input().split())
    if a == 0 and b > 0:
        print("Silver")
    elif a > 0 and b == 0:
        print("Gold")
    else:
        print("Alloy")

=======
Suggestion 7

def problem():
    # Get input
    a, b = map(int, input().split())

    # Solve problem
    if a > 0 and b == 0:
        print('Gold')
    elif a == 0 and b > 0:
        print('Silver')
    else:
        print('Alloy')
