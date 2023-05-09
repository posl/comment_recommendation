Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    n = int(input())
    print(1000 - (n % 1000) if n % 1000 != 0 else 0)

=======
Suggestion 2

def main():
    n = int(input())
    print(1000 - n % 1000 if n % 1000 != 0 else 0)

=======
Suggestion 3

def main():
    n = int(input())
    print(1000 - (n % 1000) if n % 1000 else 0)

=======
Suggestion 4

def main():
    N = int(input())
    print(1000 - N%1000 if N%1000 != 0 else 0)

=======
Suggestion 5

def main():
    n = int(input())
    print(1000 - n % 1000)

=======
Suggestion 6

def change(n):
    if n%1000 == 0:
        return 0
    else:
        return 1000 - (n%1000)

print(change(int(input())))

=======
Suggestion 7

def main():
    # Take input Here and Call solution function
    n = int(input())
    print(solution(n))

=======
Suggestion 8

def change(n):
    return 1000 - (n % 1000)

=======
Suggestion 9

def change(N):
    return 1000 - N % 1000

=======
Suggestion 10

def change(N):
    return 1000 - (N%1000)
