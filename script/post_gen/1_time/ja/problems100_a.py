Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    A, B = map(int, input().split())
    if A + B == 16:
        if A <= 8 and B <= 8:
            print("Yay!")
        else:
            print(":(")
    else:
        print(":(")

=======
Suggestion 2

def main():
    A, B = map(int, input().split())
    if A + B <= 16 and max(A, B) <= 8:
        print("Yay!")
    else:
        print(":(")

=======
Suggestion 3

def main():
    A, B = map(int, input().split())
    if A + B == 16:
        print("Yay!")
    elif A >= 9 or B >= 9:
        print("Yay!")
    else:
        print(":(")

=======
Suggestion 4

def main():
    a, b = map(int, input().split())
    if a+b > 16:
        print(':(')
    elif a > 8 or b > 8:
        print(':(')
    else:
        print('Yay!')

=======
Suggestion 5

def main():
    a, b = map(int, input().split())
    if a + b == 16:
        print("Yay!")
    else:
        print(":(")

=======
Suggestion 6

def main():
    a, b = map(int, input().split())
    if (a > 8) or (b > 8):
        print(":(")
    else:
        print("Yay!")

=======
Suggestion 7

def main():
    A, B = map(int, input().split())
    if A + B <= 16:
        print('Yay!')
    else:
        print(':(')

=======
Suggestion 8

def main():
    A,B = map(int,input().split())
    if A+B == 16:
        print("Yay!")
    else:
        print(":(")

=======
Suggestion 9

def main():
    # A, B = map(int, input().split())
    A, B = 11, 4
    if A+B <= 16:
        print('Yay!')
    else:
        print(':(')

=======
Suggestion 10

def main():
    # A, B = map(int, input().split())
    A, B = 11, 4

    if A + B > 16:
        print(':(')
    elif A % 2 == 0 or B % 2 == 0:
        print(':(')
    else:
        print('Yay!')
