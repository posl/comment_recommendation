Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    n = int(input())
    if n <= 125:
        print(4)
    elif n <= 211:
        print(6)
    else:
        print(8)

=======
Suggestion 2

def main():
    N = int(input())
    if N <= 125:
        print(4)
    elif N <= 211:
        print(6)
    else:
        print(8)

=======
Suggestion 3

def abc(n):
    if n <= 125:
        return 4
    elif n <= 211:
        return 6
    else:
        return 8

print(abc(int(input())))

=======
Suggestion 4

def problems214_a():
    n = int(input())
    if n < 126:
        print(4)
    elif n < 212:
        print(6)
    else:
        print(8)

=======
Suggestion 5

def ABC(N):
    if N <= 125:
        return 4
    elif N <= 211:
        return 6
    else:
        return 8

=======
Suggestion 6

def problem214_a():
    n = int(input())
    if n <= 125:
        print(4)
    elif n >= 126 and n <= 211:
        print(6)
    else:
        print(8)
problem214_a()

=======
Suggestion 7

def calcABC(n):
    if n <= 125:
        return 4
    elif n <= 211:
        return 6
    else:
        return 8

=======
Suggestion 8

def get_problem_count():
    problem_count = 0

    n = int(input("Enter the number of ABC contests: "))

    if n >= 1 and n <= 125:
        problem_count = 4
    elif n >= 126 and n <= 211:
        problem_count = 6
    elif n >= 212 and n <= 214:
        problem_count = 8

    return problem_count

print(get_problem_count())
