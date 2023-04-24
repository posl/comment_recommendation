Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    if (a * b) % 2 == 0:
        print('No')
    else:
        print('Yes')

=======
Suggestion 2

def main():
    a, b = map(int, input().split())
    if (a * b) % 2 == 0:
        print("No")
    else:
        print("Yes")

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    if (a * b) % 2 == 1:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    A, B = map(int, input().split())
    if A*B % 2 == 1:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    a, b = list(map(int, input().split()))
    if (a * b) % 2 == 0:
        print("No")
    else:
        print("Yes")

=======
Suggestion 6

def main():
    a, b = map(int, input().split())
    if a*b%2 == 1:
        print("Yes")
    else:
        print("No")
    return

=======
Suggestion 7

def main():
    a = input()
    b = input()
    if (int(a)*int(b)*3)%2==0:
        print("No")
    else:
        print("Yes")

=======
Suggestion 8

def checkOdd(a, b):
    if a*b%2 == 0:
        return False
    else:
        return True

a, b = input().split()
a = int(a)
b = int(b)
