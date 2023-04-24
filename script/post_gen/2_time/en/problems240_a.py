Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    if abs(a - b) == 1:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    a, b = map(int, input().split())
    if a + 1 == b or a - 1 == b or a == 1 and b == 10 or a == 10 and b == 1:
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    if (a == 1 or a == 9 or a == 7 or a == 4) and (b == 1 or b == 9 or b == 7 or b == 4):
        print("Yes")
    elif (a == 2 or a == 5 or a == 8 or a == 0) and (b == 2 or b == 5 or b == 8 or b == 0):
        print("Yes")
    elif (a == 3 or a == 6) and (b == 3 or b == 6):
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    a, b = map(int, input().split())
    if a == 1 or b == 1 or a == 9 or b == 9:
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def main():
    a, b = map(int, input().split())
    if a == 1 or b == 1 or abs(a - b) == 1:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    a, b = map(int, input().split())
    if a == 1 or b == 1:
        print("Yes")
    elif a == 9 or b == 9:
        print("Yes")
    elif a == 7 or b == 7:
        print("Yes")
    elif a == 3 or b == 3:
        print("Yes")
    elif a == 4 or b == 4:
        print("Yes")
    elif a == 6 or b == 6:
        print("Yes")
    elif a == 8 or b == 8:
        print("Yes")
    elif a == 2 or b == 2:
        print("Yes")
    elif a == 5 or b == 5:
        print("Yes")
    elif a == 10 or b == 10:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    a,b = map(int,input().split())
    if a == 1 or b == 1 or a == 9 or b == 9:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    a, b = map(int, input().split())
    if a == 1 and b == 10:
        print("Yes")
    elif a == b - 1:
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def main():
    a,b = map(int, input().split())
    if abs(a-b) <= 1:
        print("Yes")
    else:
        print("No")

=======
Suggestion 10

def main():
    a, b = map(int, input().split())
    if (a == 1 and b == 10) or (a == 10 and b == 1):
        print("Yes")
    elif (a + 1 == b) or (a - 1 == b):
        print("Yes")
    else:
        print("No")
