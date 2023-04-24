Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    if n % 1000 == 0:
        print(0)
    else:
        print(1000 - (n % 1000))

=======
Suggestion 2

def main():
    n = int(input())
    print(1000 - (n % 1000) if n % 1000 != 0 else 0)

=======
Suggestion 3

def main():
    N = int(input())
    print(1000 - N % 1000 if N % 1000 != 0 else 0)

=======
Suggestion 4

def solve():
    N = int(input())
    print(1000 - (N % 1000) if N % 1000 != 0 else 0)

=======
Suggestion 5

def main():
    N = int(input())
    if N%1000 == 0:
        print(0)
    else:
        print(1000 - (N%1000))

=======
Suggestion 6

def main():
    n = int(input())
    print(1000 - (n % 1000) if n % 1000 > 0 else 0)

=======
Suggestion 7

def main():
    N = int(input())
    print(1000 - N % 1000 if N % 1000 != 0 else 0)

main()

=======
Suggestion 8

def calcChange(n):
    return 1000 - (n % 1000)
