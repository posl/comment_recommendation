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

def main():
    N = int(input())
    if N <= 125:
        print(4)
    elif 126 <= N <= 211:
        print(6)
    else:
        print(8)

=======
Suggestion 4

def problems214_a():
    N = int(input())
    if N >= 212:
        print(8)
    elif N >= 126:
        print(6)
    else:
        print(4)

=======
Suggestion 5

def get_problem_num(n):
    if n <= 125:
        return 4
    elif n <= 211:
        return 6
    else:
        return 8
