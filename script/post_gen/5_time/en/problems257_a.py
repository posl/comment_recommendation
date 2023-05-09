Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, X = map(int, input().split())
    print(chr(ord('A') + (X - 1) % 26))

=======
Suggestion 2

def main():
    n, x = map(int, input().split())
    print(chr(ord('A') + x // n - 1))

=======
Suggestion 3

def main():
    n, x = map(int, input().split())
    print(chr(x + 64))

=======
Suggestion 4

def main():
    n, x = map(int, input().split())
    print(chr(65 + x // n - 1))

=======
Suggestion 5

def solve():
    n, x = map(int, input().split())
    print(chr(x - 1 + ord('A')))

=======
Suggestion 6

def main():
    N, X = map(int, input().split())
    print(chr(X + 64))

=======
Suggestion 7

def solve():
    N,X = map(int,input().split())
    print(chr(ord('A')+X//N-1))

=======
Suggestion 8

def problem257_a():
    n, x = map(int, input().split())
    print(chr(x-1+ord('A')*(x-1)//n))

=======
Suggestion 9

def problem257_a():
    # Get input
    n, x = map(int, input().split())
    # Get the first part of the string
    first_part = x // n
    # Get the second part of the string
    second_part = x % n
    # Get the character
    character = chr(65 + second_part - 1)
    # Print the character
    print(character)
