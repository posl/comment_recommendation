Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    if a == 1 and b == 10:
        print("Yes")
    elif a == 10 and b == 1:
        print("Yes")
    elif b - a == 1:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    a, b = map(int, input().split())
    if a == 1 and b == 10:
        print("Yes")
    elif a == 10 and b == 1:
        print("Yes")
    elif abs(a - b) == 1:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    if abs(a-b) == 1:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    a, b = map(int, input().split())
    if a == 1 and b == 10:
        print("Yes")
    elif a <= 4 and b <= 4:
        print("Yes")
    elif a >= 5 and b >= 5:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    a, b = map(int, input().split())
    if a == 1 and b == 10:
        print('Yes')
    elif a <= 4 and b <= 4:
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def main():
    a, b = map(int, input().split())
    if a == 1 or a == 3 or a == 6 or a == 8 or a == 10:
        if b == a + 1:
            print('Yes')
        else:
            print('No')
    elif a == 2 or a == 4 or a == 5 or a == 7 or a == 9:
        if b == a + 1 or b == a + 3:
            print('Yes')
        else:
            print('No')

=======
Suggestion 7

def main():
    a, b = map(int, input().split())
    if a == 1 and b == 10:
        print("Yes")
    elif a == 1 or b == 1 or a == 10 or b == 10:
        print("No")
    else:
        print("Yes")

=======
Suggestion 8

def main():
    a,b = map(int,input().split())
    if a == 1 and b == 10:
        print("Yes")
    elif a <= 4 and b <= 4:
        print("Yes")
    elif a >= 6 and b >= 6:
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def main():
    a, b = map(int, input().split())
    if a == 1 and b == 10:
        print("Yes")
    elif a == 1 or b == 1:
        print("No")
    else:
        print("Yes")

=======
Suggestion 10

def main():
    a, b = map(int, input().split())
    if a <= b <= a + 2:
        print("Yes")
    else:
        print("No")
