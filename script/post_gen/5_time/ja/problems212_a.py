Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a,b = map(int, input().split())
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
    if 0 < a and b == 0:
        print("Gold")
    elif a == 0 and 0 < b:
        print("Silver")
    elif 0 < a and 0 < b:
        print("Alloy")

main()

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
    else:
        print("Error")

=======
Suggestion 4

def main():
    a,b = map(int,input().split())
    if a == 0:
        print('Silver')
    elif b == 0:
        print('Gold')
    else:
        print('Alloy')

=======
Suggestion 5

def main():
    a,b = map(int, input().split())
    if a > 0 and b == 0:
        print("Gold")
    elif a == 0 and b > 0:
        print("Silver")
    elif a > 0 and b > 0:
        print("Alloy")

=======
Suggestion 6

def main():
    a, b = map(int, input().split())
    if a > 0 and b > 0:
        print('Alloy')
    elif a > 0 and b == 0:
        print('Gold')
    else:
        print('Silver')

=======
Suggestion 7

def main():
    a, b = map(int, input().split())
    if a > 0 and b > 0:
        print("Alloy")
    elif a > 0 and b == 0:
        print("Gold")
    elif a == 0 and b > 0:
        print("Silver")
