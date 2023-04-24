Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    if (a * b) % 2 == 0:
        print("No")
    else:
        print("Yes")

=======
Suggestion 2

def main():
    A, B = map(int, input().split())
    if (A * B) % 2 == 0:
        print("No")
    else:
        print("Yes")

=======
Suggestion 3

def main():
    A, B = map(int, input().split())
    if (A == 1 and B == 1) or (A == 1 and B == 2) or (A == 2 and B == 1):
        print("No")
    else:
        print("Yes")

=======
Suggestion 4

def main():
    A, B = map(int, input().split())
    if (A * B) % 2 == 1:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    a, b = map(int, input().split())
    if (a * b) % 2 == 0:
        print('No')
    else:
        print('Yes')

=======
Suggestion 6

def main():
    a, b = map(int, input().split())
    if a % 2 == 1 and b % 2 == 1:
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def main():
    A, B = map(int, input().split())
    odd = False
    for i in range(1, 4):
        if (A * B * i) % 2 == 1:
            odd = True
    if odd:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    a,b = map(int,input().split())
    if a%2==1 and b%2==1:
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def main():
    a, b = map(int, input().split())
    print("Yes" if (a * b) % 2 == 1 else "No")
    return

=======
Suggestion 10

def main():
    # Read a line
    line = input()
    # Split a line
    a, b = line.split()
    # Convert to integer
    a = int(a)
    b = int(b)
    # Output Yes or No
    if a * b % 2 == 1:
        print("Yes")
    else:
        print("No")
