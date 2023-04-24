Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    if a <= 8 and b <= 8:
        print("Yay!")
    else:
        print(":(")

=======
Suggestion 2

def main():
    a, b = map(int, input().split())
    if a + b <= 15 and a <= 8 and b <= 8:
        print("Yay!")
    else:
        print(":(")

=======
Suggestion 3

def main():
    A, B = map(int, input().split())
    if A + B <= 16:
        print("Yay!")
    else:
        print(":(")

=======
Suggestion 4

def main():
    A, B = map(int, input().split())
    if A + B > 16:
        print(':(')
    else:
        print('Yay!')

=======
Suggestion 5

def main():
    A, B = map(int, input().split())
    if A + B <= 16:
        print('Yay!')
    else:
        print(':(')

=======
Suggestion 6

def main():
    A, B = map(int, input().split())
    print('Yay!' if A + B <= 16 and A <= 8 and B <= 8 else ':(')

=======
Suggestion 7

def main():
    # A, B = map(int, input().split())
    A, B = 11, 4
    if A + B == 16:
        print("Yay!")
    elif A <= 8 and B <= 8:
        print("Yay!")
    else:
        print(":(")

=======
Suggestion 8

def main():
    A, B = map(int, input().split())
    if (A + B) <= 16 and (A + B) > 3 and A != 1 and B != 1:
        print("Yay!")
    else:
        print(":(")

=======
Suggestion 9

def main():
    a,b = map(int,input().split())
    if a+b-1 <= 16:
        print("Yay!")
    else:
        print(":(")

=======
Suggestion 10

def main():
    a,b = map(int, input().split())
    if (a+b) > 16:
        print(":( ")
    else:
        print("Yay!")
